---
File: tests/helpers/integration.js
Size: 5380 bytes
Lines: 192
---
// Licensed under the Apache License, Version 2.0 (the 'License'); you may not
// use this file except in compliance with the License. You may obtain a copy of
// the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations under
// the License.

'use strict';

var async = require('async');
var debug = require('debug');
var path = require('path');
var harness = require('tape-it');
var endsWith = require('endswith');
var cfg = require('../fixtures/cfg');
var nano = require('../../lib/nano');
var helpers = require('./');

helpers.setup = function() {
  var self = this;
  var args = Array.prototype.slice.call(arguments);

  return function(assert) {
    args.push(function(err) {
      assert.equal(err, null, 'create database');
      assert.end();
    });

    self.nano.db.create.apply(this, args);
  };
};

helpers.teardown = function() {
  var self = this;
  var args = Array.prototype.slice.call(arguments);

  return function(assert) {
    args.push(function(err) {
      assert.equal(err, null, 'destroy database');
      assert.ok(self.mock.isDone(), 'mocks didn\'t run');
      assert.end();
    });

    self.nano.db.destroy.apply(this, args);
  };
};

helpers.harness = function(name, setup, teardown) {
  var parent = name || module.parent.filename;
  var fileName = path.basename(parent).split('.')[0];
  var parentDir = path.dirname(parent)
    .split(path.sep).reverse()[0];
  var shortPath = path.join(parentDir, fileName);
  var log = debug(path.join('nano', 'tests', 'integration', shortPath));
  var dbName = shortPath.replace('/', '_');
  var nanoLog = nano({
    url: cfg.couch,
    log: log
  });

  var mock = helpers.nock(helpers.couch, shortPath, log);
  var db   = nanoLog.use(dbName);
  var locals = {
    mock: mock,
    db: db,
    nano: nanoLog
  };

  return harness({
    id: shortPath,
    timeout: helpers.timeout,
    checkLeaks: !!process.env.LEAKS,
    locals: locals,
    setup: setup ? setup : helpers.setup.call(locals, dbName),
    teardown: teardown ? teardown : helpers.teardown.call(locals, dbName)
  });
};

helpers.nock = function helpersNock(url, fixture, log) {
  var nock = require('nock');
  var nockDefs = require('../fixtures/' + fixture + '.json');

  nockDefs.forEach(function(n) {
    var headers = n.headers || {};
    var response = n.buffer ? endsWith(n.buffer, '.png') ?
        helpers.loadFixture(n.buffer) : new Buffer(n.buffer, 'base64') :
        n.response || '';
    var body = n.base64 ? new Buffer(n.base64, 'base64').toString() :
        n.body || '';

    if (typeof headers === 'string' && endsWith(headers, '.json')) {
      headers = require(path.join(fixture, headers));
    }

    n.method = n.method || 'get';
    n.options = {log: log};
    n.scope = url;
    n.headers = headers;
    n.response = response;
    n.body = body;

    return n;
  });

  nock.define(nockDefs);

  return nock(url);
};

helpers.prepareAView = function(assert, search, db) {
  search = search || '';
  db = db || this.db;

  db.insert({
    views: {
      by_name_and_city: {
        map: 'function(doc) { emit([doc.name, doc.city], doc._id); }'
      }
    },
    lists: {
      'my_list': 'function(head, req) { send(\'Hello\'); }'
    }
  }, '_design/people' + search, function(error, response) {
    assert.equal(error, null, 'should create view');
    assert.equal(response.ok, true, 'response is good');
    async.parallel([
      function(cb) {
        db.insert({
          name: 'Derek',
          city: 'San Francisco'
        }, 'p_derek', cb);
      }, function(cb) {
        db.insert({
          name: 'Randall',
          city: 'San Francisco'
        }, 'p_randall', cb);
      }, function(cb) {
        db.insert({
          name: 'Nuno',
          city: 'London'
        }, 'p_nuno', cb);
      }
    ], function(error) {
      assert.equal(error, undefined, 'store the peeps');
      assert.end();
    });
  });
};

helpers.viewDerek = function viewDerek(db, assert, opts, next, method) {
  method = method || 'view';
  db[method]('people','by_name_and_city', opts, function(error, view) {
    assert.equal(error, null, 'no errors');
    assert.equal(view.rows.length,1);
    assert.equal(view.rows.length,1);
    assert.equal(view.rows[0].id,'p_derek');
    assert.equal(view.rows[0].key[0],'Derek');
    assert.equal(view.rows[0].key[1],'San Francisco');
    next(error);
  });
};

helpers.insertOne = function insertThree(assert) {
  var db = this.db;
  db.insert({'foo': 'baz'}, 'foobaz', function(err) {
    assert.equal(err, null, 'should store docs');
    assert.end();
  });
};

helpers.insertThree = function insertThree(assert) {
  var db = this.db;
  async.parallel([
    function(cb) { db.insert({'foo': 'bar'}, 'foobar', cb); },
    function(cb) { db.insert({'bar': 'foo'}, 'barfoo', cb); },
    function(cb) { db.insert({'foo': 'baz'}, 'foobaz', cb); }
  ], function(error) {
    assert.equal(error, undefined, 'should store docs');
    assert.end();
  });
};

helpers.unmocked = (process.env.NOCK_OFF === 'true');
helpers.mocked = !helpers.unmocked;

module.exports = helpers;



---
File: tests/helpers/unit.js
Size: 3842 bytes
Lines: 151
---
// Licensed under the Apache License, Version 2.0 (the 'License'); you may not
// use this file except in compliance with the License. You may obtain a copy of
// the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations under
// the License.

'use strict';

var helpers = require('./');
var Client = require('../../lib/nano');
var test  = require('tape');
var _ = require('underscore');

helpers.unit = function(method, error) {
  var unitName = 'nano/tests/unit/' + method.join('/');
  var debug = require('debug')(unitName);

  function log(data) {
    debug({ got: data.body });
  }

  var cli = helpers.mockClientOk(log, error);

  //
  // allow database creation and other server stuff
  //
  if(method[1].match(/follow/)) {
    if(method[0] === 'database') {
      cli.server = helpers.mockClientFollow(log, error);
    } else {
      cli = helpers.mockClientFollow(log, error);
    }
  } else {
    cli.server = helpers.mockClientDb(log, error);
  }

  var testNr = 1;

  return function() {
    var args = Array.prototype.slice.call(arguments);
    var stub = args.pop();

    test(unitName + ':' + testNr++,
    function(assert) {
      var f;
      assert.ok(typeof stub, 'object');

      //
      // document functions and database functions
      // are at the top level in nano
      //
      if(method[0] === 'database') {
        f = cli.server.db[method[1]];
      } else if(method[0] === 'view' && method[1] === 'compact') {
        f = cli.view.compact;
      } else if(!~['multipart', 'attachment'].indexOf(method[0])) {
        f = cli[method[1]];
      } else {
        f = cli[method[0]][method[1]];
      }
      assert.ok(typeof f, 'function');

      args.push(function(err, req, response) {
        if (error) {
          assert.ok(err);
          return assert.end();
        }

        assert.equal(response.statusCode, 200);
        if(stub.uri) {
          stub.uri = helpers.couch + stub.uri;
        } else {
          stub.db = helpers.couch + stub.db;
        }

        assert.deepEqual(req, stub);
        assert.end();
      });

      f.apply(null, args);
    });
  };
};

function mockClient(code, path, extra) {
  return function(debug, error) {
    extra = extra || {};
    var opts = _.extend(extra, {
      url: helpers.couch + path,
      log: debug,
      request: function(req, cb) {
        if(error) {
          return cb(error);
        }

        if(code === 500) {
          cb(new Error('omg connection failed'));
        } else {
          cb(null, {
            statusCode: code,
            headers: {}
          }, req); }
        }
    });

    return Client(opts);
  };
}

function mockClientUnparsedError() {
  return function(debug, body) {
    return Client({
      url: helpers.couch,
      log: debug,
      request: function(_, cb) {
        return cb(null, {statusCode: 500}, body || '<b> Error happened </b>');
      }
    });
  };
}

function mockClientFollow() {
  return function(debug, error) {
    return Client({
      url: helpers.couch,
      log: debug,
      follow: function(qs, cb) {
        if(error) {
          return cb(error);
        }

        return cb(null, qs,  {statusCode: 200});
      }
    });
  };
}


helpers.mockClientFollow = mockClientFollow();
helpers.mockClientUnparsedError = mockClientUnparsedError();
helpers.mockClientDb = mockClient(200, '');
helpers.mockClientOk = mockClient(200, '/mock');
helpers.mockClientFail = mockClient(500, '');
helpers.mockClientJar = mockClient(300, '', {jar: 'is set'});
module.exports = helpers;


---
File: tests/integration/attachment/update.js
Size: 1772 bytes
Lines: 50
---
// Licensed under the Apache License, Version 2.0 (the 'License'); you may not
// use this file except in compliance with the License. You may obtain a copy of
// the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations under
// the License.

'use strict';

var helpers = require('../../helpers/integration');
var pixel = helpers.pixel;
var harness = helpers.harness(__filename);
var db = harness.locals.db;
var it = harness.it;

var rev;

it('should be able to insert and update attachments', function(assert) {
  var buffer = new Buffer(pixel, 'base64');
  db.attachment.insert('new', 'att', 'Hello', 'text/plain',
  function(error, hello) {
    assert.equal(error, null, 'should store hello');
    assert.equal(hello.ok, true, 'response ok');
    assert.ok(hello.rev, 'should have a revision number');
    db.attachment.insert('new', 'att', buffer, 'image/bmp',
    {rev: hello.rev}, function(error, bmp) {
      assert.equal(error, null, 'should store the pixel');
      assert.ok(bmp.rev, 'should store a revision');
      rev = bmp.rev;
      assert.end();
    });
  });
});

it('should be able to fetch the updated pixel', function(assert) {
  db.get('new', function(error, newDoc) {
    assert.equal(error, null, 'should get new');
    newDoc.works = true;
    db.insert(newDoc, 'new', function(error, response) {
      assert.equal(error, null, 'should update doc');
      assert.equal(response.ok, true, 'response ok');
      assert.end();
    });
  });
});


---
File: tests/integration/attachment/destroy.js
Size: 1577 bytes
Lines: 41
---
// Licensed under the Apache License, Version 2.0 (the 'License'); you may not
// use this file except in compliance with the License. You may obtain a copy of
// the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations under
// the License.

'use strict';

var helpers = require('../../helpers/integration');
var harness = helpers.harness(__filename);
var it = harness.it;
var db = harness.locals.db;

it('should be able to insert a new plain text attachment', function(assert) {
  db.attachment.insert('new',
  'att', 'Hello World!', 'text/plain', function(error, att) {
    assert.equal(error, null, 'store the attachment');
    assert.equal(att.ok, true, 'response ok');
    assert.ok(att.rev, 'have a revision number');
    db.attachment.destroy('new', 'att', {rev: att.rev},
    function(error, response) {
      assert.equal(error, null, 'delete the attachment');
      assert.equal(response.ok, true, 'response ok');
      assert.equal(response.id, 'new', '`id` should be `new`');
      assert.end();
    });
  });
});

it('should fail destroying with a bad filename', function(assert) {
  db.attachment.destroy('new', false, true, function(error, response) {
    assert.equal(response, undefined, 'no response should be given');
    assert.end();
  });
});


---
File: tests/integration/attachment/get.js
Size: 1864 bytes
Lines: 48
---
// Licensed under the Apache License, Version 2.0 (the 'License'); you may not
// use this file except in compliance with the License. You may obtain a copy of
// the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations under
// the License.

'use strict';

var helpers = require('../../helpers/integration');
var harness = helpers.harness(__filename);
var it = harness.it;
var db = harness.locals.db;

it('should be able to fetch an attachment', function(assert) {
  db.attachment.insert('new_string', 'att', 'Hello', 'text/plain',
  function(error, hello) {
    assert.equal(error, null, 'should store `hello`');
    assert.equal(hello.ok, true, 'response ok');
    assert.ok(hello.rev, 'should have a revision number');
    db.attachment.get('new_string', 'att',
    function(error, helloWorld) {
      assert.equal(error, null, 'should get `hello`');
      assert.equal('Hello', helloWorld.toString(), 'string is reflexive');
      assert.end();
    });
  });
});

it('should insert and fetch a binary file', function(assert) {
  db.attachment.insert('new_binary', 'att', new Buffer('123'),
  'text/plain', function(error, hello) {
    assert.equal(error, null, 'should store `123`');
    assert.equal(hello.ok, true, 'response ok');
    assert.ok(hello.rev, 'should have a revision number');
    db.attachment.get('new_binary', 'att',
    function(error, binaryData) {
      assert.equal(error, null, 'should get the binary data');
      assert.equal('123', binaryData.toString(), 'binary data is reflexive');
      assert.end();
    });
  });
});


---
File: tests/integration/attachment/pipe.js
Size: 1958 bytes
Lines: 57
---
// Licensed under the Apache License, Version 2.0 (the 'License'); you may not
// use this file except in compliance with the License. You may obtain a copy of
// the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations under
// the License.

'use strict';

var fs = require('fs');
var path = require('path');
var helpers = require('../../helpers/integration');
var harness = helpers.harness(__filename);
var db = harness.locals.db;
var it = harness.it;
var pixel = helpers.pixel;

it('should be able to pipe to a writeStream', function(assert) {
  var buffer = new Buffer(pixel, 'base64');
  var filename = path.join(__dirname, '.temp.bmp');
  var ws = fs.createWriteStream(filename);

  ws.on('close', function() {
    assert.equal(fs.readFileSync(filename).toString('base64'), pixel);
    fs.unlinkSync(filename);
    assert.end();
  });

  db.attachment.insert('new', 'att', buffer, 'image/bmp',
  function(error, bmp) {
    assert.equal(error, null, 'Should store the pixel');
    db.attachment.get('new', 'att', {rev: bmp.rev}).pipe(ws);
  });
});

it('should be able to pipe from a readStream', function(assert) {
  var logo = path.join(__dirname, '..', '..', 'fixtures', 'logo.png');
  var rs = fs.createReadStream(logo);
  var is = db.attachment.insert('nodejs', 'logo.png', null, 'image/png');

  is.on('end', function() {
    db.attachment.get('nodejs', 'logo.png', function(err, buffer) {
      assert.equal(err, null, 'should get the logo');
      assert.equal(
        fs.readFileSync(logo).toString('base64'), buffer.toString('base64'),
        'logo should remain unchanged');
      assert.end();
    });
  });

  rs.pipe(is);
});


---
File: tests/integration/attachment/insert.js
Size: 1063 bytes
Lines: 28
---
// Licensed under the Apache License, Version 2.0 (the 'License'); you may not
// use this file except in compliance with the License. You may obtain a copy of
// the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations under
// the License.

'use strict';

var helpers = require('../../helpers/integration');
var harness = helpers.harness(__filename);
var it = harness.it;
var db = harness.locals.db;

it('should be able to insert a simple attachment', function(assert) {
  db.attachment.insert('new', 'att', 'Hello World!', 'text/plain',
  function(error, att) {
    assert.equal(error, null, 'should store the attachment');
    assert.equal(att.ok, true, 'response ok');
    assert.ok(att.rev, 'should have a revision');
    assert.end();
  });
});


---
File: tests/integration/shared/updates.js
Size: 1813 bytes
Lines: 60
---
// Licensed under the Apache License, Version 2.0 (the 'License'); you may not
// use this file except in compliance with the License. You may obtain a copy of
// the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations under
// the License.

'use strict';

var helpers = require('../../helpers/integration');
var harness = helpers.harness(__filename, helpers.noopTest, helpers.noopTest);
var it = harness.it;
var nano = harness.locals.nano;

it('should be able to track updates in couch', function(assert) {
  var called = false;

  function getUpdates() {
    nano.updates(function(err, updates) {
      if (called) {
        return;
      }
      called = true;

      if (err && updates.error && updates.error === 'illegal_database_name') {
        //
        // older couches
        //
        assert.expect(1);
        assert.ok(updates.ok, 'db updates are not supported');
        assert.end();
      } else {
        //
        // new couches
        //
        assert.equal(err, null, 'got root');
        assert.ok(updates.ok, 'updates are ok');
        assert.equal(updates.type, 'created', 'update was a create');
        assert.equal(updates['db_name'], 'mydb', 'mydb was updated');
        assert.end();
      }
    });

    setTimeout(function() { nano.db.create('mydb'); }, 50);
  }

  nano.db.destroy('mydb', getUpdates);
});

it('should destroy mydb', function(assert) {
  nano.db.destroy('mydb', function(err) {
    assert.equal(err, null, 'no errors');
    assert.end();
  });
});


---
File: tests/integration/shared/log.js
Size: 1003 bytes
Lines: 30
---
// Licensed under the Apache License, Version 2.0 (the 'License'); you may not
// use this file except in compliance with the License. You may obtain a copy of
// the License at
//
//   http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on