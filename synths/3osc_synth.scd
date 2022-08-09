s.boot;
s.options.numOutputBusChannels = 2;


(
z = List.new(3);
y = List.new(3);
z.free;
y.free;
z = List.new(3);
y = List.new(3);

s.makeBundle(nil,
	{
		3.do(
			{
				arg i;

				var theName;
				theName = '/osc'++i;
				j = SynthDef(theName, {
					|         amp = 0.5,           freq = 440,         trig = 1,
					sin_freq      = 440.0,      sin_amp = 0.0,    sin_phase = 0.0,
					filter_center = 440.0, filter_width = 0.05,
					lfo0_freq     =   1.0,     lfo0_amp = 1.0,   lfo0_phase = 0.0,
					lfo1_freq     =   1.0,     lfo1_amp = 1.0,   lfo1_phase = 0.0,
					saw_freq      = 440.0,      saw_amp = 0.0,
					square_freq   = 440.0,   square_amp = 0.0, square_width = 0.5,
					tri_freq      = 440.0,   tri_amp    = 0.0,    tri_phase = 0.0 |

					var env, sin, sig, sigL, sigR, tri, squ, saw, res, lfo0, lfo1, fin;
					env = EnvGen.kr(Env.asr(attackTime: 0.01, sustainLevel: 1.0, releaseTime: 1.0, curve: -4.0), gate: trig, doneAction: 0);
					lfo0 = SinOsc.ar(freq: lfo0_freq, phase: lfo0_phase, mul: lfo0_amp, add: 0.0);
					lfo1 = SinOsc.ar(freq: lfo1_freq, phase: lfo1_phase, mul: lfo1_amp, add: 0.0);
					//amp  = amp * lfo0;

					saw  = Saw.ar(   freq: saw_freq,    mul:    saw_amp,      add: 0.0);
					squ  = Pulse.ar( freq: square_freq, width:  square_width, mul: square_amp, add:saw);
					tri  = LFTri.ar( freq: tri_freq,    iphase: tri_phase,    mul: tri_amp,    add: squ);
					sin  = SinOsc.ar(freq: sin_freq,    phase:  sin_phase,    mul: sin_amp,        add: tri) * env;
					sig  = sin * amp;

					res  = Resonz.ar(in: sig, freq: filter_center, bwr: filter_width, mul: 1.0, add: 0.0);
					sigL = sin * amp * (lfo0_amp+lfo0);
					sigR = sin * amp * (lfo0_amp-lfo0);
					//scope([sigL, sigR]);
					fin = { [ sigL, sigR ] };


					Out.ar({[0]},fin);
					}
				).add;
				s.sync;
				h = Synth(theName, [ \amp, 0.1 ] );
				z.add(h);
				y.add(j);
			}
		)
	}
)

)

z.postln;
z[0].set(\sin_amp, 0.0);
z[1].set(\sin_amp, 0.0);
z[2].set(\sin_amp, 0.0);

(
z[0].set(\lfo0_freq, 0.2);
z[0].set(\lfo1_freq, 1.0);
z[0].set(\lfo1_phase, pi);
z[0].set(\lfo0_amp,0.5);
z[0].set(\saw_amp, 0.0);
z[0].set(\sin_amp, 10.0);
)

(
z[0].set(\lfo0_freq, 0.2);
z[0].set(\lfo1_freq, 1.0);
z[0].set(\lfo1_phase, pi);
z[0].set(\lfo0_amp,0.5);
z[0].set(\saw_amp, 0.0);
z[0].set(\sin_amp, 10.0);

z[1].set(\lfo0_freq, 0.2);
z[1].set(\lfo1_freq, 1.0);
z[1].set(\lfo1_phase, 0.0);
z[1].set(\lfo0_amp,0.5);
z[1].set(\saw_amp, 0.8);
z[1].set(\sin_amp, 10.0);
)


z[1].set(\saw_amp, 1.5);
z[0].set(\sin_amp, 1.0);
z[0].set(\sin_freq, 445);

{ [SinOsc.ar(440, 0, 0.2), SinOsc.ar(442, 0, 0.1)] }.play;
s.scope;

s.scope;

