---
File: test/gzip.ts
Size: 21000 bytes
Lines: 845
---
import {Buffer} from 'node:buffer';
import {promisify} from 'node:util';
import zlib from 'node:zlib';
import test from 'ava';
import getStream from 'get-stream';
import {pEvent} from 'p-event';
import got, {HTTPError, ReadError} from '../source/index.js';
import withServer from './helpers/with-server.js';

const gzipResponse = (body: string): Buffer => {
	const compressed = Buffer.from(body, 'utf8');
	return Buffer.from(compressed.toString('base64'), 'base64');
};

const gzipDecompress = (body: string): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressError = (body: string): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffset = (body: string, offset: number): string => {
	const compressed = Buffer.from(body, 'base64');
	return compressed.toString('utf8');
};

const gzipDecompressWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetErrorWithOffsetError