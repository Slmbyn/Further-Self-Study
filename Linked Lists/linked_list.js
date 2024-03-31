
class Node {
    constructor(data) {
      this.data = data;
      this.next = null;
      this.previous = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    insert(data) {
        const newNode = new Node(data);
        newNode.next = null;
        newNode.previous = null;

        if (this.head === null) {
            this.head = newNode;
        } 
        
        else {
            let lastNode = this.head;
            while (lastNode.next !== null) {
                console.log("Traversing linked list...");
                lastNode = lastNode.next;
            }
            lastNode.next = newNode;
            newNode.previous = lastNode;
        }
    }

    deleteByKey(key) {
        console.log(`\nDelete Element ${key} from Linked List`);
        let currentNode = this.head;
        let previousNode = null;

        if (currentNode !== null && currentNode.data === key) {
            this.head = currentNode.next;
            console.log(`${key} found and deleted`);
            return;
        }

        while (currentNode !== null && currentNode.data !== key) {
            previousNode = currentNode;
            currentNode = currentNode.next;
        }

        if (currentNode !== null) {
            previousNode.next = currentNode.next;
            console.log(`${key} found and deleted`);
        }

        if (currentNode === null) {
            console.log(`${key} not found`);
        }
    }

    printList() {
        let currentNode = this.head;
        process.stdout.write("Linked List Elements: ");
        while (currentNode !== null) {
            process.stdout.write(`${currentNode.data} `);
            currentNode = currentNode.next;
        }
        console.log();
    }

}

const linkedList = new LinkedList();
linkedList.insert(4);
linkedList.insert(1);
linkedList.insert(3);
linkedList.insert(8);

linkedList.printList();
linkedList.deleteByKey(1);
linkedList.printList();
