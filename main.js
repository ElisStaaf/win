var Airplane = function() {
    this.ready = false
    this.completed = false
    makeReady = function() {
        this.ready = true
    }
    land = function() {
        tower = Tower
        if (tower._ready == true) {
            this.completed = true
            console.log("Success")
        }
    }
}

var Airway = function() {
    this.clear = false
    this.connected = false
    clearRunway = function() {
        this.clear = true
    }
    var connectToTower = function() {
        if (this.clear == true) {
            this.connected = true
        } else {
            console.log("Couldn't connect.")
        }
    }
}

var Tower = function() {
    this.signal = false
    this._ready = false
    var takeConnection = function() {
        road = Airway
        if (road.connected == true) {
            this.signal = true
        }
    var makeConnection = function() {
        this._ready = true
    }
    }
}

airplane = Airplane
airway = Airway
tower = Tower
airplane.makeReady
airway.clearRunway
airway.connectToTower
tower.takeConnection
tower.makeConnection
airplane.land