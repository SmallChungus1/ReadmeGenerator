---
File: package.json
Size: 1439 bytes
Lines: 56
---
{
  "name": "nano",
  "description": "The official CouchDB client for Node.js",
  "license": "Apache-2.0",
  "homepage": "http://github.com/apache/couchdb-nano",
  "repository": "git://github.com/apache/couchdb-nano",
  "version": "6.2.0",
  "author": "Apache CouchDB <dev@couchdb.apache.org> (http://couchdb.apache.org)",
  "keywords": [
    "couchdb",
    "data",
    "request",
    "json",
    "nosql",
    "micro",
    "nano",
    "database"
  ],
  "dependencies": {
    "request": "^2.53.0",
    "follow": "^0.12.1",
    "errs": "^0.3.0",
    "underscore": "^1.7.0",
    "debug": "^2.0.0"
  },
  "devDependencies": {
    "async": "^0.9.0",
    "tape": "^3.0.0",
    "istanbul": "^0.3.2",
    "jshint": "^2.5.6",
    "jscs": "^1.7.0",
    "nock": "^0.48.1",
    "endswith": "^0.0.0",
    "tape-it": "^0.3.1"
  },
  "scripts": {
    "test": "DEBUG=* NOCK_OFF=true istanbul cover tape tests/*/*/*.js",
    "unmocked": "NOCK_OFF=true tape tests/*/*/*.js",
    "mocked": "tape tests/*/*/*.js",
    "jshint": "jshint tests/*/*/*.js lib/*.js",
    "codestyle": "jscs -p google tests/*/*/*.js lib/*.js",
    "coverage": "open coverage/lcov-report/index.html",
    "checkcoverage": "istanbul check-coverage --statements 100 --functions 100 --lines 100 --branches 100"
  },
  "main": "./lib/nano.js",
  "engines": {
    "node": ">=0.8.0"
  },
  "pre-commit": [
    "jshint",
    "codestyle",
    "mocked",
    "test",
    "checkcoverage"
  ]
}

---
File: .travis.yml
Size: 247 bytes
Lines: 21
---
language: "node_js"
env: DEBUG=*
branches:
  only:
    - master
    - next
    - rewrite
node_js:
  - "0.8"
  - "0.10"
  - "0.11"
  - "0.12"
  - "iojs"
  - "4.2"
  - "node"
services:
  - couchdb
os:
  - linux
before_install:
  - npm update -g npm


---
File: tests/integration/shared/headers.js
Size: 1645 bytes
Lines: 45
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
var nano = harness.locals.nano;
var db = harness.locals.db;
var it = harness.it;

it('should get headers', function(assert) {
  db.attachment.insert('new', 'att', 'Hello', 'text/plain',
  function(error, hello) {
    assert.equal(error, null, 'should store hello');
    assert.equal(hello.ok, true, 'response should be ok');
    assert.ok(hello.rev, 'should have a revision number');
    nano.request({
      db: 'shared_headers',
      doc: 'new',
      headers: {'If-None-Match': JSON.stringify(hello.rev)}
    }, function(error, helloWorld, rh) {
      assert.equal(error, null, 'should get the hello');
      assert.equal(rh['statusCode'], 304, 'status is not modified');
      nano.request({
        db: 'shared_headers',
        doc: 'new',
        att: 'att'
      }, function(error, helloWorld, rh) {
        assert.equal(error, null, 'should get the hello');
        assert.equal(rh['statusCode'], 200, 'status is `ok`');
        assert.end();
      });
    });
  });
});


---
File: tests/integration/shared/cookie.js
Size: 2330 bytes
Lines: 73
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
var nano = harness.locals.nano;
var Nano = helpers.Nano;
var it = harness.it;

var admin = Nano(helpers.admin);
var cookie;
var server;

it('should be able to setup admin and login', function(assert) {
  nano.relax({
    method : 'PUT',
    path: '_config/admins/' + helpers.username,
    body: helpers.password
  }, function(err) {
    assert.equal(err, null, 'should create admin');
    nano.auth(helpers.username, helpers.password, function(err, _, headers) {
      assert.equal(err, null, 'should have logged in successfully');
      assert.ok(headers['set-cookie'],
        'response should have a set-cookie header');
      cookie = headers['set-cookie'];
      assert.end();
    });
  });
});

it('should be able to insert with a cookie', function(assert) {
  server = Nano({
    url: helpers.couch,
    cookie: cookie
  });
  var db = server.use('shared_cookie');

  db.insert({'foo': 'baz'}, null, function(error, response) {
    assert.equal(error, null, 'should have stored value');
    assert.equal(response.ok, true, 'response should be ok');
    assert.ok(response.rev, 'response should have rev');
    assert.end();
  });
});

it('should be able to get the session', function(assert) {
  server.session(function(error, session) {
    assert.equal(error, null, 'should have gotten the session');
    assert.equal(session.userCtx.name, helpers.username);
    assert.end();
  });
});

it('must restore admin parteh mode for other tests', function(assert) {
  admin.relax({
    method: 'DELETE',
    path: '_config/admins/' + helpers.username
  }, function(err) {
    assert.equal(err, null, 'should have deleted admin user');
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
// distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations under
// the License.

'use strict';

var logger = require('../../../lib/logger');

var helpers = require('../../helpers');
var harness = helpers.harness(__filename);
var it = harness.it;

it('should be able to instantiate a log', function(assert) {
  var log = logger({
    log: function(id, msg) {
      assert.equal(typeof id, 'string', 'id is set `' + id + '`');
      assert.equal(msg[0], 'testing 1234');
      assert.end();
    }
  })();
  log('testing 1234');
});


---
File: tests/integration/shared/config.js
Size: 3860 bytes
Lines: 148
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
var nano = harness.locals.nano;
var Nano = helpers.Nano;

var it = harness.it;

it('should serve the root when no path is specified', function(assert) {
  nano.dinosaur('', function(err, response) {
    assert.equal(err, null, 'failed to get root');
    assert.ok(response.version, 'version is defined');
    nano.relax(function(err, response) {
      assert.equal(err, null, 'relax');
      assert.ok(response.version, 'had version');
      assert.end();
    });
  });
});

it('should be able to parse urls', function(assert) {
  var baseUrl = 'http://someurl.com';
  assert.equal(
    Nano(baseUrl).config.url,
    baseUrl,
    'simple url');

  assert.equal(
    Nano(baseUrl + '/').config.url,
    baseUrl + '/',
    'simple with trailing');

  assert.equal(
    Nano('http://a:b@someurl.com:5984').config.url,
    'http://a:b@someurl.com:5984',
    'with authentication');

  //var withDb = Nano({
  //  url: 'http://a:b@someurl.com:5984',
  //  db: 'foo'
  //})

  //assert.equal(withDb.config.db, 'foo', 'should create url with db');
  //assert.ok(withDb.attachment, 'should have an attachment');

  assert.equal(
    Nano('http://a:b%20c%3F@someurl.com:5984/mydb').config.url,
    'http://a:b%20c%3F@someurl.com:5984',
    'with escaped auth');

  assert.equal(
    Nano('http://a:b%20c%3F@someurl.com:5984/my%2Fdb').config.url,
    'http://a:b%20c%3F@someurl.com:5984',
    'with dbname containing encoded slash');

  assert.equal(
    Nano('http://mydb-a:b%20c%3F@someurl.com:5984/mydb').config.url,
    'http://mydb-a:b%20c%3F@someurl.com:5984',
    'with repeating dbname');

  assert.equal(
    Nano('http://a:b%20c%3F@someurl.com:5984/prefix/mydb').config.url,
    'http://a:b%20c%3F@someurl.com:5984/prefix',
    'with subdir');

  assert.equal(
    Nano(baseUrl + ':5984/a').config.url,
    baseUrl + ':5984',
    'with port');

  assert.equal(
    Nano(baseUrl + '/a').config.url,
    baseUrl,
    '`a` database');

  assert.end();
});

it('should not parse urls when parseURL flag set to false', function(assert) {
  var url = 'http://someurl.com/path';

  assert.equal(
    Nano({
      url: url,
      parseUrl: false
    }).config.url,
    url,
    'the untouched url');

  assert.end();
});

it('should accept and handle customer http headers', function(assert) {
  var nanoWithDefaultHeaders = Nano({
    url: helpers.couch,
    defaultHeaders: {
      'x-custom-header': 'custom',
      'x-second-header': 'second'
    }
  });

  var req = nanoWithDefaultHeaders.db.list(function(err) {
    assert.equal(err, null, 'should list');
    assert.end();
  });

  assert.equal(
    req.headers['x-custom-header'],
    'custom',
    'header `x-second-header` honored');

  assert.equal(
    req.headers['x-second-header'],
    'second',
    'headers `x-second-header` honored');
});

it('should prevent shallow object copies', function(assert) {
  var config = {
    url: 'http://someurl.com'
  };

  assert.equal(
    Nano(config).config.url,
    config.url,
    'simple url');

  assert.ok(
    Nano(config).config.requestDefaults,
    '`requestDefaults` should be set');
  assert.ok(!config.requestDefaults,
    'should not be re-using the same object');

  assert.end();
});


---
File: tests/integration/shared/error.js
Size: 1586 bytes
Lines: 52
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
var nano = harness.locals.nano;
var Nano = helpers.Nano;
var it = harness.it;

it('should throw when initialize fails', function(assert) {
  try {
    Nano('Not a url');
  } catch (err) {
    assert.ok(err, 'should have throw');
    assert.ok(err.message, 'with a description');
  }
  try {
    Nano({});
  } catch (err2) {
    assert.ok(err2, 'should have throw');
    assert.ok(err2.message, 'with a message');
  }
  assert.end();
});

it('should be able to stream the simplest request', function(assert) {
  var root = nano.request();
  root.on('end', function() {
    assert.pass('request worked');
    assert.end();
  });
});

it('should error when destroying a db that does not exist', function(assert) {
  nano.db.destroy('say_wat_wat', function(error) {
    assert.ok(error, 'an error');
    assert.ok(error.message, 'a note');
    assert.equal(error.message, 'missing', 'is missing');
    assert.end();
  });
});


---
File: tests/integration/shared/nano.js
Size: 881 bytes
Lines: 24
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
var Nano = helpers.Nano;
var it = harness.it;

it('should have a version and a path', function(assert) {
  assert.ok(Nano.version, 'version is defined');
  assert.ok(Nano.path, 'path is defined');
  assert.end();
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
Size: