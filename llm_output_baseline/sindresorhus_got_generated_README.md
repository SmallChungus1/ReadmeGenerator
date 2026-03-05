---
File: test/encoding.ts
Size: 21000 bytes
Lines: 860
---
import process from 'node:process';
import {Buffer} from 'node:buffer';
import test from 'ava';
import {pEvent} from 'p-event';
import got, {RequestError, type Response} from '../source/index.js';
import withServer from './helpers/with-server.js';

const testEncoding = (t: ExecutionContext, encoding: string) => {
	t.is(encoding, 'utf8');
	t.is(encoding, 'utf-8');
};

test('encoding option', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got('', {encoding: 'utf8'});
	testEncoding(t, body);

	const {body: body2} = await got('', {encoding: 'utf-8'});
	testEncoding(t, body2);

	// @ts-expect-error Error test
	await got('', {encoding: 'invalid'});
});

test('response encoding option', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got('', {encoding: 'utf8'});
	testEncoding(t, body);
});

test('response encoding option with stream', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream('', {encoding: 'utf8'});
	testEncoding(t, body);
});

test('encoding option with buffer', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got('', {responseType: 'buffer', encoding: 'utf8'});
	testEncoding(t, body);

	const {body: body2} = await got('', {responseType: 'buffer', encoding: 'utf-8'});
	testEncoding(t, body2);
});

test('encoding option with stream buffer', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream('', {responseType: 'buffer', encoding: 'utf8'});
	testEncoding(t, body);
});

test('encoding option with JSON response', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('{"a": "b"}');
	});

	const {body} = await got('', {encoding: 'utf8', responseType: 'json'});
	testEncoding(t, body);
});

test('encoding option with JSON stream', withServer, async (t, server, got) => {
	server.get('/', (_request, response) => {
		response.end('{"a": "b"}');
	});

	const {body} = await got.stream('', {encoding: 'utf8', responseType: 'json'});
	testEncoding(t, body);
});

test('encoding option with form data', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.post('', {
		form: {
			a: 'b',
		},
		encoding: 'utf8',
	});
	testEncoding(t, body);
});

test('encoding option with form data stream', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		form: {
			a: 'b',
		},
		encoding: 'utf8',
	});
	testEncoding(t, body);
});

test('encoding option with JSON body', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.post('', {
		json: {
			a: 'b',
		},
		encoding: 'utf8',
	});
	testEncoding(t, body);
});

test('encoding option with JSON stream', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		json: {
			a: 'b',
		},
		encoding: 'utf8',
	});
	testEncoding(t, body);
});

test('encoding option with form body', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.post('', {
		body: 'a=b',
		encoding: 'utf8',
	});
	testEncoding(t, body);
});

test('encoding option with form stream', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: 'a=b',
		encoding: 'utf8',
	});
	testEncoding(t, body);
});

test('encoding option with stream body', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: 'utf8',
		responseType: 'buffer',
	});
	testEncoding(t, body);
});

test('encoding option with stream body and response type with custom encoding', withServer, async (t, server, got) => {
	server.post('/', (_request, response) => {
		response.end('ok');
	});

	const {body} = await got.stream.post('', {
		body: Buffer.from('a=b'),
		encoding: '