---
File: source\create.ts
Size: 9747 bytes
Lines: 334 [structural]
---
import {setTimeout as delay} from 'node:timers/promises';
import is, {assert} from '@sindresorhus/is';
import asPromise from './as-promise/index.js';
import type {
import Request from './core/index.js';
import type {Response} from './core/response.js';
import Options, {
import type {RequestPromise} from './as-promise/types.js';
const isGotInstance = (value: Got | ExtendOptions): value is Got => is.function(value);
const aliases: readonly HTTPAlias[] = [
const optionsObjectUrlErrorMessage = 'The `url` option is not supported in options objects. Pass it as the first argument instead.';
const assertNoUrlInOptionsObject = (options: Record<string, unknown>): void => {
const cloneWithProperty = <Value extends Record<string, unknown>>(value: Value, property: string, propertyValue: unknown): Value => {
	const clone = Object.create(Object.getPrototypeOf(value), Object.getOwnPropertyDescriptors(value)) as Value;
const create = (defaults: InstanceDefaults): Got => {
	const makeRequest = (url: string | URL | OptionsInit | undefined, options: OptionsInit | undefined, defaultOptions: Options, isStream: boolean): GotReturn => {
		const requestUrl = isStream && is.plainObject(url) ? cloneWithProperty(url, 'isStream', true) : url;
		const requestOptions = isStream && !is.plainObject(url) && options ? cloneWithProperty(options, 'isStream', true) : options;
		const request = new Request(requestUrl, requestOptions, defaultOptions);
		let promise: RequestPromise | undefined;
		const lastHandler = (normalized: Options): GotReturn => {
			const shouldReturnStream = normalized?.isStream ?? isStream;
		let iteration = 0;
		const iterateHandlers = (newOptions: Options): GotReturn => {
			const handler = defaults.handlers[iteration++] ?? lastHandler;
			const result = handler(newOptions, iterateHandlers) as GotReturn;
					const descriptors = Object.getOwnPropertyDescriptors(promise);
	const got: Got = ((url: string | URL | OptionsInit | undefined, options?: OptionsInit, defaultOptions: Options = defaults.options): GotReturn =>
	got.extend = (...instancesOrOptions) => {
		const options = new Options(undefined, undefined, defaults.options);
		const handlers = [...defaults.handlers];
		let mutableDefaults: boolean | undefined;
	const paginateEach = (async function * <T, R>(url: string | URL, options?: OptionsWithPagination<T, R>): AsyncIterableIterator<T> {
		let normalizedOptions = new Options(url, options as OptionsInit, defaults.options);
		const {pagination} = normalizedOptions;
		const allItems: T[] = [];
		let {countLimit} = pagination;
		let numberOfRequests = 0;
			const response = (await got(undefined, undefined, normalizedOptions)) as Response;
			const parsed: unknown[] = await pagination.transform(response);
			const currentItems: T[] = [];
			const requestOptions = response.request.options;
			const previousUrl = requestOptions.url ? new URL(requestOptions.url) : undefined;
			const previousState = previousUrl ? snapshotCrossOriginState(requestOptions) : undefined;
			const [optionsToMerge, changedState] = await requestOptions.trackStateMutations(async changedState => [
					const nextUrl = normalizedOptions.url as URL | undefined;
				const hasExplicitBody = (Object.hasOwn(optionsToMerge, 'body') && optionsToMerge.body !== undefined)
					const nextUrl = applyUrlOverride(normalizedOptions, optionsToMerge.url, optionsToMerge);
	got.paginate.all = (async <T, R>(url: string | URL, options?: OptionsWithPagination<T, R>) => Array.fromAsync(paginateEach<T, R>(url, options))) as GotPaginate['all'];
	got.stream = ((url: string | URL, options?: StreamOptions) =>
		got[method] = ((url: string | URL, options?: Options): GotReturn => got(url, {...options, method})) as GotRequestFunction;
		got.stream[method] = ((url: string | URL, options?: StreamOptions) =>
export default create;

---
File: source\index.ts
Size: 905 bytes
Lines: 27
---
import create from './create.js';
import type {InstanceDefaults} from './types.js';
import Options from './core/options.js';

const defaults: InstanceDefaults = {
	options: new Options(),
	handlers: [],
	mutableDefaults: false,
};

const got = create(defaults);

export default got;

export {default as Options} from './core/options.js';
export * from './core/options.js';
export * from './core/response.js';
export type {default as Request} from './core/index.js';
export * from './core/index.js';
export * from './core/errors.js';
export * from './core/diagnostics-channel.js';
export type {Delays} from './core/timed-out.js';
export {default as calculateRetryDelay} from './core/calculate-retry-delay.js';
export type * from './as-promise/types.js';
export type * from './types.js';
export {default as create} from './create.js';
export {default as parseLinkHeader} from './core/parse-link-header.js';


---
File: source\types.ts
Size: 12452 bytes
Lines: 341 [structural]
---
import type {Spread} from 'type-fest';
import type {RequestPromise} from './as-promise/types.js';
import type {Response} from './core/response.js';
import type Options from './core/options.js';
import {type PaginationOptions, type OptionsInit} from './core/options.js';
import type Request from './core/index.js';
type Except<ObjectType, KeysType extends keyof ObjectType> = Pick<ObjectType, Exclude<keyof ObjectType, KeysType>>;
type Merge<FirstType, SecondType> = Except<FirstType, Extract<keyof FirstType, keyof SecondType>> & SecondType;
export type InstanceDefaults = {
export type GotReturn = Request | RequestPromise;
export type HandlerFunction = <T extends GotReturn>(options: Options, next: (options: Options) => T) => T | Promise<T>;
export type ExtendOptions = {
export type StreamOptions = Except<OptionsInit, 'url'>;
export type StrictOptions = Except<StreamOptions, 'responseType' | 'resolveBodyOnly'>;
export type OptionsWithPagination<T = unknown, R = unknown> = Merge<StreamOptions, {pagination?: PaginationOptions<T, R>}>;
export type GotPaginate = {
export type OptionsOfTextResponseBody = Merge<StrictOptions, {responseType?: 'text'}>;
export type OptionsOfTextResponseBodyOnly = Merge<StrictOptions, {resolveBodyOnly: true; responseType?: 'text'}>;
export type OptionsOfTextResponseBodyWrapped = Merge<StrictOptions, {resolveBodyOnly: false; responseType?: 'text'}>;
export type OptionsOfJSONResponseBody = Merge<StrictOptions, {responseType?: 'json'}>; // eslint-disable-line @typescript-eslint/naming-convention
export type OptionsOfJSONResponseBodyOnly = Merge<StrictOptions, {resolveBodyOnly: true; responseType?: 'json'}>; // eslint-disable-line @typescript-eslint/naming-convention
export type OptionsOfJSONResponseBodyWrapped = Merge<StrictOptions, {resolveBodyOnly: false; responseType?: 'json'}>; // eslint-disable-line @typescript-eslint/naming-convention
export type OptionsOfBufferResponseBody = Merge<StrictOptions, {responseType?: 'buffer'}>;
export type OptionsOfBufferResponseBodyOnly = Merge<StrictOptions, {resolveBodyOnly: true; responseType?: 'buffer'}>;
export type OptionsOfBufferResponseBodyWrapped = Merge<StrictOptions, {resolveBodyOnly: false; responseType?: 'buffer'}>;
export type OptionsOfUnknownResponseBody = StrictOptions;
export type OptionsOfUnknownResponseBodyOnly = Merge<StrictOptions, {resolveBodyOnly: true}>;
export type OptionsOfUnknownResponseBodyWrapped = Merge<StrictOptions, {resolveBodyOnly: false}>;
type DefaultResponseBodyType<U extends ExtendOptions> =
type GotResponseResult<U extends ExtendOptions, BodyType> = U['resolveBodyOnly'] extends true
export type GotRequestFunction<U extends ExtendOptions = Record<string, unknown>> = {
export type HTTPAlias =
type GotStreamFunction =
export type GotStream = GotStreamFunction & Record<HTTPAlias, GotStreamFunction>;
export type Got<GotOptions extends ExtendOptions = ExtendOptions> = {
export type ExtractExtendOptions<T> = T extends Got<infer GotOptions>
export type MergeExtendsConfig<Value extends Array<Got | ExtendOptions>> =

---
File: documentation\examples\advanced-creation.js
Size: 3970 bytes
Lines: 164 [structural]
---
import process from 'node:process';
import crypto from 'node:crypto';
import got from '../../dist/source/index.js';
const logger = got.extend({
		(options, next) => {
const controlRedirects = got.extend({
			(options, response) => {
				const {origin} = response.request.options.url;
const limitDownloadUpload = got.extend({
		(options, next) => {
			const {downloadLimit, uploadLimit} = options.context;
			let controller;
			let {signal} = options;
			const promiseOrStream = next(options);
				promiseOrStream.on('downloadProgress', progress => {
						const error = new Error(`Exceeded the download limit of ${downloadLimit} bytes`);
				promiseOrStream.on('uploadProgress', progress => {
						const error = new Error(`Exceeded the upload limit of ${uploadLimit} bytes`);
const noUserAgent = got.extend({
const httpbin = got.extend({
const getMessageSignature = (data, secret) => crypto.createHmac('sha256', secret).update(data).digest('hex').toUpperCase();
const signRequest = got.extend({
			options => {
				const secret = options.context.secret ?? process.env.SECRET;
const merged = got.extend(
const {headers} = await merged.post('anything', {
const MEGABYTE = 1_048_576;

---
File: source\core\calculate-retry-delay.ts
Size: 1123 bytes
Lines: 42
---
import type {RetryFunction} from './options.js';

type Returns<T extends (...arguments_: any) => unknown, V> = (...arguments_: Parameters<T>) => V;

const calculateRetryDelay: Returns<RetryFunction, number> = ({
	attemptCount,
	retryOptions,
	error,
	retryAfter,
	computedValue,
}) => {
	if (error.name === 'RetryError') {
		return 1;
	}

	if (attemptCount > retryOptions.limit) {
		return 0;
	}

	const hasMethod = retryOptions.methods.includes(error.options.method);
	const hasErrorCode = retryOptions.errorCodes.includes(error.code);
	const hasStatusCode = error.response && retryOptions.statusCodes.includes(error.response.statusCode);
	if (!hasMethod || (!hasErrorCode && !hasStatusCode)) {
		return 0;
	}

	if (error.response) {
		if (retryAfter) {
			// In this case `computedValue` is `options.request.timeout`
			return retryAfter > computedValue ? 0 : retryAfter;
		}

		if (error.response.statusCode === 413) {
			return 0;
		}
	}

	const noise = Math.random() * retryOptions.noise;
	return Math.min(((2 ** (attemptCount - 1)) * 1000), retryOptions.backoffLimit) + noise;
};

export default calculateRetryDelay;


---
File: source\core\diagnostics-channel.ts
Size: 3466 bytes
Lines: 139 [structural]
---
import {randomUUID} from 'node:crypto';
import diagnosticsChannel from 'node:diagnostics_channel';
import type {Timings} from './utils/timer.js';
import type {RequestError} from './errors.js';
const channels = {
export type RequestId = string;
export type DiagnosticRequestCreate = {
export type DiagnosticRequestStart = {
export type DiagnosticResponseStart = {
export type DiagnosticResponseEnd = {
export type DiagnosticRequestRetry = {
export type DiagnosticRequestError = {
export type DiagnosticResponseRedirect = {
export function generateRequestId(): RequestId {
const publishToChannel = (channel: diagnosticsChannel.Channel, message: unknown): void => {
export function publishRequestCreate(message: DiagnosticRequestCreate): void {
export function publishRequestStart(message: DiagnosticRequestStart): void {
export function publishResponseStart(message: DiagnosticResponseStart): void {
export function publishResponseEnd(message: DiagnosticResponseEnd): void {
export function publishRetry(message: DiagnosticRequestRetry): void {
export function publishError(message: DiagnosticRequestError): void {
export function publishRedirect(message: DiagnosticResponseRedirect): void {

---
File: source\core\errors.ts
Size: 5715 bytes
Lines: 192 [structural]
---
import is from '@sindresorhus/is';
import stripUrlAuth from './utils/strip-url-auth.js';
import type {Timings} from './utils/timer.js';
import type Options from './options.js';
import type {TimeoutError as TimedOutTimeoutError} from './timed-out.js';
import type {PlainResponse, Response} from './response.js';
import type Request from './index.js';
type Error = NodeJS.ErrnoException;
function isRequest(x: unknown): x is Request {
export class RequestError<T = unknown> extends Error {
	constructor(message: string, error: Partial<Error & {code?: string}>, self: Request | Options) {
			const indexOfMessage = this.stack.indexOf(this.message) + this.message.length;
			const thisStackTrace = this.stack.slice(indexOfMessage).split('\n').toReversed();
			const errorStackTrace = error.stack.slice(error.stack.indexOf(error.message!) + error.message!.length).split('\n').toReversed();
export class MaxRedirectsError extends RequestError {
	constructor(request: Request) {
export class HTTPError<T = unknown> extends RequestError<T> {
	constructor(response: PlainResponse) {
export class CacheError extends RequestError {
	constructor(error: Error, request: Request) {
export class UploadError extends RequestError {
	constructor(error: Error, request: Request) {
export class TimeoutError extends RequestError {
	constructor(error: TimedOutTimeoutError, timings: Timings, request: Request) {
export class ReadError extends RequestError {
	constructor(error: Error, request: Request) {
export class RetryError extends RequestError {
	constructor(request: Request) {
export class AbortError extends RequestError {
	constructor(request: Request) {

---
File: documentation\examples\gh-got.js
Size: 1743 bytes
Lines: 78
---
import process from 'node:process';
import got from '../../dist/source/index.js';

const packageJson = {
	name: 'gh-got',
	version: '12.0.0',
};

const getRateLimit = headers => ({
	limit: Number.parseInt(headers['x-ratelimit-limit'], 10),
	remaining: Number.parseInt(headers['x-ratelimit-remaining'], 10),
	reset: new Date(Number.parseInt(headers['x-ratelimit-reset'], 10) * 1000),
});

const instance = got.extend({
	prefixUrl: 'https://api.github.com',
	headers: {
		accept: 'application/vnd.github.v3+json',
		'user-agent': `${packageJson.name}/${packageJson.version}`,
	},
	responseType: 'json',
	context: {
		token: process.env.GITHUB_TOKEN,
	},
	hooks: {
		init: [
			(raw, options) => {
				if ('token' in raw) {
					options.context.token = raw.token;
					delete raw.token;
				}
			},
		],
	},
	handlers: [
		(options, next) => {
			// Authorization
			const {token} = options.context;
			if (token && !options.headers.authorization) {
				options.headers.authorization = `token ${token}`;
			}

			// Don't touch streams
			if (options.isStream) {
				return next(options);
			}

			// Magic begins
			return (async () => {
				try {
					const response = await next(options);

					// Rate limit for the Response object
					response.rateLimit = getRateLimit(response.headers);

					return response;
				} catch (error) {
					const {response} = error;

					// Nicer errors
					if (response && response.body) {
						error.name = 'GitHubError';
						error.message = `${response.body.message} (${response.statusCode} status code)`;
					}

					// Rate limit for errors
					if (response) {
						error.rateLimit = getRateLimit(response.headers);
					}

					throw error;
				}
			})();
		},
	],
});

export default instance;


---
File: documentation\examples\h2c.js
Size: 1062 bytes
Lines: 55
---
import http2 from 'http2-wrapper';
import got from '../../dist/source/index.js';

let sessions = {};
const getSession = ({origin}) => {
	if (sessions[origin] && !sessions[origin].destroyed) {
		return sessions[origin];
	}

	const session = http2.connect(origin);
	session.once('error', () => {
		delete sessions[origin];
	});

	sessions[origin] = session;

	return session;
};

const closeSessions = () => {
	for (const key in sessions) {
		if (!Object.hasOwn(sessions, key)) {
			continue;
		}

		sessions[key].close();
	}

	sessions = {};
};

const instance = got.extend({
	hooks: {
		beforeRequest: [
			options => {
				options.h2session = getSession(options.url);
				options.http2 = true;
				options.request = http2.request;
			},
		],
	},
});

const server = http2.createServer((request, response) => {
	response.end('{}');
});

server.listen(async () => {
	const url = `http://localhost:${server.address().port}`;
	const {body, headers} = await instance(url, {context: {h2c: true}});
	console.log(headers, body);

	closeSessions();
	server.close();
});


---
File: documentation\examples\pagination.js
Size: 1691 bytes
Lines: 57
---
import Bourne from '@hapi/bourne';
import got from '../../dist/source/index.js';

const max = Date.now() - (1000 * 86_400 * 7);

const iterator = got.paginate('https://api.github.com/repos/sindresorhus/got/commits', {
	pagination: {
		paginate({response, currentItems}) {
			// If there are no more data, finish.
			if (currentItems.length === 0) {
				return false;
			}

			// Get the current page number.
			const {searchParams} = response.request.options;
			const previousPage = Number(searchParams.get('page') ?? 1);

			// Update the page number by one.
			return {
				searchParams: {
					page: previousPage + 1,
				},
			};
		},
		// Using `Bourne` to prevent prototype pollution.
		transform: response => Bourne.parse(response.body),
		filter({item}) {
			// Check if the commit time exceeds our range.
			const date = new Date(item.commit.committer.date);
			const end = date.getTime() - max >= 0;

			return end;
		},
		shouldContinue({item}) {
			// Check if the commit time exceeds our range.
			const date = new Date(item.commit.committer.date);
			const end = date.getTime() - max >= 0;

			return end;
		},
		// We want only 50 results.
		countLimit: 50,
		// Wait 1s before making another request to prevent API rate limiting.
		backoff: 1000,
		// It is a good practice to set an upper limit of how many requests can be made.
		// This way we can avoid infinite loops.
		requestLimit: 10,
		// In this case, we don't need to store all the items we receive.
		// They are processed immediately.
		stackAllItems: false,
	},
});

console.log('Last 50 commits from now to week ago:');
for await (const item of iterator) {
	console.log(item.commit.message.split('\n')[0]);
}


---
File: source\core\parse-link-header.ts
Size: 1314 bytes
Lines: 44
---
export default function parseLinkHeader(link: string) {
	const parsed = [];

	const items = link.split(',');

	for (const item of items) {
		// https://tools.ietf.org/html/rfc5988#section-5
		const [rawUriReference, ...rawLinkParameters] = item.split(';') as [string, ...string[]];
		const trimmedUriReference = rawUriReference.trim();

		// eslint-disable-next-line @typescript-eslint/prefer-string-starts-ends-with
		if (trimmedUriReference[0] !== '<' || trimmedUriReference.at(-1) !== '>') {
			throw new Error(`Invalid format of the Link header reference: ${trimmedUriReference}`);
		}

		const reference = trimmedUriReference.slice(1, -1);
		const parameters: Record<string, string> = {};

		if (rawLinkParameters.length === 0) {
			throw new Error(`Unexpected end of Link header parameters: ${rawLinkParameters.join(';')}`);
		}

		for (const rawParameter of rawLinkParameters) {
			const trimmedRawParameter = rawParameter.trim();
			const center = trimmedRawParameter.indexOf('=');

			if (center === -1) {
				throw new Error(`Failed to parse Link header: ${link}`);
			}

			const name = trimmedRawParameter.slice(0, center).trim();
			const value = trimmedRawParameter.slice(center + 1).trim();

			parameters[name] = value;
		}

		parsed.push({
			reference,
			parameters,
		});
	}

	return parsed;
}


---
File: source\core\response.ts
Size: 5457 bytes
Lines: 191 [structural]
---
import {Buffer} from 'node:buffer';
import type {IncomingMessageWithTimings, Timings} from './utils/timer.js';
import {RequestError} from './errors.js';
import stripUrlAuth from './utils/strip-url-auth.js';
import type {ParseJsonFunction, ResponseType} from './options.js';
import type Request from './index.js';
const decodedBodyCache = new WeakMap<PlainResponse, string>();
const textDecoder = new TextDecoder();
export const isUtf8Encoding = (encoding?: BufferEncoding): boolean => encoding === undefined || encoding.toLowerCase().replace('-', '') === 'utf8';
export const decodeUint8Array = (data: Uint8Array, encoding?: BufferEncoding): string => {
export type PlainResponse = {
export type Response<T = unknown> = {
export const isResponseOk = (response: PlainResponse): boolean => {
	const {statusCode} = response;
	const {followRedirect} = response.request.options;
	const shouldFollow = typeof followRedirect === 'function' ? followRedirect(response) : followRedirect;
	const limitStatusCode = shouldFollow ? 299 : 399;
export class ParseError extends RequestError {
	constructor(error: Error, response: Response) {
		const {