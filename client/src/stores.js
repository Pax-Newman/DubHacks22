import { writable } from "svelte/store";

export const STATES = {
    home:1,
    preview:2,
    receipt:3,
}

export const state = writable(0)

export const user = writable("")