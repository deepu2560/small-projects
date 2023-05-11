// constructor
// super()

// private property
// public property

// private method
// public method

// static property
// static method

// get and set

class Hero {
  public title: string = "Batman";
  private _firstname: string = "Bruce";
  private _lastname: string = "Wayne";
  static version: number = 1001;
  //--------------------------------------
  constructor(ntitle: string) {
    this.title = ntitle;
  }
  //--------------------------------------
  get firstname() {
    return this._firstname;
  }
  set firstname(nfirstname: string) {
    this._firstname = nfirstname;
  }
  get lastname() {
    return this._lastname;
  }
  set lastname(nlastname: string) {
    this._lastname = nlastname;
  }
}
