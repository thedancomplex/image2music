s.boot;

(
z = List.new(128);
y = List.new(128);
w = List.new(128);
v = List.new(128);

v.free;
w.free;
y.free;
z.free;

//i = Synth( \sin,[ \amp, 0.0] );
z = List.new(128);
//y = Array.new(12);
y = List.new(128);
w = List.new(128);
v = List.new(128);
s.makeBundle( nil, {
128.do(
	{
		arg i;
		var ii;
		var iis;
		var key;
		var keyHead;
		var theIndex;
		theIndex = -1;
		//i.postln;
		i.asAscii;
		ii = i.asAscii;
		ii = '/key'++i;
		iis = '\\sin'++i;
		//ii.postln;
		//iis.postln;

		j = SynthDef( iis, { | amp = 0.01, freq = 333, trig = 1, filter_center = 1000.0, filter_width=0.05 |
			var env, sig, res;
			env = EnvGen.kr( Env.asr( 0.001, 0.9, 0.001 ), trig, doneAction: 0 );
			sig = Pulse.ar( [freq], 0.4, amp ) * env;
			res = Resonz.ar(sig, filter_center, filter_width);

			//sig = LFTri.ar( [ freq, freq * 0.999 ], 0.0, amp ) * env;
			//Out.ar( [ 0 ], sig * 0.6 );
			Out.ar( [ 0 ], res * 0.6 );
		}).add;

        s.sync;

		h = Synth( iis, [ \amp, 0.0 ] );

		x = OSCFunc( { | msg, time, addr, port |
			var pyFreq;
			var theI;
			var pyAmp;
			theI = 0;
			pyFreq = msg[1].asFloat;
			pyAmp  = msg[2].asFloat;
			("OSC" + msg[0] + " freq is" + pyFreq + " filter_center = " + msg[3]).postln;
			128.do(
				{
					arg jj;
					var a1;
					var a2;
					var c;
					var c1;
					var c2;
					var cc1;
					var cc2;
					var ppp;

					a1 = w[jj].asString;
					a2 = msg[0].asString;
					c1 = a1[4].asString++a1[5].asString++a1[6].asString;
					c2 = a2[4].asString++a2[5].asString++a2[6].asString;
					cc1 = c1.asInteger;
					cc2 = c2.asInteger;

					if ( cc1==cc2,
						{theI = jj; jj.postln;},
						{ppp=0;}// "no".postln;}
					)
				}
			);
			if ( msg[1].notNil,
					{ z[theI].set( \freq, pyFreq ); },
					{}
				);
			if ( msg[2].notNil,
					{ z[theI].set( \amp, pyAmp); },
					{}
				);
			if ( msg[3].notNil,
					{ z[theI].set( \filter_center, msg[3].asFloat); "filter set".postln; },
					{}
				);
			if ( msg[4].notNil,
					{ z[theI].set( \filter_width, msg[3].asFloat); "filter width Set".postln; },
					{}
				);

						//z[theI].set( \amp, 0.4 );
		}
		, ii );


		v.add(j);
		w.add(ii);
		y.add(x);
		z.add(h);

		//v[i+1] = j;
		//w[i+1] = ii;
		//y[i+1] = x;
		//z[i+1] = h;

		w.postln;
		y.postln;
		z.postln;
		i.postln;
	}
  )
});
)

r = Recorder(s);
s.record(path: "vtx250.wav", numChannels: 2);
s.record(path: "starry_night.wav", numChannels: 2);
s.stopRecording();

1.notNil;



(
//g = Group.new;
128.do(
	{
		arg jj;
		// modulate frequency

		//{ Resonz.ar(z[jj], 8000, 0.05) }.play
		jj.postln;
	}
)
)

(
j = SynthDef( \testSin, { | amp = 0.01, freq = 333, trig = 1 |
	var env, sig;
	env = EnvGen.kr( Env.asr( 0.001, 0.9, 0.001 ), trig, doneAction: 0 );
	sig = SinOsc.ar( [freq], 0.0, amp ) * env;
	//sig = LFTri.ar( [ freq, freq * 0.999 ], 0.0, amp ) * env;
	o = Out.ar( [ 0 ], sig * 0.6 );
	}).add;

h = Synth( \testSin, [ \amp, 0.8 ] );
)

c = Bus.audio(s);
{ Resonz.ar(o, 8000, 0.05) }.play


s.sync;


z[127].postln;
y[127].postln;
w[127].postln;


this.clearAll;

