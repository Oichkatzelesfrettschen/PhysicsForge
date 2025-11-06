model, while the I Ching shows its Clifford algebra
structurefl Š but don't be fooled; his mathematics is solid. When it comes to the physics,
I'm not sure I buy his theory of everything, but that's not unusual: I don't think I buy
anyone's
theory of everything!
Let me wrap up by passing on something he told me about triality and the exceptional
groups. In
 fiWeek 90fl
 I described how you could get the Lie groups
G
2
,
F
4
and
E
8
from
triality. I didn't know how
E
6
and
E
7
t into the picture. He emailed me, saying:
flHere is a nice way: Start with
D
4
= Spin(8)
:
28 = 28 + 0 + 0 + 0 + 0 + 0 + 0
Add spinors and vector to get
F
4
:
52 = 28 + 8 + 8 + 8 + 0 + 0 + 0
Now, ficomplexifyfl the
8 + 8 + 8
part of
F
4
to get
E
6
:
78 = 28 + 16 + 16 + 16 + 1 + 0 + 1
Then, fiquaternionifyfl the
8 + 8 + 8
part of
F
4
to get
E
7
:
133 = 28 + 32 + 32 + 32 + 3 + 3 + 3
Finally, fioctonionifyfl the
8 + 8 + 8
part of
F
4
to get
E
8
:
248 = 28 + 64 + 64 + 64 + 7 + 14 + 7
This way shows you that the fisecondfl
Spin(8)
in
E
8
breaks down as
28 =
7 + 14 + 7
which is globally like two 7-spheres and a
G
2
, one
S
7
for left-action,
one for right-action, and a
G
2
automorphism group of octonions that is needed
to for ficompatibilityfl of the two
S
7
s. The
3 + 3 + 3
of
E
7
, the
1 + 0 + 1
of
E
6
, and
the
0 + 0 + 0
of
F
4
and
D
4
are the quaternionic, complex, and real analogues
of the
7 + 14 + 7
.fl
When I asked him where he got this, he said he cooked it up himself using the
construction of
E
8
that I learned from Kostant together with the FreudenthalŒTits magic
square. He gave some references for the latter:
4)
 Hans Freudenthal, fiLie groups in the foundations of geometryfl,
Adv. Math.
1
(1964) 145Œ190.
5)
 Jacques Tits, fiAlg
´
ebres alternatives, alg
´
ebres de Jordan et alg
´
ebres de Lie excep-
tionnelles. I. Constructionfl
Indag. Math.
28
(1966), 223Œ237.
218
 WEEK 91 OCTOBER 6, 1996
6)
 Kevin McCrimmon, fiJordan algebras and their applicationsfl,
Bull. Amer. Math. Soc.
84
(1978), 612Œ627, at pp. 620Œ621. Available at
https://projecteuclid.org/
journals/bulletin-of-the-american-mathematical-society/volume-84/
issue-4/Jordan-algebras-and-their-applications/bams/1183540925.full
I would describe it here, but I'm running out of steam, and it's easy to learn about it from
Tony Smith's web page:
7)
 Tony Smith, FreudenthalŒTits magic square,
https://web.archive.org/web/
20110808093537/http://valdostamuseum.org/hamsmith/FTsquare.html
fiI regret that it has been necessary for me in this lecture to administer such
a large dose of four-dimensional geometry. I do not apologise, because I am
not really responsible for the fact that nature in its most fundamental aspect
is four-dimensional.fl
Š Albert North Whitehead.
219
 WEEK 92 OCTOBER 17, 1996
Week 92
October 17, 1996
I'm sure most of you have lost interest in my fiTale of
n
-Categoriesfl, because it takes a
fair amount of work to keep up with all the abstract concepts involved. However, we are
now at a point where we can have some fun with what we've got, even if you haven't
really followed all the previous stuff. So what follows is a rambling tour through monads,
adjunctions, the 4-color theorem and the large-N limit of
SU(
N
)
gauge theory. . . .
Okay, so in
 fiWeek 89fl
 we dened a gadget called a fimonadfl. Using the string dia-
grams we talked about, you can think of a monad as involving a process like this:
s
s

M
s
which we read downwards as describing the fifusionfl of two copies of something called
s
into one copy of the same thing
s
. The fusion process itself is called
M
.
I can hear you wonder, what exactly
is
this thing s? What
is
this process
M
? Well,
I gave the technical answer in
 fiWeek 89fl
 Š but the point is that
n
-category theory is
deliberately designed to be so general that it covers pretty much anything you could
want! For example,
s
could be the set of real numbers and
M
could be multiplication
of real numbers, which is a function from
s

s
to
s
. Or we could be doing topology
in the plane, in which case the picture above stands for exactly what it looks like: two
lines merging to form one line! These and many other situations are analogous, and the
formalism allows us to treat them all at once. Here I will not review all the rules of the
game. If you just play along and trust me everything will be all right. If you don't trust
me, go back and check the denitions.
Let me turn to the axioms for a monad. In addition to the multiplication
M
we want
to have a fimultiplicative identityfl,
I
, looking like this:
I
s
Here nothing is coming in, and a copy of
s
is going out. Because ordinary multiplication
has
1
x
=
x
and
x
1 =
x
for all
x
, we want the following axioms to hold:
I
s

M
s
=
s
220
 WEEK 92 OCTOBER 17, 1996
and
I
s

M
s
=
s
Also, since ordinary multiplication has
(
xy
)
z
=
x
(
y z
)
, we want the following associativ-
ity law to hold, too:
s
s
s

M

M
s
s
=
s
s
s

M

M
s
s
These rules are a translation of the rules given in
 fiWeek 89fl
 into string diagram form.
If you are a physicist, you can think of these diagrams as being funny Feynman di-
agrams where you've got some kind of particle
s
and two processes
M
and
I
. Then
M
is a bit like what you'd call a ficubic self-interactionfl, where two particles combine to
form a third. These interactions sh ow up in simple textbook theories like the fi
'
3
theoryfl
and, more importantly, in nonabelian gauge eld theories like quantum chromodynam-
ics, where the gauge bosons have cubic self-interactions. On the other hand,
I
is a bit
like what you'd usually call a fisourcefl or an fiexternal potentialfl, some sort of eld im-
posed from outside that can create particles of type
s
. You shouldn't take the analogy
with Feynman diagrams too seriously yet, because the context we're working in is so
general, and the most interesting physics theories don't correspond to monads but to
more elaborate setups. However, we could esh out the analogy to make it very precise
and accurate if we wanted, and this is especially important in topological quantum eld
theory. More later about that.
Now in
 fiWeek 83fl
 I discussed a different sort of gadget, called an fiadjunctionfl. Here
you have two guys
x
and
x

, and two processes
U
and
C
called the fiunitfl and ficounitfl,
which look like this:
x
x


U
and
x

x

C
221
 WEEK 92 OCTOBER 17, 1996
They satisfy the following axioms:
x
x
x


U

C
=
x
x

x

x

U

C
=
x

Physically, we can think of
x

as the antiparticle of
x
, and then
U
is the process of creation
of a particle-antiparticle pair, while
C
is the process of annihilation. The axioms just say
that for a particle or antiparticle to fidouble back in timefl by means of these processes
isn't really different than for it to march obediently along forwards. Mathematically,
one nice example of an adjunction involves a vector space
x
and its dual vector space
x

. This is really the same example, since if the behavior of a particle under symmetry
transformations is described by some group representation, its antiparticle is described
by the dual representation. For more details on the math, see
 fiWeek 83fl
.
Now, let's see how to get a monad from an adjunction! We need to get
s
,
M
, and
I
from
x
,
x

,
U
, and
C
. To do this, we rst dene
s
to be
xx

. Then dene
M
to be
x

x

C
x
x

x
x

Again, to really understand the rules of the game you need to learn a bit about string
diagrams and
2
-categories, but the basic idea is supposed to be simple: we can get two
xx

's to turn into one
xx

by letting an
x

and
x
annihilate each other!
Finally, we dene
I
to be
x
x


U
In other words, an
xx

can be created out of nothing since it's a fiparticle/antiparticle
pairfl.
Now one can check that all the axioms for a monad hold. You really need to know
a bit about
2
-categories to do it carefully, but basically you just let yourself deform the
222
 WEEK 92 OCTOBER 17, 1996
pictures, in part with the help of the axioms for an adjunction, which let you straighten
out curves that fidouble back in time.fl So for example, we can prove the identity law
x
x


U
x

C
x
x

x

=
x
x

by canceling the
U
and the
C
on the left using one of the axioms for an adjunction.
Similarly, associativity holds because the following two pictures are topologically the
same:
x

x

C
x
x

x
x

x

x

C
x
x

x
x

x
x

x
x

=
x
x


C
x

x
x

x
x
x


C
x

x
x

x
x

x
x

x
Whew! Drawing these is tough work.
Now, as I said, an example of an adjunction is a vector space
x
and its dual
x

. What
monad do we get in this case? Well, the vector space
x
tensored with
x

is just the vector
space of linear transformations of
x
, so that's our monad in this case. In less high-brow
terms, we've proven that matrices form an algebra when you dene matrix multiplication
in the usual way! In particular, the above picture serves as a diagrammatic proof that
matrix multiplication is associative.
Of course, people didn't invent all this fancy-looking (but actually very basic) stuff
just to deal with matrix multiplication! Or did they? Well, actually, Penrose
did
invent a
diagrammatic notation for tensors which is just a slightly souped-up version of the above
stuff. You can nd it in:
1)
 fiApplications of negative dimensional tensorsfl, by Roger Penrose, in
Combinatorial
Mathematics and its Applications
, ed. D. J. A. Welsh, Academic Press, 1971.
223
 WEEK 92 OCTOBER 17, 1996
But most of the work on this sort of thing has been aimed at applications of other
sorts.
Now let me drift over to a related subject, the large-
N
limit of
SU(
N
)
gauge theory.
Quantum chromodynamics, or QCD, is an
SU(
N
)
gauge theory with
N
= 3
, but it turns
out that things simplify a lot in the limit as
N
! 1
, and one gets some nice qualitative
insight into the strong force by considering this simplied theory. One can even treat the
number
3
as a small perturbation around the number
1
and get some decent answers!
A good introduction to this appears in Coleman's delightful book, essential reading for
anyone learning particle physics:
2)
 Sidney Coleman,
Aspects of Symmetry
, Cambridge U. Press, Cambridge, 1989.
Check out section 8.3.1, entitled fithe double line representation and the dominance of
planar graphsfl. Coleman considers YangŒMills theories, like QCD, but many of the same
ideas apply to other gauge theories.
The idea is that if we start out studying the Feynman diagrams for a gauge eld theory
with gauge group
SU(
N
)
, and see how much various diagrams contribute to any process
for large
N
, the diagrams that contribute the most are those that can be drawn on a
plane without any lines crossing. Technically, the reason is that diagrams that can only
be drawn on a surface of genus
g
grow like
N
2

2
g
is
called the Euler characteristic and it's biggest when your surface has no handles.
Even better, in the
N
! 1
limit we can think of the Feynman diagrams using di-
agrams like the ones above. For example, we can think of the cubic self-interaction in
YangŒMills theory as simply matrix multiplication:
x


C
x
x
x
x

x

and the quartic self-interaction as something a wee bit fancier:
x


C
x
x
x
x

x

x


U
x
Apparently these ideas have spawned a whole eld of physics called fimatrix modelsfl.
These ideas work not only for YangŒMills theory but also for ChernŒSimons theory,
which is a topological quantum eld theory: a theory that doesn't require any metric on
224
 WEEK 92 OCTOBER 17, 1996
spacetime to make sense. Here they have been exploited by Dror Bar-Natan to come up
with a new formulation of the famous 4-color theorem:
3)
 Dror Bar-Natan, fiLie algebras and the four color theoremfl, available as
q-alg/
9606016
.
As I explained in
 fiWeek 8fl
 and
 fiWeek 22fl
, there is a way to formulate the 4-color
theorem as a statement about trivalent graphs. In particular, Penrose invented a little
recipe that lets us calculate an invariant of trivalent graphs, which is zero for some
planar
graph only if some corresponding map can't be 4-colored. This recipe involves
the vector cross product, or equivalently, the Lie algebra of the group
SU(2)
. You can
generalize it to work for
SU(
N
)
. And if you then consider the
N
! 1
limit, you get the
above stuff! (The point is that the above stuff also gives a rule for computing a number
from any trivalent graph.)
Now as I said, in the
N
! 1
limit all the nonplanar Feynman diagrams give negligi-
ble results compared to the planar ones. So another way to state the 4-color theorem is
this: if the
SU(2)
invariant of a trivalent graph is zero, the
SU(
N
)
invariant is negligible
in the
N
! 1
limit.
This doesn't yet give a new proof of the 4-color theorem. But it makes it into sort of
a
physics
problem: a problem about the relation of
SU(2)
ChernŒSimons theory and the
N
! 1
limit of ChernŒSimons theory.
Now, the 4-color theorem is one of the two deep mysteries of 2-dimensional topol-
ogy Š a subject too often considered trivial. The other mystery is the AndrewsŒCurtis
conjecture, discussed in
 fiWeek 23fl
. Often a problem is hard or unsolvable until you get
the right tools. Topological quantum eld theory is a new tool in topology, so one could
hope it'll shed some light on these problems. Bar-Natan's paper is a tantalizing piece of
evidence that maybe, just maybe, it will.
One can't really tell yet.
Anyway, I don't really care much about the 4-color theorem per se. If I ever need
to color a map I'll hire a cartographer. It's the connections between seemingly disparate
subjects that I nd interesting.
2
-categories are a very abstract formalism developed to
describe
2
-dimensional ways of glomming things together. Starting from the study of
2
-categories, we very naturally get the notions of fimonadfl and fiadjunctionfl. And before
we know it, this leads us to some interesting questions about
2
-dimensional quantum
eld theory: for really, the dominance of planar diagrams in the
N
! 1
limit of gauge
theory is saying that in this limit the theory becomes essentially a 2-dimensional eld
theory, in some funny sense. And then, lo and behold, this turns out to be related to the
4-color theorem!
By the way, I guess you all know that the 4-color theorem was proved using a com-
puter, by breaking things down into lots of separate cases. (See
 fiWeek 22fl
 for refer-
ences.) Well, there's a new proof out, which also uses a computer, but is supposed to be
simpler:
4)
 Neil Robertson, Daniel P. Sanders, Paul Seymour, and Robin Thomas, fiA new
proof of the four-colour theoremfl,
Electronic Research Announcements of the Amer-
ican Mathematical Society
2
(1996), 17Œ25. Available at
http://www.ams.org/
journals/
 journals/era/1996-02-01/
.
225
 WEEK 92 OCTOBER 17, 1996
I'm still hoping for the 2-page fiphysicist's proof fl using path integrals!
To continue reading the fiTale of
n
-Categoriesfl, see
 fiWeek 99fl
. For more on adjunc-
tions and monoid objects, try fiWeek173fl and especially fiWeek 174fl.
226
 WEEK 93 OCTOBER 27, 1996
Week 93
October 27, 1996
Lately I've been trying to learn more about string theory. I've always had grave doubts
about string theory, but it seems worth knowing about. As usual, when I'm trying to
learn something I nd it helpful to write about it Š it helps me remember stuff, and it
points out gaps in my understanding. So I'll start trying to explain some string theory in
this and forthcoming Week's Finds.
However: watch out! This isn't going to be a systematic introduction to the subject.
First of all, I don't know enough to do that. Secondly, it will be very quirky and id-
iosyncratic, because the aspects of string theory I'm interested in now aren't necessarily
the ones most string theorists would consider central. I've been taking as my theme of
departure, fiWhat's so great about 10 and 26 dimensions?fl When one reads about string
theory, one often hears that it only works in 10 or 26 dimensions Š and the obvious
question is, why?
This question leads one down strange roads, and one runs into lots of surprising coin-
cidences, and spooky things that sound like coindences but might NOT be coincidences
if we understood them better.
For example, when we have a string in 26 dimensions we can think of it as wig-
gling around in the 24 directions perpendicular to the 2-dimensional surface the string
traces out in spacetime (the fistring worldsheetfl). So the number 24 plays an especially
important role in 26-dimensional string theory. It turns out that
1
2
+ 2
2
+ 3
2
+
  
+ 24
2
= 70
2
:
In fact, 24 is the
only
integer
n >
1
such that the sum of squares from
1
2
to
n
2
is itself a
perfect square. Is this a coincidence? Probably not, as I'll eventually explain! This is just
one of many eerie facts one meets when trying to understand this stuff.
For starters I just want to explain why dimensions of the form
8
k
+ 2
are special.
Notice that if we take
k
= 0
here we get
2
, the dimension of the string worldsheet. For
k
= 1
we get
10
, the dimension of spacetime in fisupersymmetric string theoryfl. For
k
= 3
we get
26
, the dimension of spacetime in fipurely bosonic string theoryfl. So these
dimensions are important. What about
k
= 2
and the dimension
18
, I hear you ask?
Well, I don't know what happens there yet... maybe someone can tell me! All I want to
do now is to explain what's good about
8
k
+ 2
.
But I need to start by saying a bit about fermions.
Remember that in the Standard Model of particle physics Š the model that all fancier
theories are trying to outdo Š elementary particles come in 3 basic kinds. There are the
basic fermions. In general a fifermionfl is a particle whose angular momentum comes in
units of Planck's constant
~
times
1
=
2
,
3
=
2
,
5
=
2
, and so on. Fermions satisfy the Pauli
exclusion principle Š you can't put two identical fermions in the same state. That's why
we have chemistry: the electrons stack up in fishellsfl at different energy levels, instead of
all going to the lowest-energy state, because they are fermions and satisfy the exclusion
principle. In the Standard Model the fermions go like this:
227
 WEEK 93 OCTOBER 27, 1996
L eptons Quarks
electron electron neutrino down quark up quark
muon muon neutrino strange quark charm quark
tauon tauon neutrino bottom quark top quark
There are three figenerationsfl here, all rather similar to each other.
There are also particles in the Standard Model called fibosonsfl having angular mo-
mentum in units of
~
times
0
,
1
,
2
, and so on. Identical bosons, far from satisfying the
exclusion principle, sort of like to all get into the same state: one sees this in phenomena
such as lasers, where lots of photons occupy the same few states. Most of the bosons in
the Standard Model are called figauge bosonsfl. These carry the different forces in the
standard model, by which the particles interact:
Electromagnetic force Weak force Strong force
photon W
+
, W

, Z 8 gluons
Finally, there is also a bizarre particle in the Standard Model called the fiHiggs bosonfl.
This was rst introduced as a rather ad hoc hypothesis: it's supposed to interact with the
forces in such a way as to break the symmetry that would otherwise be present between
the electromagnetic force and the weak force. It has not yet been observed; nding
it would would represent a great triumph for the Standard Model, while
not
nding it
might point the way to better theories.
Indeed, while the Standard Model has passed many stringent experimental tests, and
successfully predicted the existence of many particles which were later observed (like
the W, the Z, and the charm and top quarks), it is a most puzzling sort of hodgepodge.
Could nature really be this baroque at its most fundamental level? Few people seem to
think so; most hope for some deeper, simpler theory.
It's easy to want a fideeper, simpler theoryfl, but how to get it? What are the clues?
What can we do? Experimentalists certainly have their work cut out for them. They can
try to nd or rule out the Higgs. They can also try to see if neutrinos, assumed to be
massless in the Standard Model, actually have a small mass Š for while the Standard
Model could easily be patched if this were the case, it would shed interesting light on one
of the biggest mysteries in physics, namely why the fermions in nature seem not to be
symmetric under reection, or fiparityfl. Right now, we believe that neutrinos only exist
in a left-handed form, rotating one way but not the other around the axis they move
along. This is intimately related to their apparent masslessness. In fact, for reasons that
would take a while to explain, the lack of parity symmetry in the Standard Model forces
us to assume all the observed fermions acquire their mass only through interaction with
the Higgs particle! For more on the neutrino mass puzzle, try:
1)
 Paul Langacker, Implications of Neutrino Mass,
https://www.physics.upenn.edu/
˘
pgl/neutrino/jhu/jhu.html
And, of course, experimentalists can continue to do what they always do best: discover
the utterly unexpected.
228
 WEEK 93 OCTOBER 27, 1996
Theorists, on the other hand, have been spending the last couple of decades poring
over the standard model and trying to understand what it's telling us. It's so full of sug-
gestive patterns and partial symmetries! First, why are there 3 forces here? Each force
goes along with a group of symmetries called a figauge groupfl, and electromagnetism
corresponds to
U(1)
, while the weak force corresponds to
SU(2)
and the strong force
corresponds to
SU(3)
. (Here
U(
n
)
is the group of
n

n
unitary complex matrices, while
SU(
n
)
is the subgroup consisting of those with determinant equal to
1
.) Well, actually
the Standard Model partially unies the electromagnetic and weak force into the fielec-
troweak forcefl, and then resorts to the Higgs to explain why these forces are so different
in practice. Various figrand unied theoriesfl or fiGUTsfl try to unify the forces further by
sticking the group
SU(3)

SU(2)

U(1)
into a bigger group Š but then resort to still
more Higgses to break the symmetry between them!
Then, there is the curious parallel between the leptons and quarks in each generation.
Each generation has a lepton with mass, a massless or almost massless neutrino, and
two quarks. The massive lepton has charge

1
=
3
, and the fiupfl type quark has charge
2
=
3
. Funny pattern, eh? The Standard Model does not really explain this, although
it would be ruined by fianomaliesfl Š certain nightmarish problems th at can beset a
quantum eld theory Š if one idly tried to mess with the generations by leaving out a
quark or the like. It's natural to try to fiunifyfl the quarks and leptons, and indeed, in
grand unied theories like the
SU(5)
theory proposed in 1974 of Georgi and Glashow,
the quarks and leptons are treated in a unied way.
Another interesting pattern is the repetition of generations itself. Why is there more
than one? Why are there three, almost the same, but with the masses increasing dramat-
ically as we go up? The Standard Model makes no attempt to explain this, although it
does suggest that there had better not be more than 17 quarks Š more, and the strong
force would not be fiasymptotically freefl (weak at high energies), which would cause
lots of problems for the theory. In fact, experiments strongly suggest that there are no
more than 3 generations. Why?
Finally, there is the grand distinction between bosons and fermions. What does this
mean? Here we understand quite a bit from basic principles. For example, the fispin-
statistics theoremfl explains why particles with half-integer spin should satisfy the Pauli
exclusion principle, while those with integer spin should like to hang out together. This
is a very beautiful result with a deep connection to topology, which I try to explain here:
2)
 John Baez, Spin, statistics, CPT and all that jazz,
http://math.ucr.edu/home/
baez/spin.stat.html
But many people have tried to bridge the chasm between bosons and fermions, unifying
them by a principle called fisupersymmetryfl. As in the other cases mentioned above,
when they do this, they then need to pull tricks to fibreakfl the symmetry to get a theory
that ts the experimental fact that bosons and fermions are very different. Personally, I'm
suspicious of all these symmetries postulated only to be cleverly broken; this approach
was so successful in dealing with the electroweak force Š modulo the missing Higgs!
Š that it seems to have been accepted as a universal method of having ones cake and
eating it too.
Now, string theory comes in two basic avors. Purely bosonic string theory lives in 26
dimensions and doesn't have any fermions in it. Supersymmetric string theories live in
229
 WEEK 93 OCTOBER 27, 1996
10 dimensions and have both bosons and fermions, unied via supersymmetry. To deal
with the fermions in nature, most work in physics has focused on the supersymmetric
case. Just for completeness, I should point out that there are 5 different supersymmetric
string theories: type I, type IIA, type IIB,
E
8

E
8
heterotic and
SO(32)
heterotic. For
more on these, see
 fiWeek 72fl
. We won't be getting into them here. Instead, I just want
to explain how fermions work in different dimensions, and why nice things happen in
dimensions of the form
8
k
+ 2
. Most of what I say is in Section 3 of
3)
 John H. Schwarz, fiIntroduction to supersymmetryfl, in
Superstrings and Supergrav -
ity, Proc. of the 28th Scottish Universities Summer School in Physics
, ed. A. T. Davies
and D. G. Sutherland, University Printing House, Oxford, 1985.
but mathematicians may also want to supplement this with material from the book
Spin
Geometry
by Lawson and Michelson, cited in
 fiWeek 82fl
.
To understand fermions in different dimensions we need to understand Clifford alge-
bras. As far as I know, when Clifford originally invented these algebras in the late 1800s,
he was trying to generalize Hamilton's quaternion algebra by considering algebras that
had lots of different anticommuting square roots of

1
, depending
on our preference. As Cecile DeWitt has pointed out, it
does
make a difference which
one we use.
With some work, one can check that these algebras go like this:
C
0
;
1
R
+
R
C
1
;
0
C
C
1
;
1
R
(2)
C
1
;
1
R
(2)
C
2
;
1
C
(2)
C
1
;
2
R
(2) +
R
(2)
C
3
;
1
H
(2)
C
1
;
3
R
(4)
C
4
;
1
H
(2) +
H
(2)
C
1
;
4
C
(4)
C
5
;
1
H
(4)
C
1
;
5
H
(4)
C
6
;
1
C
(8)
C
1
;
6
H
(4) +
H
(4)
C
7
;
1
R
(16)
C
1
;
7
H
(8)
I've only listed these up to
8
-dimensional Minkowski spacetime, and the cool thing is
that after that they sort of repeat Š more precisely,
C
n
+8
;
1
is just the same as
16

16
matrices with entries in
C
n;
1
, and
C
1
;n
+8
is just
16

16
matrices with entries in
C
1
;n
!
This fiperiod-8fl phenomenon, sometimes called Bott periodicity, has implications for all
sorts of branches of math and physics. This is why fermions in 2 dimensions are a bit
like fermions in 10 dimensions and 18 dimensions and 26 dimensions. . . .
In physics, we describe fermions using fispinorsfl, but there are different kinds of
spinors: Dirac spinors, Weyl spinors, Majorana spinors, and even MajoranaŒWeyl spinors.
This is a bit technical but I want to dig into it here, since it explains what's special about
8
k
+ 2
dimensions and especially 10 dimensions.
Before I get technical, though, let me just summarize the point for those of you
who don't want all the gory details. fiDirac spinorsfl are what you use to describe spin-
1
=
2
particles that come in both left-handed and right-handed forms and aren't their
own antiparticle Š like the electron. Weyl spinors have half as many components, and
describe spin-
1
=
2
particles with an intrinsic handedness that aren't their own antiparticle
Š like the neutrino. fiWeyl spinorsfl are only possible in even dimensions!
Both these sorts of spinors are ficomplexfl Š they have complex-valued components.
But there are also real spinors. These are used for describing particles that are their own
antiparticle, because the operation of turning a particle into an antiparticle is described
mathematically by complex conjugation. fiMajorana spinorsfl describe spin-
1
=
2
particles
that come in both left-handed and right-handed forms and are their own antiparticle.
Finally, fiMajoranaŒWeyl spinorsfl are used to describe spin-
1
=
2
particles with an intrinsic
handedness that are their own antiparticle.
As far as we can tell, none of the particles we've seen are Majorana or MajoranaŒWeyl
spinors, although if the neutrino has a mass it might be a Majorana spinor. Majorana and
MajoranaŒWeyl spinors only exist in certain dimensions. In particular, MajoranaŒWeyl
spinors are very nicky: they only work in dimensions of the form
8
k
+ 2
. This is part of
what makes supersymmetric string theory work in 10 dimensions!
Now let me describe the technical details. I'm doing this mainly for my own benet;
if I write this up, I'll be able to refer to it whenever I forget it. For those of you who stick
with me, there will be a little reward: we'll see that a certain kind of supersymmetric
231
 WEEK 93 OCTOBER 27, 1996
gauge theory, in which there's a symmetry between gauge bosons and fermions, only
works in dimensions 3, 4, 6, and 10. Perhaps coincidentally Š I don't understand this
stuff well enough to know Š these are also the dimensions when supersymmetric string
theory works classically. (It's the quantum version that only works in dimension 10.)
So: part of the point of these Clifford algebras is that they give representations of the
double cover of the Lorentz group in different dimensions. In
 fiWeek 61fl
 I explained this
double cover business, and how the group
SO(
n
)
of rotations of
n
-dimensional Euclidean
space has a double cover called
Spin(
n
)
. Similarly, the Lorentz group of
n
-dimensional
Minkowski space, written
SO(
n

1
;
1
, become isometric. There is a single even self-dual
lattice in 17+1 dimensions,

y
j
y
i
while the bosonic coordinates commute with fermionic ones:
x
i
y
j
=
y
j
x
i
:
If you've studied bosons and fermions this will be sort of familiar; all the differences be-
tween them arise from the difference between commuting and anticommuting variables.
For a little glimpse of this subject try:
4)
 John Baez, Spin and the harmonic oscillator,
http://math.ucr.edu/home/baez/
harmonic.html
.
As it so happens, supersymmetric string theory Š often abbreviated to fisuperstring
theoryfl Š works best in 10 dimensions. There are ve main versions of superstring
theory, which I described in
 fiWeek 74fl
. The type I string theory involves open strings
Š little segments rather than loops. The type IIA and type IIB theories involve closed
strings, that is, loops. But the most popular sort of superstring theories are the fiheterotic
stringsfl. A nice introduction to these, written by one of their discoverers, is:
5)
 David J. Gross, fiThe heterotic stringfl, in
Workshop on Unied String Theories
,
eds. M. Green and D. Gross, World Scientic, Singapore, 1986, pp. 357Œ399.
These theories involve closed strings, but the odd thing about them, which accounts for
the name fiheteroticfl, is that vibrations of the string going around one way are super-
symmetric and act as if they were in 10 dimensions, while the vibrations going around
the other way are bosonic and act as if they were in 26 dimensions!
To get this string with a split personality to make sense, people cleverly think of the
26 dimensional spacetime for the bosonic part as a 10-dimensional spacetime times a
little
16
-dimensional curled-up space, or ficompact manifoldfl. To get the theory to work,
it seems that this compact manifold needs to be at, which means it has to be a torus
Š a 16-dimensional torus. We can think of any such torus as
16
-dimensional Euclidean
244
 WEEK 95 NOVEMBER 26, 1996
space fimodulo a latticefl. Remember, a lattice in Euclidean space is something that looks
sort of like this:
x
y
















Mathematically, it's just a discrete subset
L
of
R
n
(
n
-dimensional Euclidean space, with
its usual coordinates) with the property that if
x
and
y
lie in
L
, so does
j x
+
k y
for all
integers
j
and
k
. When we form
n
-dimensional Euclidean space fimodulo a latticefl, we
decree two points
x
and
y
to be the same if
x

y
is in
L
. For example, all the points
labelled
x
in the gure above count as the same when we fimod out by the latticefl... so
in this case, we get a
2
-dimensional torus.
For more on
2
-dimensional tori and their relation to complex analysis, you can read
fiWeek 13fl
. Here we are going to be macho and plunge right into talking about lattices
and tori in arbitrary dimensions.
To get our
26
-dimensional string theory to work out nicely when we curl up
16
-
dimensional space to a
16
-dimensional torus, it turns out that we need the lattice
L
that we're modding out by to have some nice properties. First of all, it needs to be an
fiintegralfl lattice, meaning that for any vectors
x
and
y
in
L
the dot product
x

y
must
be an integer. This is no big deal Š there are gadzillions of integral lattices. In fact,
sometimes when people say filatticefl they really mean fiintegral latticefl. What's more of
a big deal is that
L
must be fievenfl, that is, for any
x
in
L
the inner product
x

x
is even.
This implies that
L
is integral, by the identity
(
x
+
y
)

(
x
+
y
) =
x

x
+ 2
x

y
+
y

y :
But what's really a big deal is that
L
must also be fiunimodularfl. There are different
ways to dene this concept. Perhaps the easiest to grok is that the volume of each lattice
cell Š e.g., each parallelogram in the picture above Š is
1
. Another way to say it is
this. Take any basis of
L
, that is, a bunch of vectors in
L
such that any vector in
L
can
be uniquely expressed as an integer linear combination of these vectors. Then make a
matrix with the components of these vectors as rows. Then take its determinant. That
should equal plus or minus
1
. Still another way to say it is this. We can dene the fidualfl
of
L
, say
L

, to be all the vectors
x
such that
x

y
is an integer for all
y
in
L
. An integer
lattice is one that's contained in its dual, but
L
is unimodular if and only if
L
=
L

. So
people also call unimodular lattices fiself-dualfl. It's a fun little exercise in linear algebra
to show that all these denitions are equivalent.
245
 WEEK 95 NOVEMBER 26, 1996
Why does
L
have to be an even unimodular lattice? Well, one can begin to under-
stand this a litle by thinking about what a closed string vibrating in a torus is like. If
you've ever studied the quantum mechanics of a particle on a torus (e.g. a circle!) you
may know that its momentum is quantized, and must be an element of
L

. So the
momentum of the center of mass of the string lies in
L

.
On the other hand, the string can also wrap around the torus in various topologically
different ways. Since two points in Euclidean space correspond to the same point in the
torus if they differ by a vector in
L
, if we imagine the string as living up in Euclidean
space, and trace our nger all around it, we don't necesarily come back to the same point
in Euclidean space: the same point
plus
any vector in
L
will do. So the way the string
wraps around the torus is described by a vector in
L
. If you've heard of the fiwinding
numberfl, this is just a generalization of that.
So both
L
and
L

are really important here (which has to do with the fashionable
subject of fistring dualityfl), and a bunch more work shows that they
both
need to be
even, which implies that
L
is even and unimodular.
Now something cool happens: even unimodular lattices are only possible in certain
dimensions Š namely, dimensions divisible by 8. So we luck out, since we're in dimen-
sion 16.
In dimension 8 there is only
one
even unimodular lattice (up to isometry), namely
the wonderful lattice
E
8
! The easiest way to think about this lattice is as follows. Say
you are packing spheres in
n
dimensions in a checkerboard lattice Š in other words, you
color the cubes of an
n
-dimensional checkerboard alternately red and black, and you put
spheres centered at the center of every red cube, using the biggest spheres that will t.
There are some little hole left over where you could put smaller spheres if you wanted.
And as you go up to higher dimensions, these little holes get bigger! By the time you
get up to dimension 8, there's enough room to put another sphere
of the same size as the
rest
in each hole! If you do that, you get the lattice
E
8
. (I explained this and a bunch of
other lattices in
 fiWeek 65fl
, so for more info take a look at that.)
In dimension 16 there are only
two
even unimodular lattices. One is
E
8

E
8
. A vector
in this is just a pair of vectors in
E
8
. The other is called
D
+
16
, which we get the same way
as we got
E
8
: we take a checkerboard lattice in 16 dimensions and stick in extra spheres
in all the holes. More mathematically, to get
E
8
or
D
+
16
, we take all vectors in
R
8
or
R
16
,
respectively, whose coordinates are either
all
integers or
all
half-integers, for which the
coordinates add up to an even integer. (A fihalf-integerfl is an integer plus
1
=
2
.)
So
E
8

E
8
and
D
+
16
give us the two kinds of heterotic string theory! They are often
called the
E
8

E
8
and
SO(32)
heterotic theories.
In
 fiWeek 63fl
 and
 fiWeek 64fl
 I explained a bit about lattices and Lie groups, and if
you know about that stuff, I can explain why the second sort of string theory is called
fi
SO(32)
fl. Any compact Lie group has a maximal torus, which we can think of as some
Euclidean space modulo a lattice. There's a group called
E
8
, described in
 fiWeek 90fl
,
which gives us the
E
8
lattice this way, and the product of two copies of this group gives
us
E
8

E
8
. On the other hand, we can also get a lattice this way from the group
SO(32)
of rotations in 32 dimensions, and after a little nagling this gives us the
D
+
16
lattice (technically, we need to use the lattice generated by the weights of the adjoint
representation and one of the spinor representations, according to Gross). In any event,
it turns out that these two versions of heterotic string theory act, at low energies, like
gauge eld theories with gauge group
E
8

E
8
and
SO(32)
, respectively! People seem
246
 WEEK 95 NOVEMBER 26, 1996
especially optimistic that the
E
8

E
8
theory is relevant to real-world particle physics;
see for example:
6)
 Edward Witten, fiUnication in ten dimensionsfl, in
Workshop on Unied String
Theories
, eds. M. Green and D. Gross, World Scientic, Singapore, 1986, pp. 438Œ
456.
Edward Witten, fiTopological tools in ten dimensional physicsfl, with an appendix
by R. E. Stong, in
Workshop on Unied String Theories
, eds. M. Green and D. Gross,
World Scientic, Singapore, 1986, pp. 400Œ437.
The rst paper listed here is about particle physics; I mention the second here just
because
E
8
fans should enjoy it Š it discusses the classication of bundles with
E
8
as
gauge group.
Anyway, what does all this have to do with Lucas and his stack of cannon balls?
Well, in dimension 24, there are
24
even unimodular lattices, which were classied
by Niemeier. A few of these are obvious, like
E
8

E
8

E
8
and
E
8

D
+
16
, but the coolest
one is the fiLeech latticefl, which is the only one having no vectors of length 2. This
is related to a whole
world
of bizarre and perversely fascinating mathematics, like the
fiMonster groupfl, the largest sporadic nite simple group Š and also to string theory. I
said a bit about this stuff in
 fiWeek 66fl
, and I will say more in the future, but for now let
me just describe how to get the Leech lattice.
First of all, let's think about Lorentzian lattices, that is, lattices in Minkowski space-
time instead of Euclidean space. The difference is just that now the dot product is dened
by
(
x
1
; : : : ; x
n
)

(
y
1
; : : : ; y
n
) =

x
1
y
1
+
x
2
y
2
+
  
+
x
n
y
n
with the rst coordinate representing time. It turns out that the only even unimodular
Lorentzian lattices occur in dimensions of the form
8
k
+ 2
. There is only
one
in each
of those dimensions, and it is very easy to describe: it consists of all vectors whose
coordinates are either all integers or all half-integers, and whose coordinates add up to
an even number.
Note that the dimensions of this form: 2, 10, 18, 26, etc., are precisely the dimensions
I said were specially important in
 fiWeek 93fl
 for some
other
string-theoretic reason. Is
this a ficoincidencefl? Well, all I can say is that I don't understand it.
Anyway, the
10
-dimensional even unimodular Lorentzian lattice is pretty neat and
has attracted some attention in string theory:
7)
 Reinhold W. Gebert and Hermann Nicolai, fi
E
10
for beginnersfl, available as
hep-th/
9411188
but the
26
-dimensional one is even more neat. In particular, thanks to the cannonball
trick of Lucas, the vector
v
= (70
;
0
;
1
;
2
;
3
;
4
; : : : ;
24)
is filightlikefl. In other words,
v

v
= 0
:
What this implies is that if we let
T
be the set of all integer multiples of
v
, and let
S
be
the set of all vectors
x
in our lattice with
x

v
= 0
, then
T
is contained in
S
, and
S =T
is
a
24
-dimensional lattice Š the Leech lattice!
247
 WEEK 95 NOVEMBER 26, 1996
Now
that
has all sorts of ramications that I'm just barely beginning to understand.
For one, it means that if we do bosonic string theory in 26 dimensions on
R
26
modulo
the
26
-dimensional even unimodular lattice, we get a theory having lots of symmetries
related to those of the Leech lattice. In some sense this is a fimaximally symmetricfl
approach to
26
-dimensional bosonic string theory:
8)
 Gregory Moore, fiFinite in all directionsfl, available as
hep-th/9305139
.
Indeed, the Monster group is lurking around as a symmetry group here! For a physics-
avored introduction to that aspect, try:
9)
 Reinhold W. Gebert, fiIntroduction to vertex algebras, Borcherds algebras, and the
Monster Lie algebrafl,
Int. Jour. Mod. Phys. A
8
(1993), 5441Œ5503. Also available
as
hep-th/9308151
.
and for a detailed mathematical tour see:
10)
 Igor Frenkel, James Lepowsky, and Arne Meurman,
Vertex Operator Algebras and
the Monster
, Academic Press, New York, 1988.
Also try the very readable review articles by Richard Borcherds, who came up with a lot
of this business:
11)
 Richard Borcherds, fiAutomorphic forms and Lie algebrasfl, available at
https://math.berkeley.edu/
˘
reb/papers/index.html#preprints
.
Richard Borcherds, fiSporadic groups and string theoryfl, available at
https://math.berkeley.edu/
˘
reb/papers/index.html#preprints
.
Well, there is a lot more to say, but I need to go home and pack for my Thanksgiving
travels. Let me conclude by answering a natural followup question: how many even
unimodular lattices are there in 32 dimensions? Well, one can show that there are
at
least 80 million!
Some of you may have wondered what's happened to the fiTale of
n
-Categoriesfl. I
haven't forgotten that! In fact, earlier this fall I nished writing a big fat paper on 2-
Hilbert spaces (which are to Hilbert spaces as categories are to sets), and since then I
have been struggling to nish another big fat paper with James Dolan, on the general
denition of fiweak
n
-categoriesfl. I want to talk about this sort of thing, and other
progress on
n
-categories and physics, but I've been so busy
working
on it that I haven't
had time to
chat
about it on This Week's Finds. Maybe soon I'll nd time.
Addenda:
Robin Chapman pointed out that Anglin's proof also appears in the
Ameri-
can Mathematical Monthly
, February 1990, pp. 120Œ124, and that another elementary
proof has subsequently appeared in the
Journal of Number Theory
. David Morrison
pointed out in email that since the sum
1
2
+ 2
2
+
  
+
n
2
=
m
2
248
 WEEK 95 NOVEMBER 26, 1996
is
n
(
n
+ 1)(2
n
+ 1)
=
6
, this problem can be solved by nding all the rational points
(
n; m
)
on the elliptic curve
n
3
3
+
n
2
2
+
n
6
=
m
2
which is the sort of thing folks know how to do.
Also, here's something Michael Thayer wrote on one of the newsgroups, and my
reply:
John Baez wrote:
In particular, thanks to the cannonball trick of Lucas, the vector
v
= (70
;
0
;
1
;
2
;
3
;
4
; : : : ;
24)
is filightlikefl. In other words,
v

v
= 0
.
I don't see what is so signicant about the vector v. For instance, the 10 dimen-
sional vector (3,1,1,1,1,1,1,1,1,1) is also light like, and you make no big deal
about that. Is there some reason why the ascending values in
v
are important?
Yikes! Thanks for catching that massive hole in the exposition.
You're right that there's no shortage of lightlike vectors in the even unimodular
Lorentzian lattices of other dimensions
8
n
+ 2
; there are also lots of other lightlike vec-
tors in the
26
-dimensional one. Any one of these gives us a lattice in
8
n
-dimensional
Euclidean space. In fact, we can get all 24 even unimodular lattices in
24
-dimensional
Euclidean space by suitable choices of lightlike vector. The lightlike vector you wrote
down happens to give us the
E
8
lattice in 8 dimensions.
So what's so special about I wrote, which gives the Leech lattice? Of course the Leech
lattice is itself special, but what does this have to do with the nicely ascending values of
the components of
v
?
Alas, I don't know the real answer. I'm not an expert on this stuff; I'm just explaining
it in order to try to learn it. Let me just say what I know, which all comes from Chap. 27
of Conway and Sloane's book
Sphere Packings, Lattices, and Groups
.
If we have a lattice, we say a vector
r
in it is a firootfl if the reection through
r
is a symmetry of the lattice. Corresponding to each root is a hyperplane consisting of
all vectors perpendicular to that root. These chop space into a bunch of fifundamental
regionsfl. If we pick a fundamental region, the roots corresponding to the hyperplanes
that form the walls of this region are called fifundamental rootsfl. The nice thing about
the fundamental roots is that the reection through any root is a product of reections
through these fundamental roots.
(For more stuff on reection groups and lattices see
 fiWeek 62fl
 and the following
weeks.)
In 1983 John Conway published a paper where he showed various amazing things;
this is now Chapter 27 of the above book. First, he shows that the fundamental roots of
the even unimodular Lorentzian lattices in dimensions 10, 18, and 26 are the vectors
r
with
r

r
= 2
and
r

v
=

7
degrees above absolute zero. A team at Rice University did it with lithium soon after,
followed by a team at MIT, who did it with sodium.
Check out:
2)
 NIST, fiPhysicists create new state of matterfl, July 13, 1995. Available at
https:/
/www.nist.gov/news-events/news/1995/07/physicists-create-new-state-
matter-record-low-temperature
Atomcool home page,
http://atomcool.rice.edu/
fiBoseŒEinstein condensation of ultracold sodiumfl
https://web.archive.org/web/
19990203201237/http://amo.mit.edu/%7Ebec/news/news.html
So what's the news? Well, recently the team at MIT, led by Wolfgang Ketterle, made
two blobs of BoseŒEinstein condensate out of sodium atoms. Ramming these into each
other, they were able to see interference fringes just as in a laser! In other words, they are
seeing interference of matter waves, just as quantum mechanics predicts, but involving
lots of atoms in a coherent state rather than a single electron as in the famous double
slit experiment.
In honor of this event, I hereby present the following limerick composed by the poet
Lisa Raphals, with myself serving as science consultant. It may aid your appreciation if I
note rst that fiSquantumfl is an actual town in Massachusetts. With no further ado:
A metaphysician from Squantum
Was asked, what's the state of the quantum?
It's all reciprocity: Position, velocity Š
They're never both there when you want 'em!
Now on to some more technical stuff. . . .
I am now visiting the Center for Gravitational Physics and Geometry here at Penn
State, which is a delightful place for people interested in the loop representation of
256
 WEEK 97 FEBRUARY 8, 1997
quantum gravity (see
 fiWeek 77fl
). Right now everyone is working on using the loop
representation to derive Hawking's formula which says that the entropy of a black hole
is proportional to the surface area of its event horizon.
When I arrived, Jorge Pullin handed me a copy of his book:
3)
 Rodolfo Gambini and Jorge Pullin,
Loops, Knots, Gauge Theories, and Quantum
Gravity
, Cambridge U. Press, Cambridge, 1996.
Here is the table of contents:
1.
 Holonomies and the group of loops
2.
 Loop coordinates and the extended group of loops
3.
 The loop representation
4.
 Maxwell theory
5.
 YangŒMills theories
6.
 Lattice techniques
7.
 Quantum gravity
8.
 The loop representation of quantum gravity
9.
 Loop representation: further developments
10.
 Knot theory and physical states of quantum gravity
11.
 The extended loop representation of quantum gravity
12.
 Conclusions, present status and outlook
This is presently the most complete introduction available to the filoop representa-
tionfl concept, as applied to electromagnetism, YangŒMills theory, and quantum gravity.
Gambini was one of the original inventors of this notion, and this book covers the whole
sweep of its ramications, with a special emphasis on a particular technical form, the
fiextended loop representationfl, which he has been developing with Pullin and other
collaborators.
What the heck is the loop representation, anyway? Well, all the forces we know are
described by gauge theories, and gauge theories all describe the fiphasefl, or generaliza-
tion thereof, that a particle acquires when you carry it around a loop. In the case of
electromagnetism, for example, a charged quantum particle carried around a loop in
space acquires a phase equal to
exp(

cA
)
where
h
W
(
g
)
i
is the vacuum expectation value of the Wilson loop, and
A
is the area
spanned by the loop
g
. The point is that
h
W
(
g
)
i
is the same as what I was (a bit sloppily)
calling the probability of the quark-antiquark pair tracing out the loop
g
.
't Hooft calls the Wilson loops fiorder operatorsfl. We don't really need to worry why
he calls them this, but if you know how physicists think, you may know that the Wilson
loops are keeping track of a kind of fiorder parameterfl of the vacuum state. Anyway,
his idea was to study the Wilson loops by introducing some other operators he called
fidisorder operatorsfl.
Chromodynamics is an
SU(3)
gauge theory but it's a little clearer if we work with any
SU(
N
)
gauge theory. Notice that the center of the group
SU(
N
)
consists of the matrices
of the form
exp(2
ˇ in=N
)
where
n
is an integer. So if we have a loop
h
, we can imagine an operator that does
the following thing: it modies the connection, or vector potential, in such a way that
if you do parallel transport around a tiny loop linking
h
once, the holonomy changes to
exp(2
ˇ i=N
)
times what it had been. Note: this is a gauge-invariant thing to do, because
that
exp(2
ˇ i=N
)
is in the center of
SU(
N
)
! So just as the Wilson loop observables are
gauge-invariant, we can hope for some some fidisorder operatorsfl
V
(
h
)
that modify the
connection in this way.
If you think about it, what this means is that the following commutation relations
hold:
W
(
g
)
V
(
h
) =
V
(
h
)
W
(
g
) exp(2
ˇ iL
(
g ; h
)
=N
)
259
 WEEK 97 FEBRUARY 8, 1997
where
L
(
g ; h
)
is the linking number of the loops
g
and
h
, which counts h ow many times
g
wraps around
h
.
There is an obvious symmetry or fidualityfl between the
V
's and the
W
's going on here.
In fact, just as
W
's satisfy an area law where there is connement of chromoelectric eld
lines into ux tubes, I believe the
V
's satisfy an area law when there is connement of
chromomagnetic eld lines into ux tubes. The simplest case of this kind of thing occurs
in plain old electromagnetism, where plain old magnetic eld lines are conned into
ux tubes in type II superconductors. For this reason connement of electric eld lines
is sometimes called fidual superconductivityfl.
Perhaps the simplest way of beginning to understand this stuff more deeply is to un-
derstand the wonderful formula proved by Ashtekar and Corichi in the following paper:
6)
 Abhay Ashtekar and Alejandro Corichi, fiGauss linking number and electro-magnetic
uncertainty principlefl,
Phys. Rev. D
56
(1997), 2073. Also available as
hep-th/
9701136
.
This formula applies to plain old electromagnetism, or more precisely, quantum electro-
dynamics. If we work in units where
~
= 1
, and consider a particle of charge
1
, the
Wilson loop operator
W
(
g
)
in electromagnetism is just
W
(
g
) = e xp(

E
(
h
)
B
(
g
) =
iL
(
g ; h
)
:
In other words, the electric and magnetic elds don't commute in quantum electrody-
namics, and the Heisenberg uncertainty of the electric eld owing through a loop
g
and
the magnetic eld owing through a loop
h
is proportional to the linking number of
g
and
h
!
Quantum mechanics, electromagnetism, and knot theory are clearly quite tangled up
here. Since the linking number was rst discovered by Gauss in his work on magnetism,
it's all quite tting.
And that leads me to the last paper I want to mention this week. It should be of
great interest to Vassiliev invariant fans; see
 fiWeek 3fl
 if you don't know what a Vassiliev
invariant is.
7)
 Dror Bar-Natan and Alexander Stoimenow, fiThe fundamental theorem of Vassiliev
invariantsfl, in
Geometry and Physics
, CRC Press, Boca Raton, 2021, pp 101Œ134.
Also available as
q-alg/9702009
.
Let me just quote the abstract here:
The fifundamental theorem of Vassiliev invariantsfl says that every weight system
can be integrated to a knot invariant. We discuss four different approaches to
the proof of this theorem: a topological/combinatorial approach following M.
Hutchings, a geometrical approach following Kontsevich, an algebraic approach
260
 WEEK 97 FEBRUARY 8, 1997
following Drinfel'd's theory of associators, and a physical approach coming from
the ChernŒSimons quantum eld theory. Each of these approaches is unsatis-
factory in one way or another, and hence we argue that we still don't really
understand the fundamental theorem of Vassiliev invariants.
261
 WEEK 98 FEBRUARY 27, 1997
Week 98
February 27, 1997
I feel guilty for slacking off on This Week's Finds, so I should explain the reason. Lots of
things have been building up that I'm dying to talk about, but new ones keep coming in
at such a rapid rate that I never feel I have time!
I will have to be ruthless, and face up to the fact that a quick and imperfect exposition
is better than none.
First of all, here at the Center for Gravitational Physics and Geometry there are a lot
of interesting attempts going on to compute the entropy of black holes from rst prin-
ciples. Bekenstein, Hawking and many others have used a wide variety of semiclassical
arguments to argue that black holes satisfy
S
=
A=
4
where
S
is the entropy and
A
is the area of the event horizon, both measured in Planck's
units, where
G
=
c
=
~
= 1
.
For example, using purely classical reasoning (general relativity, but no quantum
theory) one can prove the fi2nd law of black hole thermodynamicsfl, which says that
A
always increases. As Bekenstein noted, this suggests that the area of the event horizon
is somehow analogous to entropy. However, by itself this does not determine the magic
number
1
=
4
, which can only be derived using quantum theory (as one can see by simple
dimensional analysis).
By semiclassical reasoning Š studying quantum electrodynamics in the Schwarzschild
metric used to describe black holes Š Hawking showed that black holes should radiate
as if they had a temperature inversely proportional to their mass:
T
=
1
8
ˇ M
:
This made the analogy between entropy and event horizon area much more than an
analogy, because it meant that one could assign a temperature to black holes and see
if they satisfy the laws of thermodynamics. It turns out that if you consider
A=
4
to be
the entropy of a black hole, you can eliminate seeming violations of the 2nd law that
otherwise arise in thought experiments where you get rid of entropy by throwing it into
a black hole. In other words, if you throw something with entropy
S
into a black hole,
calculations seem to show that the area of the event horizon always increases by at least
4
S
!
So far nothing I've said is related to full-edged quantum gravity, because in the
semiclassical arguments one is still working in the approximation where the gravitational
eld is treated classically. An interesting test of any theory of quantum gravity is whether
can use it to derive
S
=
A=
4
. In a subject with no real experimental evidence, this is the
closest we have to an fiexperimental resultfl that our theory should predict.
Recently the string theorists have done some calculations claiming to show that string
theory predicts
S
=
A=
4
. Personally I feel that while these calculations are interesting
they are far from denitive. For example, they all involve taking calculations done using
perturbative string theory on
at
spacetime and extrapolating them drastically to the
262
 WEEK 98 FEBRUARY 27, 1997
regime in which string theory approximates general relativity. One typically uses ideas
from supersymmetry to justify such extrapolations; however, these ideas only seem to
apply to fiextremal black holesfl, having the maximum possible charge for a black hole
of a given mass and angular momentum. Realistic black holes are far from extremal. In
short, while exciting, these calculations still need to be taken with a grain of salt.
Of course, I am biased because I am interested in another approach to quantum
gravity, the loop representation of quantum gravity, which folks are working on here at
the CGPG, among other places. This is in many ways a more conservative approach. The
idea is to simply take Einstein's equation for general relativity and quantize it, rather
than trying to develop a theory of
all
particles and forces as in string theory. Of course,
for various reasons it is not so easy to quantize Einstein's equation. String theorists
think it's
impossible
without dragging in all sorts of other forces and particles, but folks
working on the loop representation are more optimistic. This is an ongoing argument,
but certainly a good test of the loop representation would be to try to use it to derive
Hawking's formula S = A/4. If the loop representation is really any good, this should
be possible, because many different lines of reasoning using only general relativity and
quantum theory lead to this formula.
I've already mentioned a few attempts to do this in
 flWeek 56
fi,
 flWeek 57
fl, and
 fiWeek
87fl
. These were promising, but they didn't get the magical number
1
=
4
. Also, they are
rather rough, in that they do computations on some region with boundary, but don't use
anything that ensures the boundary is an event horizon.
Recently Kirill Krasnov has made some progress:
1)
 Kirill Krasnov, fiOn quantum statistical mechanics of Schwarzschild black holefl,
Gen. Rel. Grav.
30
(1998), 53Œ68. Also available as
gr-qc/9605047
.
This paper still doesn't get the magic number
1
=
4
, and Krasnov later realized it has a
few mistakes in it, but it does something very cool. It notes that the boundary conditions
holding on the event horizon of a Schwarzschild black hole are closely related to ChernŒ
Simons theory. Now is not the time for me to go into ChernŒSimons theory, but basically,
it lets you apply a lot of neat mathematics to calculate everything to your heart's content,
very much as Carlip did on his work on the toy model of a 2+1-dimensional black
hole (see
 fiWeek 41fl
). Also, it sheds new light on the relationship between topological
quantum eld theory and quantum gravity, something I am always trying to understand
better.
While I'm at it, I should note the existence of a paper that reworks Carlip's calculation
from a slightly different angle:
2)
 Maximo Banados and Andres Gomberoff, fiBlack hole entropy in the ChernŒSimons
formulation of 2+1 gravityfl,
Phys. Rev. D
55
(1997) 6162Œ6167. Also available as
gr-qc/9611044
.
2+1-dimensional quantum gravity is very simple compared to the 3+1-dimensional
quantum gravity we'd really like to understand: in a sense it's fiexactly solvablefl. But
there are still some puzzling things about Carlip's computation of the entropy of a black
hole in 2+1 dimensions which need guring out, so every paper on the subject is worth
looking at, if you're interested in black hole entropy.
Speaking of topological quantum eld theory and quantum gravity, I just nished a
paper on these topics:
263
 WEEK 98 FEBRUARY 27, 1997
3)
 John Baez, fiDegenerate solutions of general relativity from topological eld the-
oryfl,
Commun. Math. Phys.
193
(1998) 219Œ231. Also available as
gr-qc/
9702051
.
Let me just summarize the basic idea, resisting the temptation to become insanely
technical.
A while ago Rovelli and Smolin introduced Penrose's notion of fispin networkfl into
the loop representation of quantum gravity. I described spin networks pretty carefully in
fiWeek 43fl
, but here let me just say that they are graphs embedded in space with edges
labelled by spins
j
= 0
;
1
=
2
;
1
;
3
=
2
; : : :
, just as in the quantum mechanics of angular mo-
mentum, and with vertices labelled by fiintertwining operatorsfl, which are other gadgets
that come up in the study of angular momentum. In the loop representation these spin
networks form a basis of states. Geometrical observables like the area of surfaces and
the volumes of regions have been quantized and their matrix elements computed in the
spin network basis, giving us a nice picture of fiquantum 3-geometriesfl, that is, the pos-
sible geometries of space in the context of quantum gravity. In this picture, the edges of
spin networks play the role of quantized ux tubes of area, much as the magnetic eld
comes in quantized ux tubes in a type II superconductor. To work out the area of a
surface in some spin network state, you just total up contributions from each edge of the
spin network that pokes through the surface. An edge labelled with spin
j
carries an area
equal to
p
j
(
j
+ 1)
times the Planck length squared. What's cool is that this is not merely
postulated, it's derived from fairly standard ideas about how you turn observables into
operators in quantum mechanics.
However, the dynamics of quantum gravity is more obscure. Technical issues aside,
the main problem is that while we have a nice picture of quantum 3-geometries, we
don't have a similar picture of the
4-dimensional
, or
spacetime
, aspects of the theory. To
represent a physical state of quantum gravity, a spin network state (or linear combination
thereof) has to satisfy something called the WheelerŒDeWitt equation. This is sort of the
quantum gravity analog of the Schrodinger equation. There is a lot of controversy over
the WheelerŒDeWitt equation and what's the right way to write it down in the loop
representation. The really annoying thing, however, is that even if you feel you know
how to write it down Š for example, Thomas Thiemann has worked out one way (see
fiWeek 85fl
) Š and can nd solutions, you still don't necessarily have a good intuition
as to what the solutions
mean
. For example, almost everyone seems to agree that spin
networks with no vertices should satisfy the WheelerŒDeWitt equation. These are just
knots or links with edges are labelled by spins. We know these states are supposed to
represent fiquantum 4-geometriesfl satisfying the quantized Einstein equations. But how
should we visualize these states in
4
-dimensional terms?
In search of some insight into the
4
-dimensional interpretation of these states, I turn
to classical general relativity. In my paper, I construct solutions of the equations of
general relativity which at a typical xed time look like fiux tubes of areafl reminiscent
of the loop states of quantum gravity. These are fidegenerate solutionsfl, meaning that
the fi3-metricfl, the tensor you use to measure distances in 3-dimensional space, is zero in
lots of regions of space. Here I should warn you that ordinary general relativity doesn't
allow degenerate metrics like this. The loop representation works with an extension of
general relativity that covers the case of degenerate metrics; for more on this, see
 fiWeek
88fl
.
264
 WEEK 98 FEBRUARY 27, 1997
More precisely, if you look at these fiux tubefl solutions at a typical time, the 3-metric
vanishes outside a collection of solid tori embedded in space, while inside any of these
solid tori the metric is degenerate in the longitudinal direction, but nondegenerate in the
two transverse directions.
Now since these are classical solutions Š no quantum theory in sight! Š there is
no problem with understanding what they do as time passes. We can solve Einstein's
equation and get a 4-metric, a metric on spacetime. The
4
-dimensional picture is as fol-
lows: given any surface

embedded in spacetime, I get solutions for which the 4-metric
vanishes outside a neighborhood of

. Inside this neighborhood, the 4-metric is zero in
the two directions tangent to

but nondegenerate in the two transverse directions. In
the 4-geometry dened by one of these solutions, the area of a typical surface

0
inter-
secting

in some isolated points is a sum of contributions from the points where

and

0
intersect.
The solutions I study are inspired by the work of Mike Reisenberger, who studied a
solution for which the metric vanishes outside a neighborhood of a sphere embedded in
R
4
. I consider more general surfaces embedded in more general 4-manifolds, so I need
to worry a lot more about topological issues. Also, I allow the possibility of a nonzero
cosmological constant (this being a parameter in Einstein's equation that determines the
energy density of the vacuum). A lot of the most interesting stuff happens for nonzero
cosmological constant, and this case actually helps one understand the case of vanishing
cosmological constant as a kind of limiting case.
It turns out that the interesting degrees of freedom of the metric living on the surface

in spacetime are described by elds living on this surface. In fact, these elds are
solutions of a
2
-dimensional topological eld theory called
B F
theory. To prove this, I
take advantage of the relation between general relativity and
B F
theory in 4 dimensions,
together with the fact that
B F
theory behaves in a simple manner under dimensional
reduction.
Another neat thing is that to get a solution of general relativity this way, we need to
pick a fiframingfl of

. Roughly speaking, this means we need to pick a way of thick-
ening up the surface

to a neighborhood that looks like


D
2
, where
D
2
is the
2
-dimensional disc. This is precisely the
4
-dimensional analog of a framing of a knot or
link in 3-dimensions. People who know about topological quantum eld theory know
that framings are very important. In fact, I can show that my solutions of general relativ-
ity are closely related to ChernŒSimons theory, a
3
-dimensional topological eld theory
famous for giving invariants of framed knots and links. What's beginning to emerge is a
picture that makes the
spacetime
aspects of framings easier to understand.
Now before I plunge into some even more esoteric stuff, let me briey return to
reality and answer the question you've all been secretly dying to ask: how does general
relativity impact the world of big business?
In plain terms: is all this fancy physics just an excuse to have fun visualizing evolving
spin networks in terms of quantum eld theories on surfaces embedded in
4
-dimensional
spacetime, etcetera etcetera... or does it actually contribute to the well-being of the
corporations upon which we depend?
Well, you may be surprised to know that general relativity plays an signicant role
in a $200-million business. Surprised? Read on! What follows is taken from the latest
issue of fiMatters of Gravityfl, the newsletter put out by Jorge Pullin. More precisely, it's
from:
265
 WEEK 98 FEBRUARY 27, 1997
4)
 Neil Ashby, fiGeneral relativity in the global positioning systemfl, in
Matters of Grav -
ity
, ed. Jorge Pullin, no.
9
, available at
http://www.phys.lsu.edu//mog/mog9/
node9.html
.
I will simply quote some excerpts from this fascinating article:
flThe Global Position System (GPS) consists of 24 earth-orbiting satellites, each
carrying accurate, stable atomic clocks. Four satellites are in each of six differ-
ent orbital planes, of inclination 55 degrees with respect to earth's equator. Or-
bital periods are 12 hours (sidereal), so that the apparent position of a satellite
against the background of stars repeats in 12 hours. Clock-driven transmitters
send out synchronous time signals, tagged with the position and time of the
transmission event, so that a receiver near the earth can determine its position
and time by decoding navigation messages from four satellites to nd the trans-
mission event coordinates, and then solving four simultaneous one-way signal
propagation equations. Conversely,

-ray detectors on the satellites could deter-
mine the space-time coordinates of a nuclear event by measuring signal arrival
times and solving four one-way propagation delay equations.
Apart possibly from high-energy accelerators, there are no other engineering
systems in existence today in which both special and general relativity have so
many applications. The system is based on the principle of the constancy of
c
in
a local inertial frame: the Earth-Centered Inertial or ECI frame. Time dilation
of moving clocks is signicant for clocks in the satellites as well as clocks at rest
on earth. The weak principle of equivalence nds expression in the presence of
several sources of large gravitational frequency shifts. Also, because the earth
and its satellites are in free fall, gravitational frequency shifts arising from the
tidal potentials of the moon and sun are only a few parts in 10‹16 and can be
neglected.
[. . . ]
At the time of launch of the rst NTS-2 satellite (June 1977), which contained
the rst Cesium clock to be placed in orbit, there were some who doubted that
relativistic effects were real. A frequency synthesizer was built into the satellite
clock system so that after launch, if in fact the rate of the clock in its nal
orbit was that predicted by GR , then the synthesizer could be turned on bringing
the clock to the coordinate rate necessary for operation. The atomic clock was
rst operated for about 20 days to measure its clock rate before turning on the
synthesizer. The frequency measured during that interval was +442.5 parts
in
10
12
faster than clocks on the ground; if left uncorrected this would have
resulted in timing errors of about 38,000 nanoseconds per day. The difference
between predicted and measured values of the frequency shift was only 3.97
parts in
10
12
, well within the accuracy capabilities of the orbiting clock. This
then gave about a 1% validation of the combined motional and gravitational
shifts for a clock at 4.2 earth radii.
[. . . ]
266
 WEEK 98 FEBRUARY 27, 1997
This system was intended primarily for navigation by military users having ac-
cess to encrypted satellite transmissions which are not available to civilian users.
Uncertainty of position determination in real time by using the Precise Position-
ing code is now about 2.4 meters. Averaging over time and over many satellites
reduces this uncertainty to the point where some users are currently interested in
modelling many effects down to the millimeter level. Even without this impetus,
the GPS provides a rich source of examples for the applications of the concepts
of relativity.
New and surprising applications of position determination and time transfer
based on GPS are continually being invented. Civilian applications include for
example, tracking elephants in Africa, studies of crustal plate movements, sur-
veying, mapping, exploration, salvage in the open ocean, vehicle eet tracking,
search and rescue, power line fault location, and synchronization of telecom-
munications nodes. About 60 manufacturers now produce over 350 different
commercial GPS products. Millions of receivers are being made each year; prices
of receivers at local hardware stores start in the neighborhood of $200.fl
Pretty cool, eh?
Okay, now for something completely different Š homotopy theory! Well, everything
I write about is actually secretly part of my grand plan to see how everything interesting
is related to everything else, but let me not delve into how homotopy theory is related to
topological quantum eld theory and thus quantum gravity. Let me simply mention the
existence of this great book:
5)
Handbook of Algebraic Topology
, ed. I. M. James, North-Holland, Amsterdam, 1995,
1324 pages.
Occasionally you come across a book that you wish you just download into your brain;
for me this is one of those books. It is probably not a good idea to read it if you are just
wanting to get started on algebraic topology; it assumes you are pretty familiar with the
basic ideas already, and it goes into a lot of depth, mainly in hardcore homotopy theory.
A lot of it is too technical for me to appreciate, but let me list a few chapters that I can
understand and like.
Ł
 Chapter 1, fiHomotopy typesfl by Hans-Joachim Baues, is a great survey of different
models of homotopy types. Remember, we say two topological spaces
X
and
Y
are
homotopy equivalent if there are continuous functions
f
:
X
!
Y
and
g
:
Y
!
X
that are inverses fiup to homotopyfl. In other words, we don't require that
f g
and
g f
are
equal
to identity functions, but merely that they can both be
continuously
deformed
to identity functions. So for example the circle and an annulus are ho-
motopy equivalent, and we say therefore that they represent the same fihomotopy
typefl.
The cool thing is that there turn out to be very elegant algebraic and combinatorial
ways of describing homotopy types that don't mention topology at all. Perhaps
the most beautiful way of all is a way that in a sense hasn't been fully worked out
yet: namely, th inking of homotopy types as fi
!
-groupoidsfl. The idea is this. An
fi
!
-categoryfl is something that has
267
 WEEK 98 FEBRUARY 27, 1997
Œ
objects like
x
Œ
morphisms between objects like
f
:
x
!
y
Œ
2
-morphisms between morphisms like
F
:
f
!
g
Œ
3
-morphisms between
2
-morphisms like
T
:
F
!
G
Œ
. . .
and so on ad innitum. There should be some ways of composing these, and these
should satisfy some axioms, and that of course is the tricky part. But the basic idea
is that if you hand me a topological space
X
, I can cook up an
!
-category whose
Œ
objects are points in
X
Œ
morphisms are paths between points in
X
Œ
2
-morphisms are continuous 1-parameter families of paths in
X
, i.e. fipaths of
pathsfl in
X
Œ
3
-morphisms are fipaths of paths of pathsfl in
X
Œ
. . .
and so on. This is better than your garden-variety
!
-category because all the mor-
phisms and
2
-morphisms and
3
-morphisms and so on have inverses, at least fiup to
homotopyfl. We call it an fi
!
-groupoidfl. This
!
-groupoid keeps track of the homo-
topy type of
X
in a very nice way. (If this fi
!
fl stuff is too mind-boggling, you may
want to start by reading a bit about plain old categories and groupoids in
 fiWeek
74fl
.)
Conversely, given any
!
-groupoid there should be a nice way to cook up a ho-
motopy corresponding to it. This is just the innite-dimensional generalization
of something I described in
 fiWeek 75fl
. There, I showed how you could get a
groupoid from a fihomotopy 1-typefl and vice versa. Here there are
1
-morphisms
but no interesting
2
-morphisms,
3
-morphisms, and so on, because the topology of
a fihomotopy 1-typefl is boring in dimensions greater than 1. (In case any experts
are reading this, what I mean is that its higher homotopy groups are trivial; its
higher homology and cohomology groups can be very interesting.)
So we can Š and should Š think of homotopy theory as, among other things, the
study of
!
-groupoids, and thus a very useful warmup to the study of
!
-categories.
In my occasional series on This Week's Finds called fithe Tale of
n
-Categoriesfl, I
have tried to explain why
n
-categories, and u ltimately
!
-categories, should serve
as a powerful unifying approach to lots of mathematics and physics. In trying to
understand this subject, I nd time and time again that homotopy theorists are the
ones to listen to.
Ł
 Chapter 2, fiHomotopy theories and model categoriesfl, by W. G. Dwyer and J.
Spalinski, is a nice introduction to the formal idea of using different fimodelsfl for
homotopy types. For example, above I was sketching how one might do homotopy
theory using the fimodel categoryfl of
!
-groupoids. Other model categories include
gadgets like Kan complexes, CW complexes, simplicial complexes, and so on.
268
 WEEK 98 FEBRUARY 27, 1997
Ł
 Chapter 6, fiModern foundations for stable homotopy theoryfl, by A. D. Elmendorf,
I. Kriz, M. Mandell and J. P. May describes a very nice approach to spectra. Loosely
speaking, we can think of a spectrum as a
Z
-groupoid, where
Z
denotes the in-
tegers. In other words, in addition to
j
-morphisms for all natural numbers
j
, we
also have
j
-morphisms for negative
j
! This may seem bizarre, but it's a lot like
how in homology theory one is interested in chain complexes that extend in both
the positive and negative directions. In fact, we can think of a chain complex as a
very special sort of
Z
-groupoid or spectrum. The study of spectra is called stable
homotopy theory.
Ł
 Chapter 13, fiStable homotopy and iterated loop spacesfl, by G. Carlsson and R. J.
Milgram, is packed with handy information about stable homotopy theory.
Ł
 Chapter 21, fiClassifying spaces of compact Lie groups and nite loop spacesfl, by
D. Notbohm, is a good source of heavy-duty information on classifying spaces of
your favorite Lie groups. To study vector bundles and the like one really needs
to become comfortable with classifying spaces, and I'm nally doing this, and I
hope eventually I'll be comfortable enough with them to really understand all these
results.
There is a lot more, but I will stop here.
269
 WEEK 99 MARCH 15, 1997
Week 99
March 15, 1997
Life here at the Center for Gravitational Physics and Geometry is tremendously exciting.
In two weeks I have to return to U. C. Riverside and my mundane life as a teacher
of calculus, but right now I'm still living it up. I'm working with Ashtekar, Corichi,
and Krasnov on computing the entropy of black holes using the loop representation of
quantum gravity, and also I'm talking to lots of people about an interesting
4
-dimensional
formulation of the loop representation in terms of fispin foamsfl Š roughly speaking,
soap-bubble-like structures with faces labelled by spins.
Here are some papers I've come across while here:
1)
 Lee Smolin, fiThe future of spin networksfl, in
The Geometric Universe: Science,
Geometry, and the Work of Roger Penrose
, eds. S. Hugget, Paul Tod, and L.J. Mason,
Oxford U. Press, Oxford, 1998. Also available as
gr-qc/9702030
.
I've spoken a lot about spin networks here on This Week's Finds. They were rst
invented by Penrose as a radical alternative to the usual way of thinking of space as a
smooth manifold. For him, they were purely discrete, purely combinatorial structures:
graphs with edges labelled by fispinsfl
j
= 0
;
1
=
2
;
1
;
3
=
2
; : : :
, and with three edges meeting
at each vertex. He showed how when these spin networks become sufciently large
and complicated, they begin in certain ways to mimic ordinary 3-dimensional Euclidean
space. Interestingly, he never got around to publishing his original paper on the subject:
2)
 Roger Penrose, fiTheory of quantized directionsfl, unpublished manuscript, avail-
able at
https://math.ucr.edu/home/baez/penrose/
.
Anyway, Smolin's paper is a kind of tribute to Penrose, and it traces the curiously twisting
history of spin networks from their origin up to the present day, where they play a
major role in topological quantum eld theory and the loop representation Š now more
appropriately called the spin network representation! Š of quantum gravity. (See
 fiWeek
55fl
 for more on spin networks.)
Note however that the title of the paper refers to the
future
of spin networks. Smolin
argues that spin networks are a major clue about the future of physics, and he paints a
picture of what this future might be... which I urge you to look at.
For more on this, try:
3)
 Fotini Markopoulou and Lee Smolin, fiCausal evolution of spin networksfl, available
as
gr-qc/9702025
.
Fotini Markopoulou is a student of Chris Isham at Imperial College, but now she's visiting
the CGPG and working with Lee Smolin on spin networks. In this paper they describe
some theories in which spin networks evolve in time in discrete steps. The evolution is
filocalfl in the sense that in a given step, any vertex of the spin network changes in a way
that only depends on its immediate neighbors Š vertices connected to it by an edge.
It is also ficausalfl in the sense that history of spin network evolving according to their
rules gives a causal set, i.e. a set equipped with a partial ordering which we think of as
270
 WEEK 99 MARCH 15, 1997
saying which points come fibeforefl which other points. This ties their work to the work
of Rafael Sorkin on causal sets, e.g.:
4)
 Luca Bombelli, Joohan Lee, David Meyer and Rafael D. Sorkin, fiSpace-time as a
causal setfl,
Phys. Rev. Lett.
59
(1987), 521.
Unlike the related work of Reisenberger and Rovelli (see
 fiWeek 96fl
), Markopolou
and Smolin do not attempt to fiderivefl their rules from general relativity by standard
quantization techniques. Instead, they hope that some theory of the sort they consider
will approximate general relativity in the large-scale limit. To check this will require
some new techniques akin to the firenormalization groupfl approach to studying the
large-scale limits of statistical mechanical systems dened on a lattice. This is a bit
daunting, but it seems likely that no matter how one proceeds to pursue a spin-network-
based theory of quantum gravity, one will need to develop such techniques at some
point.
Now I'd like to switch gears and return to...
THE TALE OF
n
-CATEGORIES!
Recall that in our last episode, in
 fiWeek 92fl
, we had worked our way up to
2
-
categories, and we were beginning to see what they had to do with
2
-dimensional physics
and topology. I described how to get monads from adjunctions, and what this has to do
with matrix multiplication, YangŒMills theory, and the 4-color theorem.
Next week I want to get serious and start talking about
n
-categories for arbitrary
n
.
One reason is that at the end of this month there's a conference on
n
-categories and
physics that I want to report on:
5)
Workshop on Higher Category Theory and Physics
, March 28-30, 1997, Northwest-
ern University, Evanston, Illinois. Organized by Ezra Getzler and Mikhail Kapranov.
But before doing this, I want to say a bit about what category theory has to do with
quantum mechanics!
First remember the big picture:
n
-category theory is a language to talk about pro-
cesses that turn processes into other processes. Roughly speaking, an
n
-category is some
sort of structure with objects, morphisms between objects,
2
-morphisms between mor-
phisms, and so on up to
n
-morphisms. A
0
-category is just a set, with its objects usually
being called fielementsfl. Things get trickier as
n
increases. For a precise denition of
n
-categories for
n
= 1
and
2
, see
 fiWeek 73fl
 and
 fiWeek 80fl
, respectively.
Most familiar mathematical gadgets are sets equipped with extra bells and whistles:
groups, vector spaces, Hilbert spaces, and so on all have underlying sets. This is why set
theory plays an important role in mathematics. However, we can also consider fancier
gadgets that are
categories
equipped with extra bells and whistles. Some of the most
interesting examples are just ficategoricationsfl of well-known gadgets.
For example, a fimonoidfl is a simple gadget, just a set equipped with an associative
product and multiplicative identity. An example we all know and love is the complex
271
 WEEK 99 MARCH 15, 1997
numbers: the product is just ordinary multiplication, and the multiplicative identity is
the number
1
.
We may categorify the notion of fimonoidfl and dene a fimonoidal categoryfl to be
a
category
equipped with an associative product and multiplicative identity. I gave the
precise denition back in
 fiWeek 89fl
; the point here is that while they may sound scary,
monoidal categories are actually very familiar. For example, the category of Hilbert
spaces is a monoidal category where the product of Hilbert spaces is the tensor product
and the multiplicative identity is
C
, the complex numbers.
If one systematically studies categorication one discovers an amazing fact: many
deep-sounding results in mathematics are just categorications of stuff we all learned in
high school. There is a good reason for this, I believe. All along, mathematicians have
been unwittingly fidecategorifyingfl mathematics by pretending that categories are just
sets. We fidecategorifyfl a category by forgetting about the morphisms and pretending
that isomorphic objects are equal. We are left with a mere set: the set of isomorphism
classes of objects.
I gave an example in
 fiWeek 73fl
. There is a category FinSet whose objects are nite
sets and whose morphisms are functions. If we decategorify this, we get the set of natural
numbers! Why? Well, two nite sets are isomorphic if they have the same number of
elements. fiCountingfl is thus the primordial example of decategorication.
I like to think of it in terms of the following fairy tale. Long ago, if you were a
shepherd and wanted to see if two nite sets of sheep were isomorphic, the most obvious
way would be to look for an isomorphism. In other words, you would try to match each
sheep in herd
A
with a sheep in herd
B
. But one day, along came a shepherd who
invented decategorication. This person realized you could take each set and ficountfl it,
setting up an isomorphism between it and some set of finumbersfl, which were nonsense
words like fione, two, three, four,...fl specially designed for this purpose. By comparing
the resulting numbers, you could see if two herds were isomorphic without explicitly
establishing an isomorphism!
According to this fairy tale, decategorication started out as the ultimate stroke of
mathematical genius. Only later did it become a matter of dumb habit, which we are
now struggling to overcome through the process of ficategoricationfl.
Okay, so what does this have to do with quantum mechanics?
Well, a Hilbert space is a set with extra bells and whistles, so maybe there is some
gadget called a fi2-Hilbert spacefl which is a
category
with analogous extra bells and
whistles. And maybe if we gure out this notion we will learn something about quantum
mechanics.
Actually the notion of 2-Hilbert space didn't arise in this simple-minded way. It arose
in some work by Daniel Freed on topological quantum eld theory:
5)
 Daniel Freed, fiHigher algebraic structures and quantizationfl,
Commun. Math.
Phys.
159
(1994), 343Œ398. Also available as
hep-th/9212115
; see also
 fiWeek
48fl
.
Later, Louis Crane adopted this notion as part of his program to reduce quantum gravity
to
n
-category theory:
6)
 Louis Crane: fiClock and category: is quantum gravity algebraic?fl,
Jour. Math.
Phys.
36
(1995), 6180Œ6193. Also available as
gr-qc/9504038
.
272
 WEEK 99 MARCH 15, 1997
These papers made is clear that 2-Hilbert spaces are interesting things and that one
should go further and think about fi
n
-Hilbert spacesfl for higher
n
, too. However, neither
of them gave a precise denition of 2-Hilbert space, so at some point I decided to do this.
It took a while for me to learn enough category theory, but eventually I wrote something
about it:
7)
 John Baez, fiHigher-dimensional algebra II: 2-Hilbert spacesfl,
Adv. Math.
127
(1997),
125Œ189. Also available as
q-alg/9609018
.
To understand this requires a little category theory, so let me explain the basic ideas here.
I'll concentrate on nite-dimensional Hilbert spaces, since the innite-dimensional
case introduces extra complications. To dene 2-Hilbert spaces we need to start by
categorifying the various ingredients in the denition of Hilbert space. These are:
1.
 the zero element,
2.
 addition,
3.
 subtraction,
4.
 scalar multiplication, and
5.
 the inner product.
The rst four have well-known categorical analogs. The fth one, which is really the
essence of a Hilbert space, may seem a bit more mysterious at rst, but as we shall see,
it's really the key to the whole business.
1)
 The analog of the zero vector is a `zero object'. A zero object in a category is an
object that is both initial and terminal. That is, there is exactly one morphism from
it to any object, and exactly one morphism to it from any object. Consider for
example the category
Hilb
having nite-dimensional Hilbert spaces as objects, and
linear maps between them as morphisms. In
Hilb
, any zero-dimensional Hilbert
space is a zero object.
Note: there isn't really a unique zero object in the fistrictfl sense of the term. In-
stead, any two zero objects are canonically isomorphic. The reason is that if you
have two zero objects, say
0
and
0
0
, there is a unique morphism
f
: 0
!
0
0
and a
unique morphism
g
: 0
0
!
0
. These morphisms are inverses of each other so they
are isomorphisms. Why are they inverses? Well,
f g
: 0
!
0
0
must be the identity
morphism
1
0
: 0
!
0
, because there is only one morphism from
0
to
0
! Similarly,
g f
is the identity on
0
0
. (Note that I am using category theorist's notation, where
the composite of
f
:
x
!
y
and
g
:
y
!
z
is denoted
f g
:
x
!
z
.)
This is typical in category theory. We don't expect stuff to be unique; it should only
be unique up to a canonical isomorphism.
2)
 The analog of adding two vectors is forming the ficoproductfl of two objects. Co-
products are just a fancy way of talking about direct sums. Any decent quantum
mechanic knows about the direct sum of Hilbert spaces. But in fact, we can de-
ne this notion very generally in any category, where it goes under the name of a
273
 WEEK 99 MARCH 15, 1997
ficoproductfl. (I give the denition below; if I gave it here it would scare people
away.) As with zero objects, coproducts are typically not unique, but they are al-
ways unique up to canonical isomorphism, which is what matters. It's a good little
exercise to show this.
3)
 The analog of subtracting vectors is forming the ficokernelfl of a morphism
f
:
x
!
y
. If
x
and
y
are Hilbert spaces, the cokernel of
f
is just the orthogonal complement
of the range of
f
. In other words, for Hilbert spaces we have fidirect differencesfl as
well as direct sums. However, the notion of cokernel makes sense in any category
with a zero object. I won't burden you with the precise denition here.
An important difference between zero, addition and subtraction and their categorical
analogs is that these operations represent extra
structure
on a set, while having a zero
object, coproducts of two objects, or cokernels of morphisms is merely a
property
of a
category. Thus these concepts are in some sense more intrinsic to categories than to sets.
On the other hand, we've seen one pays a price for this: while the zero element, sums,
and differences are unique in a Hilbert space, the zero object, coproducts, and cokernels
are typically unique only up to canonical isomorphism.
4)
 The analog of multiplying a vector by a complex number is tensoring an object
by a Hilbert space. Besides its additive properties (zero object, binary coproducts,
and cokernels),
Hilb
is also a monoidal category: we can multiply Hilbert spaces by
tensoring them, and there is a m ultiplicative identity, namely the complex numbers
C
. In fact,
Hilb
is a firing categoryfl, as dened by Laplaza and Kelly.
We expect
Hilb
to play a role in 2-Hilbert space theory analogous to the role played by
the ring
C
of complex numbers in Hilbert space theory. Thus we expect 2-Hilbert spaces
to be fimodule categoriesfl over
Hilb
, as dened by Kapranov and Voevodsky.
An important part of our philosophy here is that
C
is the primordial Hilbert space:
the simplest one, upon which the rest are modelled. By analogy, we expect
Hilb
to
be the primordial 2-Hilbert space. This is part of a general pattern pervading higher-
dimensional algebra; for example, there is a sense in which the
(
n
+ 1)
-category of all
(small)
n
-categories,
n
Cat
, is the primordial
(
n
+ 1)
-category. The real signicance of
this pattern remains mysterious.
5)
 Finally, what is the categorication of the inner product in a Hilbert space? It's the
`
Hom
functor'! The inner product in a Hilbert space eats two vectors
v
and
w
and
spits out a complex number
h
v ; w
i
Similarly, given two objects
v
and
w
in a category, the
Hom
functor gives a
set
Hom(
x; y
)
namely the set of morphisms from
x
to
y
. Note that the inner product
h
v ; w
i
is
linear in
w
and conjugate-linear in
y
, and similarly, the
Hom
functor
Hom(
x; y
)
is
covariant in
y
and contravariant in
x
. This hints at the category theory secretly
underlying quantum mechanics. In quantum theory the inner product
h
v ; w
i
repre-
sents the
amplitude
to pass from
v
to
w
, while in category theory
Hom(
x; y
)
is the
274
 WEEK 99 MARCH 15, 1997
set
of ways to get from
x
to
y
. In Feynman path integrals, we do an integral over
the set of ways to get from here to there, and get a number, the amplitude to get
from here to there. So when physicists do Feynman path integration Š just like a
shepherd counting sheep Š they are engaged in a process of decategorication!
To understand this analogy better, note that any morphism
f
:
x
!
y
in
Hilb
can be
turned around or fidualizedfl to obtain a morphism
f

:
y
!
x
. This is usually called the
fiadjointfl of
f
, and it satises
h
f v ; w
i
=
h
v ; f

w
i
for all
v
in
x
, and
w
in
y
. This ability to dualize morphisms is crucial to quantum theory.
For example, observables are represented by self-adjoint morphisms, while symmetries
are represented by unitary morphisms, whose adjoint equals their inverse.
However, it should now be clear Š at least to the categorically minded Š that this
sort of adjoint is just a decategoried version of the fiadjoint functorsfl so important in
category theory. As I explained in
 fiWeek 79fl
, a functor
F

:
D ! C
is a firight adjointfl of
F
:
C ! D
if there is, not an equation, but a natural isomorphism
Hom(
F c; d
)
˘
=
Hom(
c; F

d
)
for all objects
c
in
C
, and
d
2 D
.
Anyway, in the paper I proceed to use these ideas to give a precise denition of 2-
Hilbert spaces, and then I prove all sorts of stuff which I won't describe here.
Let me wrap up by explaining the denition of ficoproductfl. This is one of those
things they should teach all math grad students, but for some reason they don't. It's a
bit dry but it'll be good for you. A coproduct of the objects
x
and
y
is an object
x
+
y
equipped with morphisms
i
:
x
!
x
+
y
and
j
:
y
!
x
+
y
that is universal with respect to this property. In other words, if we have any
other
object,
say
z
, and morphisms
i
0
:
x
!
z
and
j
0
:
y
!
z
then there is a unique morphism
f
:
x
+
y
!
z
such that
i
0
=
if
and
j
0
=
j f :
This kind of denition automatically implies that the coproduct is unique up to canonical
isomorphism. To understand this abstract nonsense, it's good to check that the coproduct
of sets or topological spaces is just their disjoint union, while the coproduct of vector
spaces or Hilbert spaces is their direct sum.
To continue reading the fiTale of
n
-Categoriesfl, see
 fiWeek 100fl
.
275
 WEEK 100 MARCH 23, 1997
Week 100
March 23, 1997
Pretty much ever since I started writing fiThis Week's Findsfl I've been trying to get folks
interested in
n
-categories and other aspects of higher-dimensional algebra. There is
really an enormous world out there that only becomes visible when you break out of
filinear thinkingfl Š the mental habits that go along with doing math by writing strings
of symbols in a line. For example, when we write things in a line, the sums
a
+
b
and
b
+
a
look very different. Then we introduce a profound and mysterious equation, the
ficommutative lawfl:
a
+
b
=
b
+
a
which says that actually they are the same. But in real life, we prove this equation using
higher-dimensional reasoning:
a
+
b
=
a
+
b
=
a
+
b
=
b
+
a
=
b
+
a
If this seems silly, think about explaining to a kid what
9 + 17
means, and how you could
prove that
9 + 17 = 17 + 9
. You might take a pile of 9 rocks and set it to the left of a
pile of 17 rocks, and say fithis is 9+17 rocksfl. Alternatively, you might put the pile of 9
rocks to the right of the pile of 17 rocks, and say fithis is 17+9 rocksfl. Thus to prove that
9 + 17 = 17 + 9
, you would simply need to
switch
the two piles by moving one around
the other.
This is all very simple. Historically, however, it took people a long time to really
understand. It's one of those things that's too simple to take seriously until it turns out
to have complicated ramications. Now it goes by the name of the fiEckmannŒHilton
theoremfl, which says that fia monoid object in the category of monoids is a commutative
monoidfl. You practically need a PhD in math to understand
that
! However, lest you
think that Eckmann and Hilton were merely dressing up the obvious in fancy jargon, it's
important to note that what they did was to gure out a
framework
that turns the above
fipicture proof fl that
a
+
b
=
b
+
a
into an actual rigorous proof! This is one of the goals
of higher-dimensional algebra.
The above proof that
a
+
b
=
b
+
a
uses
2
-dimensional space, but if you really think
about it also uses a 3rd dimension, namely time: the time that passes as you move fi
a
fl
around fi
b
fl. If we draw this 3rd dimension as space rather than time we can visualize the
process of moving
a
around
b
as follows:
a
b
a
b
This picture is an example of what mathematicians call a fibraidfl. This particular one is
a boring little braid with only two strands and one place where the two strands cross.
276
 WEEK 100 MARCH 23, 1997
It illustrates another major idea behind higher-dimensional algebra: equations are best
thought of as summarizing fiprocessesfl (or technically, fiisomorphismsfl). The equation
a
+
b
=
b
+
a
is a summary of the process of switching
a
and
b
. There is more information
in the process than in the mere equation
a
+
b
=
b
+
a
, because in fact there are two
different
ways to switch
a
and
b
: the above way and
a
b
a
b
If one has a bunch of objects one can switch them around in a lot of ways, getting lots of
different braids.
In fact, the mathematics of braids, and related things like knots, is crucially impor-
tant for understanding quantum gravity in
3
-dimensional spacetime. Spacetime is really
4
-dimensional, of course, but quantum gravity in
4
-dimensional spacetime is awfully dif-
cult, so in the late 1980s people got serious about studying
3
-dimensional quantum
gravity as a kind of warmup exercise. It turned out that the math required was closely
related to some mysterious new mathematics related to knots and fibraidingsfl. At rst
this must sound bizarre: a deep relationship between knots and
3
-dimensional quan-
tum gravity! However, after you ght your way through the sophisticated mathematical
physics that's involved, it becomes clear why they are related: both rely crucially on
fi3-dimensional algebrafl, the algebra describing how you can move things around in
3
-dimensional spacetime.
However, there is more to the story, because knot theory also seems deeply related
to
4
-dimensional
quantum gravity. Here the knots arise as fiux tubes of areafl living in
3
-dimensional space at a given time. Recent work on quantum gravity suggests that as
time passes these knots (or more generally, fispin networksfl) move around and change
topology as time passes.
To really understand this, we probably need to understand fi4-dimensional algebrafl.
Unfortunately, not enough is known about 4-dimensional algebra. The problem is that
we don't know much about 4-categories! To do
n
-dimensional algebra in a really nice
way, you need to know about
n
-categories. Roughly speaking, an
n
-category is an al-
gebraic structure that has a bunch of things called fiobjectsfl, a bunch of things called
fimorphismsfl that go between objects, and similarly
2
-morphisms going between mor-
phisms,
3
-morphisms going between
2
-morphisms, and so on up to the number
n
. You
can think of the objects as fithingsfl of whatever sort you like, the morphisms as processes
going from one thing to another, the
2
-morphisms as meta-processes going from one
process to another, and so on. Depending on how you play the
n
-category game, there
are either no morphisms after level
n
, or only simple and bland ones playing the role
of fiequationsfl. The idea is that in the world of
n
-categories, one keeps track of things,
processes, meta-processes, and so on to the
n
th level, but after that one calls it quits and
uses equations.
277
 WEEK 100 MARCH 23, 1997
So what is the denition of
4
-categories? Well, Eilenberg and Mac Lane dened
1
-categories, or simply ficategoriesfl, in a paper that was published in 1945:
1)
 Samuel Eilenberg and Saunders Mac Lane, fiGeneral theory of natural equiva-
lencesfl,
Trans. Amer. Math. Soc.
58
(1945), 231Œ294.
B
´
enabou dened
2
-categories Š though actually he called them fibicategoriesfl Š in a
1967 paper:
2)
 Jean B
´
enabou,
Introduction to Bicategories
, Springer Lecture Notes in Mathematics
47
, New York, 1967, pp. 1Œ77.
Gordon, Power, and Street dened
3
-categories Š or actually fitricategoriesfl Š in a
paper that came out in 1995:
3)
 Rorbert Gordon, A. John Power, and Ross Street, fiCoherence for tricategoriesfl,
Memoirs Amer. Math. Soc.
117
(1995).
This step took a long time in part because it took a long time for people to understand
deeply where
braidings
t into the picture.
But what about
4
-categories and higher
n
? Well, the history is complicated and I
won't get it right, but let me say a bit anyway. First of all, there are some things called
fistrict
n
-categoriesfl that people have known how to dene for arbitrarily high
n
for quite
a while. In fact, people know how to go up to innity and dene fistrict
!
-categoriesfl;
see for example:
4)
 Sjoerd E. Crans,
On combinatorial models for higher dimensional homotopies
, Ph.D. the-
sis, University of Utrecht, Utrecht, 1991.
Strict
n
-categories are quite interesting and important, but I'm mainly mentioning them
here to emphasize that they are
not
what I'm talking about. People sometimes often
call strict
n
-categories simply fi
n
-categoriesfl, and call the more general
n
-categories I'm
talking about above fiweak
n
-categoriesfl. However, I think the weak
n
-categories will
eventually be called simply fi
n
-categoriesfl, because they are far more interesting and
important than the strict ones. Anyway, that's what I'm doing here.
Secondly, when you dene
n
-categories you have to make some choice about the
fishapesfl of your
j
-morphisms. In general they should be some
j
-dimensional things, but
they could be simplices, or cubes, or other shapes. In some ways the simplest shapes are
figlobesfl, a
j
-dimensional globe being a
j
-dimensional ball with its boundary divided into
two hemispheres, the fiinfacefl and fioutfacefl, which are themselves
(
j

## Document: electromagnetic_engineering ##

material:
 
d
e
c
q
n
v
J
=
 
s
 = 
conductivity of the material 
[
S/m
]
 
E
 = 
electric field [
V
/
m
]
 
I
 = current [
A
]
 
d
s
 = 
a small increment of surface 
S
 
n
c
 = 
the number of conduction band 
electrons
 
q
e
 = 
electron charge 
-
1.602×10
-
19
 
C
 
v
d
 = 
a small increment of surface 
S
 
 
 Tom Penick    tom@tomzap.com    www.teicontrol
s.com/notes    
10/22/2000
   
Page 
8
 of 
13
 
CONTINUITY EQUATION
 
0
·
=
¶
r
¶
+
Ñ
t
J
 
J
 = 
current de
nsity [
A/m
2
] 
E
J
s
=
 
r
 =
 volume charge density 
[
C
/
m
3
]
 
 
DUALITY RELATIONSHIP of 
J
 and 
D
 
RESISTANCE, CAPACITANCE, CURRENT, 
CONDUCTIVITY
 
Where current enters and leaves a condu
cting 
medium via two perfect conductors (electrodes) we 
have:
 
e
s
=
e
s
=
s
=
=
ò
ò
ò
Q
d
d
d
I
S
S
S
s
D
s
E
s
J
·
·
·
 
J
 = 
current density [
A/m
2
] 
E
J
s
=
 
E
 = 
electric field [
V
/
m
] 
 
D
 = electric flux density vector [
C
/
m
2
] 
E
D
e
=
 
As a result of this, we have 
the following relation, 
useful in finding the resistance between two 
conductors:
 
s
e
=
RC
 
R
 = resistance [
W
]
 
C
 = capacitance [
F
]
 
e
 = 
permittivity of the material
 
s
 = 
conductivity of the material 
[
S/m
]
 
 
G
  
CONDUCTANCE
  
[
W
-1
]
 
DF
=
=
I
R
G
1
 
ò
ò
-
+
s
=
l
E
s
E
d
d
S
·
·
 
R
 = resistance [
W
]
 
I
 = current [
A
]
 
DF
 = 
voltage potential 
[
V
]
 
s
 = 
co
nductivity of the material 
[
S/m
]
 
 
s
s
  
SEMICONDUCTOR CONDUCTIVITY
  
[
W
-1
]
 
d
e
N
q
m
»
s
 
 
s
 = 
conductivity of the material 
[
S/m
]
G
 = conductance [
W
-1
]
 
q
 = 
electron charge 
-
1.602×10
-
19
 
C
 
m
e
 = 
electron mobility 
[
m
2
/(
V
-
s)
]
 
N
d
 = 
concentration of donors, and 
thereby the electron concentration 
in the transition region 
[
m
-
3
]
 
 
MATHEMATICS
 
WORKING WITH LINES, SURFACES, AND 
VOLUMES
 
r
l
(
r
'
)
 means "the charge density along line 
l
 as a 
function of 
r
'
."  This might be a value in C/m or it 
could be a function.  Similarly, 
r
s
(
r
'
)
 would be the 
charge density of a surface and 
r
v
(
r
'
)
 is the 
charge density of a volume.  
 
For example, a disk of r
adius 
a
 having a uniform 
charge density of 
r
 C/m
2
, would have a total 
charge of 
rp
a
2
, but to find its influence on points 
along the central axis we might consider 
incremental rings of the charged surface as 
r
s
(
r
'
)
 
dr'
=
 
r
s
2
p
r'
 
dr'
.
 
If 
d
l
'
 refers to an incre
mental distance along a circular 
contour 
C
, the expression is 
r
'
d
f
f
, where 
r
'
 is the 
radius and 
d
f
f
 is the incremental angle.
 
 
GEOMETRY
 
SPHERE
 
Area 
2
4
r
A
p
=
 
Volume 
3
3
4
r
V
p
=
 
ELLIPSE
 
Area 
AB
A
p
=
 
Circumference 
2
2
2
2
b
a
L
+
p
»
 
 
Ñ  
Ñ  
NABLA, 
DEL OR 
GRAD OPERATOR
   
[
+
 
m
-
1
]
 
Compare the 
Ñ
 operation to taking the ti
me 
derivative.  Where 
¶
/
¶
t
 means to take the derivative 
with respect to time and introduces a 
s
-
1
 component to 
the units of the result, the 
Ñ
 operation means to take 
the derivative with respect to distance (in 3 
dimensions) and introduces a 
m
-
1
 component t
o the 
units of the result.  
Ñ
 terms may be called 
space 
derivatives
 
and an equation which contains the 
Ñ
 
operator may be called a 
vector differential 
equation
. 
 In other words  
Ñ
A
 is how fast 
A
 
changes 
as you move through space.
 
in rectangular 
coordinates:
 
‹‹
‹
AAA
xyz
xyz
¶¶¶
Ñ
=++
¶¶¶
A
 
in cylindrical 
coordinates:
 
1
‹
‹
‹
A
AA
rz
r
rz
¶
¶¶
Ñ
=
+
f+
¶
¶
f¶
A
 
in spherical 
coordinates:
 
11
‹‹
‹
sin
A
AA
r
r
rr
¶
¶¶
Ñ
=
+
q
+f
¶
¶
q
q
¶f
A
 
 
 Tom Penick    tom@tomzap.com    www.teicontrol
s.com/notes    
10/22/2000
   
Page 
9
 of 
13
 
Ñ
Ñ
2
  
THE LAPLACIAN
   [
+
 
m
-
2
]
 
 
in 
rectangular
 
coordinates:
 
0
‹
‹
‹
2
2
2
2
=
Ñ
+
Ñ
+
Ñ
=
Ñ
z
y
x
A
A
A
z
y
x
A
 
0
2
2
2
2
2
2
2
=
¶
¶
+
¶
¶
+
¶
¶
º
Ñ
z
y
x
 
in 
spherical
 and 
cylindrical
 
coordinates:
 
(
)
(
)
(
)
A
A
A
A
A
curl
curl
div
grad
·
2
-
=
´
Ñ
´
Ñ
-
Ñ
Ñ
º
Ñ
 
for example, 
the 
Laplacian of electro
-
static potential:
 
0
2
2
2
2
2
2
2
=
¶
F
¶
+
¶
F
¶
+
¶
F
¶
=
F
Ñ
z
y
x
 
 
Ñ
Ñ
·
   
DIVERGENCE
   [
+
 
m
-
1
]
 
The del operator followed by the dot product operator 
is read as
 
"the divergence of" and is an operation 
performed on a vector.  In rectangular coordinates, 
Ñ×
 
means the sum of the partial derivatives of the 
magnitudes in the 
x
, 
y
, and 
z
 directions with respect to 
the 
x
, 
y
, and 
z
 va
riables.  The result is a scalar, and a 
factor of m
-
1
 is contributed to the units of the result.
 
For example, in this form of Gauss' law, where 
D
 is a 
density per unit area, 
Ñ×
D
 becomes a density per unit 
volume.
 
div
y
x
z
D
D
D
xyz
¶
¶
¶
=Ñ
×
=++
=r
¶¶¶
DD
 
D
 =
 electric fl
ux density vector  
D
 
=
 
e
E
  
[
C/m
2
]
 
r
 = source charge density
 
[
C/m
3
]
 
In the electrostatic context, the divergence of 
D
 is the 
total outward flux per unit volume due to a source 
charge.  The divergence of vector 
D
 is:
 
in 
rectangular
 
coordinates:
 
z
D
y
D
x
D
z
y
x
¶
¶
+
¶
¶
+
¶
¶
=
D
div
 
in 
cylindrical
 
coordinates:
 
(
)
z
D
D
r
rD
r
r
z
r
¶
¶
+
f
¶
¶
+
¶
¶
=
f
1
1
div
D
 
in 
spherical
 coordinates:
 
(
)
(
)
f
¶
¶
q
+
q
¶
q
¶
q
+
¶
¶
=
f
q
D
r
D
r
r
D
r
r
r
sin
1
sin
sin
1
1
div
2
2
D
 
 
Ñ
Ñ
×
   
CURL
   [
+
 
m
-
1
]
 
The circulation around an enclosed area.  The curl
 of 
vector 
B
 is
 
in 
rectang
ular
 coordinates:
 
curl
‹‹
‹
yy
xx
zz
BB
BB
BB
xyz
y
z
z
x
xy
=Ñ
´=
¶¶
ae
ö
aeö
¶¶
¶¶
aeö
-
+
-
+-
ç
÷
ç÷
ç÷
¶
¶
¶
¶
¶¶
èø
è
ø
èø
BB
 
in 
cylindrical
 coordinates:
 
(
)
curl
11
‹
‹
‹
z
r
zr
rB
B
B
B
BB
rz
r
z
z
r
rr
f
f
=Ñ
´=
éù
¶
¶
éù
¶
¶
¶¶
éù
-
+
f
-
+-
êú
êú
êú
¶
f
¶
¶
¶
¶
¶f
ëû
ëû
êú
ëû
BB
 
in 
spherical
 coordinates:
 
(
)
(
)
(
)
sin
1
‹
curl
sin
1
11
‹‹
sin
rr
B
B
r
r
rB
rB
BB
r
r
rr
f
q
f
q
éù
¶q
¶
=Ñ
´
=
-+
êú
q
¶
q
¶f
êú
ëû
éù
¶
¶
éù
¶¶
q
-
+
f-
êú
êú
q
¶
f
¶
¶
¶q
êú
ëû
ëû
BB
 
The 
divergence of a curl
 is always zero:
 
 
(
)
0
·
=
´
Ñ
Ñ
H
 
 
DOT PRODUCT
   [
=
 
units
2
]
 
The dot product
 is a scalar value.
 
(
)
(
)
z
z
y
y
x
x
z
y
x
z
y
x
B
A
B
A
B
A
B
B
B
A
A
A
+
+
=
+
+
+
+
=
z
y
x
z
y
x
B
A
‹
‹
‹
Ł
‹
‹
‹
Ł
 
AB
cos
Ł
y
=
B
A
B
A
 
0
‹
Ł
‹
=
y
x
,  
1
‹
Ł
‹
=
x
x
 
(
)
y
z
y
x
B
B
B
B
=
+
+
=
y
z
y
x
y
B
‹
Ł
‹
‹
‹
‹
Ł
 
y
B
A
AŁB
 
Projection
 of 
B
 
along 
â
:
 
(
)
a
a
B
‹
‹
Ł
 
B
y
â
 
â
y
B
 
The dot product of 90° vectors is zero.
 
The dot product is 
commutative
 and 
distributive
:
 
A
B
B
A
Ł
Ł
=
 
(
)
C
A
B
A
C
B
A
Ł
Ł
Ł
+
=
+
 
 
 Tom Penick    tom@tomzap.com    www.teicontrol
s.com/notes    
10/22/2000
   
Page 
10
 of 
13
 
CROSS PRODUCT
 
(
)
(
)
(
)
(
)
(
)
x
y
y
x
z
x
x
z
y
z
z
y
z
y
x
z
y
x
B
A
B
A
B
A
B
A
B
A
B
A
B
B
B
A
A
A
-
+
-
+
-
=
+
+
´
+
+
=
´
z
y
x
z
y
x
z
y
x
B
A
‹
‹
‹
‹
‹
‹
‹
‹
‹
 
AB
sin
‹
y
=
´
B
A
n
B
A
 
where 
n
‹
 is the unit vector normal to 
both 
A
 and 
B
 (thumb of right
-
hand rule).
 
B
A
A
B
´
-
=
´
 
z
y
x
=
´
 
z
x
y
-
=
´
 
0
=
´
x
x
 
f
´=
zr
 
f
´
=-
rz
 
The cross product is 
distributive:
 
(
)
C
A
B
A
C
B
A
´
+
´
=
+
´
 
Also, we have:
 
(
)
(
)
(
)
´
´=
×
-×
A
B
C
AC
B
ABC
 
n
y
A×B
A
B
 
 
COORDINATE SYSTEMS
 
Cartesian or Rectangular Coordinates:
 
‹‹
‹
(
,,)
xy
z
x
x
y
y
zz
=++
r
 
‹
x
 is a unit vector
 
2
2
2
z
y
x
+
+
=
r
 
Spherical Coordinates:
 
)
,
,
(
f
q
r
P
 
r
 is distance from center
 
 
q
 is angle from vertical
 
 
f
 is the CCW angle from the 
x
-
axis
 
‹
r
, 
‹
q
, and 
‹
f
 are unit vectores and are functions 
of 
position
Š
their orientation depends on where they 
are located.
 
Cylindrical Coordinates:
 
)
,
,
(
z
r
f
C
 
r
 is distance from the vertical (
z
) axis
 
 
f
 is the CCW angle from the 
x
-
axis
 
 
z
 is the vertical distance from origin
 
 
 
COORDINATE TRANSFORMATIONS
 
Rectangular to Cylindrical:
 
To obtain: 
‹
‹
‹
(
,,)
rz
rz
r
A
A
zA
f
f
=
+
f+
A
 
2
2
y
x
A
r
+
=
 
‹
‹‹
co
s
sin
r
xy
=
f
+f
 
x
y
1
tan
-
=
f
 
‹
‹‹
si
n
cos
xy
f=
-
f
+f
 
z
z
=
 
‹‹
zz
=
 
Cylindric
al to Rectangular:
 
To obtain: 
‹‹
‹
(
,,)
xy
z
x
x
y
y
zz
=++
r
 
f
=
cos
r
x
 
‹
‹‹
co
s
cos
xr
=
f-
ff
 
f
=
sin
r
y
 
‹
‹‹
si
n
cos
ry
f
=
f
+f
 
z
z
=
 
‹‹
zz
=
 
Rectangular to Spherical:
 
To obtain: 
‹‹
‹
(
,,)
r
r
r
AAA
qf
q
f
=
+
q
+f
A
 
2
2
2
z
y
x
A
r
+
+
=
‹
‹‹
‹
si
n
co
s
si
n
si
n
cos
r
x
yz
=
q
f
+
q
f
+q
 
2
2
2
1
cos
z
y
x
z
+
+
=
q
-
‹
‹‹
‹
co
s
co
s
co
s
si
n
sin
x
yz
q
=
q
f
+
q
f
-q
 
x
y
1
tan
-
=
f
 
‹
‹‹
si
n
cos
xy
f=
-
f
+f
 
Spherical to Rectangular:
 
To obtain: 
‹‹
‹
(
,,)
xy
z
x
x
y
y
zz
=++
r
 
f
q
=
cos
sin
r
x
‹‹
‹‹
si
n
co
s
co
s
co
s
sin
xr
=
q
f-
qq
f-
ff
 
f
q
=
sin
sin
r
y
‹‹
‹‹
si
n
si
n
co
s
si
n
cos
yr
=
q
f+
q
q
f+
ff
 
q
=
cos
r
z
 
‹
‹
‹
co
s
sin
zr
=
q-
qq
 
 
 
 Tom Penick    tom@tomzap.com    www.teicontrol
s.com/notes    
10/22/2000
   
Page 
11
 of 
13
 
THE STATIC MAGNETIC FIELD
 
F
  
F
12
  
MAGNETIC FORCE
  
[
N/m
]
 
due to a conductor
 
If the current
 in the two wires travels in opposite 
directions, the force will be attractive.
 
d
I
I
p
m
=
2
‹
2
1
0
12
x
F
 
F
12
 = the force exerted
 
by
 conductor 1 
carrying current 
I
 
on
 conductor 2. 
[
N/m
]
 
m
0
 
= permeability constant 4
p
×10
-
7
 
[
H/m
]
 
I
 
= current [A]
 
d
 = distance b
etween conductors [m]
 
 
B
P
  
BIOT
-
SAVART LAW
 
Determines the 
B
 field vector at any point 
P
 identified 
by the position vector 
r
, due to a differential current 
element 
I d
l
'
 located at vector 
r'
.
 
2
0
4
‹
'
R
d
I
d
P
p
´
m
=
R
l
B
 
(
)
ò
-
-
´
p
m
=
C
P
d
I
3
0
'
'
'
4
r
r
r
r
l
B
 
'
'
‹
r
r
r
r
R
-
-
=
 
B
P
 = magnetic field vector
 
[
T
]
 
m
0
 
= permeability constant 
4
p
×10
-
7
 [
H/m
]
 
I
 
d
l
'
 
= current element [
A
]
 
R
‹
 = unit vector pointing 
from the current 
element to point 
P
 
R
 
= distance between the 
current element and 
point 
P
 [
m
]
 
 
B
  
AMPERE'S CI
RCUITAL LAW
 
Ampere's law is a consequence of the 
Biot
-
Savart 
law
 and serves the same purpose as 
Gauss's law
.  
Ampere's law states that the line integral of 
B
 around 
any closed contour is equal to 
m
0
 times the total net 
current 
I
 passing through the surface
 
S
 enclosed by 
the contour 
C
.  This law is useful in solving 
magnetostatic problems having some degree of 
symmetry.
 
I
d
d
S
C
0
0
·
·
m
=
m
=
ò
ò
s
J
l
B
 
B
 = magnetic field vector, equal to 
B
 times the appropriate unit
 
vector [
T
]
 
m
0
 
= permeability constant 4
p
×10
-
7
 
[
H/m
]
 
d
l
 
= an increment of the line which 
is the perimeter of contour 
C
 
[
m
]
 
J
 = 
current density [
A/m
2
] 
E
J
s
=
 
d
s
 
= an increment of surface [
m
2
]
 
 
B
  
MAGNETIC FIELD
  
[
T 
or
 A/m
]
 
due to
 an infinite straight conductor
 
May also be applied to the magnetic field
 close to a 
conductor of finite length.
 
0
‹
2
P
I
r
m
=f
p
B
 
B
P
 = magnetic field vector [
T
]
 
m
0
 
= permeability constant 4
p
×10
-
7
 [
H/m
]
 
I
 
= current [
A
]
 
r
 = perpendicular distance from the 
conductor [
m
]
 
 
B
  
MAGNETIC FIELD
  
[
T
]
 
due to a finite straight conductor at a point 
perpendicular to the
 midpoint
 
0
22
‹
2
P
Ia
r
ra
m
=f
p+
B
 
a
r
I
 
B
P
 = magnetic field vector [
T
]
 
m
0
 
= permeability constant 
4
p
×10
-
7
 [
H/m
]
 
I
 
= current [
A
]
 
a
 
= half the length of the 
conductor [
m
]
 
r
 = perpendicular distance 
from the conductor [
m
]
 
 
B
   
MAGNETIC FIELD
  
[
T
]
 
at the center of a circular wire of 
N
 turns
 
a
NI
B
ctr
2
‹
0
m
=
z
 
B
 = magnetic field [
T
]
 
m
0
 
= permeability const. 4
p
×10
-
7
 [
H/m
]
 
N
 = number of turns of the coil
 
I
 
= current [
A
]
 
a
 = radius [
m
]
 
 
B
   
MAGNETIC FIELD
  
[
T
]
 
along the central axis of a solenoid
 
(
)
(
)
(
)
(
)
(
)
ú
ú
û
ù
ê
ê
ë
é
-
+
-
-
+
+
+
m
=
2
2
2
2
0
2
/
2
/
2
/
2
/
2
‹
l
z
a
l
z
l
z
a
l
z
l
NI
z
B
z
 
and at the center of the coil:  
l
NI
B
ctr
0
‹
m
»
z
 
B
 = magnetic field [
T
]
 
m
0
 
= permeability constant 
4
p
×10
-
7
 [
H/m
]
 
N
 = number of turn
s
 
I
 
= current [
A
]
 
l
 
= length of the solenoid [
m
]
 
z
 
= distance from center of 
the coil [
m
]
 
a
 = coil radius [
m
]
 
 
 Tom Penick    tom@tomzap.com    www.teicontrol
s.com/notes    
10/22/2000
   
Page 
12
 of 
13
 
H
   
MAGNETIC FIELD INTENSITY
  
[
A/m
]
 
The
 magnetic field intensity vector
 is directly 
analogous to the 
electric f
lux density vector
 
D
 in 
electrostatics in that both 
D
 and 
H
 are medium
-
independent and are directly related to their sources.
 
M
B
H
-
m
º
0
 
t
¶
¶
+
=
´
Ñ
D
J
H
 
H
 = magnetic field [
A/m
]
 
B
 = magnetic field vector [
T
]
 
m
0
 
= permeability const. 4
p
×10
-
7
 [
H/m
]
 
M
 = magnetization [
A/m
]
 
J
 = 
current density [
A/m
2
] 
E
J
s
=
 
D
 = electric flux density vector 
[
C
/
m
2
]
 
 
Y, L
Y, L
 
(,lambda)
  
MAGNETIC FLUX, 
LINKAGE
 
Flux linkage 
L
 is the a
bility of a closed circuit to 
store 
magnetic energy
.  It depends, in part, on the 
physical layout of the conductors.  It is the total 
magnetic field due to circuit #1 passing through the 

## Document: hopf_algebras ##

x
The set of all such elements in a Hopf algebra form a Lie algebra with commutator
as Lie bracket. That is,
[
x; y
] =
¹
(
x
