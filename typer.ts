/*
~ Typer Module - Made by Elis Stääf:
~ Welcome! This is the typer module!
~ A powerful module for TypeScript
~ that adds more types. Also, if
~ you didn't know, you can import
~ modules by using:
~ import * as $ from "./typer.ts"
~ So... Yeah, enjoy!
*/

//~ @ts-check

//& Simple types
export type int = number
export type str = string
export type err = never
export type tribool = boolean|null
export type Lost = null
export type Data = Record<string, any>
export type Fn = (...args: any[]) => any 
export type PromiseFn<T> = (...args: any[]) => Promise<T>
export type Arr<T> = T[]
export type Vec2 = [number, number]
export type Vec3 = [number, number, number]
export type Vec4 = [number, number, number, number]
export type Vec5 = [number, number, number, number, number]
export type Vec6 = [number, number, number, number, number, number]
export type Vec7 = [number, number, number, number, number, number, number]

//& Complex types
export type Construct<T> = {
    value: T
    }
export type Tree<T> = {
    value: T;

    left?: Tree<T>;
    right?: Tree<T>;
    }
export type Maybe<T> = T|null
export type Nullable<T> = T|undefined
export type Option<T> = T|null|undefined
export type Eslift<T> = T|never
export type Ctor<T> = new (...args: any[]) => T
export type Fun<T> = (...args: any[]) => T
export type AsyncFun<T> = (...args: any[]) => Promise<T>
export type Key<T> =  keyof T extends string ? T : never
export type Union<T> = {  [K in keyof T]: T[K]  }
export type Tuple<T> = [T,...T[]]
export type Partial<T> = {  [K in keyof T]?: T[K]|undefined  }
export type Required<T> = {  [K in keyof T]-? : T[K]  }
export type DeepPartial<T> = {  [K in keyof T]?: DeepPartial<T[K]>}
export type Mutable<T> = {  -readonly [K in keyof T] : T[K]  }
export type ReadOnly<T> = {  readonly [K in keyof T] : T[K]  }

//& Union Types
export type UnionOf<T extends any[]> = T[number]
export type SupersetOf<T, U> = T extends U ? T : never
export type Overlapping<T, U> = T extends U ? U : never
export type DisjointUnion<T, U> = T extends U ? never : T|U
export type UnionToIntersection<T> = (T extends any ? (k: T) => void : never) extends ((k: infer I) => void)? I : never
export type UnionToUnion<T> = T extends any ? T : never
export type UnionToTuple<T> = T extends any ? [T] : never
export type UnionToKeys<T> = T extends any? (k: T) => void : never extends T ? never : keyof T


