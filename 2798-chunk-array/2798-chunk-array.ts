type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    return arr.reduce((ans: Obj[][], _, idx: number) => {
        if (idx % size === 0) ans.push(arr.slice(idx, idx + size));
        return ans;
    }, [])
};
