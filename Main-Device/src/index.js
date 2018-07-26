/* eslint-disable import/unambiguous */
import { Observable, Subject, ReplaySubject, from, of, range } from 'rxjs';
import { map, filter, switchMap } from 'rxjs/operators';
//let json = require('../path/jsonfile.json');
let rxUdp = require("rx-udp");
let max = 15
let min = 5
let dgram = require('dgram');
let server = dgram.createSocket('udp4');
let exec = require('child_process').exec, child;
let observable = rxUdp.observableFromSocket(buf => buf.toString("utf8"), server);
server.bind(5000);

function change_volume(volume) {
	let vol = Math.trunc(volume);
	let cmd ='amixer -c 0 sset Master ' + vol  + '% unmute cap';
	exec(cmd);
	
}
observable.map((x) => JSON.parse(x)).filter((x) => x.distance < max && x.distance > min).map((x) => (x.distance - min) * (100/(max - min))).subscribe((x) => { change_volume(x) 
console.log(x)
});

