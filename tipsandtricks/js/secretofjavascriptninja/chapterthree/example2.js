// Storing a collection of unique functions
var store = {
    nextId: 1,
    cache: {},
    add: function (fn) {
        if (!fn.id) {
            fn.id = this.nextId++;
            this.cache[fn.id] = fn;
            return true;
        }
    }
};

function ninja() {
}

console.assert(store.add(ninja), "Function was safely added.");
console.assert(!store.add(ninja), "But it was only added once.");
