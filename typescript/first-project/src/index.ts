let message: string = "Hello world";
message += ". My name is Deepanshu Gulia";
console.log(message);

function add(a: number, b: number): number {
  return a + b;
}

console.log(add(2, 3));

function printConsole(a: string): void {
  console.log(a);
}

printConsole("function not returning anything use void");

class Animal {
  protected name: string;

  constructor(name: string) {
    this.name = name;
  }

  move(distance: number): void {
    console.log(`${this.name} moved ${distance}m.`);
  }
}

let cat = new Animal("cat");
cat.move(10);

class Bird extends Animal {
  fly(distance: number): void {
    console.log(`${this.name} flied ${distance}m.`);
  }
}

let crow = new Bird("crow");
crow.fly(20);
