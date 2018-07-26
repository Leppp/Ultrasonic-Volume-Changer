/* eslint-disable import/unambiguous */
import { Observable, Subject, ReplaySubject, from, of, range } from 'rxjs';
import { map, filter, switchMap } from 'rxjs/operators';
//let json = require('../path/jsonfile.json');
let rxUdp = require("rx-udp");
let max = 15 // over this value the results aren't used to change the volume
let min = 5 // under this value the results aren't used to change the volume
let dgram = require('dgram');
let server = dgram.createSocket('udp4');
let exec = require('child_process').exec, child;
let observable = rxUdp.observableFromSocket(buf => buf.toString("utf8"), server);
server.bind(5000);

function change_volume(volume) {
	let vol = Math.trunc(volume);
	let cmd ='amixer -c 0 sset Master ' + vol  + '% unmute cap'; // sets the volume, change this line if you want to use it for other purposes
	exec(cmd);
	
}
observable.map((x) => JSON.parse(x)).filter((x) => x.distance < max && x.distance > min).map((x) => (x.distance - min) * (100/(max - min))).subscribe((x) => { change_volume(x) 
console.log(x)
// with the (x.distance - min) * (100/(max - min))) it changes the 5 to 15 range toa 0 to 100 range (change it for other purposes than changing the volume)
});

