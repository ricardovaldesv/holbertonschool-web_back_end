export default class Building {
  constructor(sqft) {
    if (this.constructor === Building) {
      throw new Error("Building class cannot be instantiated directly");
    }
    this._sqft = 0;
    this.sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Square footage must be a number');
    }
    this._sqft = value;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
