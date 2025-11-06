op
, the opposite of
C
, which has the same objects as
C
, and has the arrows in
C
turned around backwards.
In other words, a morphism
f
:
x
!
y
in
C
op
is dened to be a morphism
f
:
y
!
x
in
C
,
and the composite
f g
of morphisms in
C
op
is dened to be their composite
g f
in
C
. So
C
op
is like a through-the-looking-glass version of
C
where they do everything backwards.
A functor
F
:
C
op
! D
is also called a ficontravariantfl functor from
C
to
D
, since we can
think of it as a screwy functor from
C
to
D
with
F
(
f g
) =
F
(
g
)
F
(
f
)
instead of the usual
F
(
f g
) =
F
(
f
)
F
(
g
)
. Whenever you see this perverse contravariant behavior going on,
you should suspect an opposite category is to blame.
Now, it turns out that we can think of the fi
Hom
fl in a category
C
as a functor
Hom(

of quantum theory more clear,
and hopefully more plausible. If we have states
h
and
h
0
in a Hilbert space,
h
h; h
0
i
keeps
track of the
amplitude
of getting from
h
to
h
0
. (Often people will say fifrom
h
0
to
h
fl, but
here I think I really want to go the other way.) This is a mere
number
. If we have objects
c
and
c
0
in a category,
Hom(
c; c
0
)
is the actual
set
of ways to get from
c
to
c
0
, that is, the
set of morphisms from
c
to
c
0
.
When one computes transition amplitudes by summing over paths, as in Feynman
path integrals, one is in a sense decategorifying, that is, turning a set of ways to get
from here to there into a number, the transition amplitude. However, one is not just
counting the ways, one is counting them fiwith phasefl. . . . and I must admit that the role
of the
complex numbers
in quantum theory is still puzzling from this viewpoint. For some
food for thought, you might want to check out Dan Freed's work on torsors, which are a
categoried version of phases:
1)
 fiHigher algebraic structures and quantizationfl, by Daniel Freed,
Commun. Math.
Phys.
159
(1994), 343Œ398, also available as
hep-th/9212115
.
To continue reading the fiTale of
n
-Categoriesfl, see
 fiWeek 79fl
.
147
 WEEK 79 APRIL 1, 1996
Week 79
April 1, 1996
Before I continue my tale of adjoint functors I want to say a little bit about icosahedra,
buckyballs, and last letter Galois wrote before his famous duel. . . . all of which is taken
from the following marvelous article:
1)
 Bertram Kostant, fiThe graph of the truncated icosahedron and the last letter of
Galoisfl,
Notices Amer. Math. Soc.
42
(September 1995), 959Œ968. Also available
at
http://www.ams.org/notices/199509/199509-toc.html
.
When I was a graduate student at MIT I realized that Kostant (who teaches there)
was deeply in love with symmetry, and deeply knowledgeable about some of its more
mysterious byways. Unfortunately I didn't dig too deeply into group theory at the time,
and now I am struggling to catch up.
Let's start with the Platonic solids. Note that the cube and the octahedron are dual
Š putting a vertex in the center of each of the cube's faces gives you an octahedron, and
vice versa. So every rotational symmetry of the cube can be reinterpreted as a symmetry
of the octahedron, and vice versa. Similarly, the dodecahedron and the icosahedron are
dual, while the tetrahedron is self-dual. So while there are 5 Platonic solids, there are
really only 3 different symmetry groups here.
These 3 fiPlatonic groupsfl are very interesting. The symmetry group of the tetrahe-
dron is the group
A
4
of all
even
permutations of 4 things, since by rotating the tetrahe-
dron we can achieve any even permutation of its 4 vertices. The symmetry group of the
cube is
S
4
, the group of
all
permutations of 4 things. What are the 4 things here? Well,
we can draw 4 line segments connecting opposite vertices of the cube; these are the 4
things! The symmetry group of the icosahedron is
A
5
, the group of even permutations
of 5 things. What are the 5 things? It we take all the line segments connecting opposite
vertices we get 6 things, not 5, but we can't get all even permutations of those by rotating
the icosahedron. To nd the
5
things is a bit trickier; I leave it as a puzzle here. See
2)
 John Baez, fiSome thoughts on the number 6fl, available at
http://math.ucr.edu/home/baez/six.html
.
for an answer.
Once we convince ourselves that the rotational symmetry group of the icosahedron
is
A
5
, it follows that it has
5!
=
2 = 60
elements. But there is another nice way to see this.
Take an icosahedron and chop off all 12 corners, getting a truncated icosahedron with
12 regular pentagonal faces and 20 regular hexagonal faces, with all edges the same
length. It looks just like a soccer ball. It's called an Archimedean solid because, while
not quite Platonic in its beauty, every face is a regular polygon and every vertex looks
alike: two pentagons abutting one hexagon.
148
 WEEK 79 APRIL 1, 1996
The truncated icosahedron has
5

12 = 60
vertices. Every symmetry of the icosahe-
dron is a symmetry of the truncated icosahedron, so
A
5
acts to permute these 60 vertices.
Moreover, we can nd an element of
A
5
that moves a given vertex of the truncated icosa-
hedron to any other one, since fievery vertex looks alikefl. Also, there is a
unique
element
of
A
5
that does the job. So there must be precisely as many elements of
A
5
as there are
vertices of the truncated icosahedron, namely 60.
There is a lot of interest in the truncated icosahedron recently, because chemists had
speculated for some time that carbon might form
C
60
molecules with the atoms at the
vertices of this solid, and a while ago they found this was true. In fact, while
C
60
in this
shape took a bit of work to get ahold of at rst, it turns out that lowly soot contains lots
of this stuff!
Since Buckminster Fuller was fond of using truncated icosahedra in his geodesic domes,
C
60
and its relatives are called fullerenes, and the shape is affectionately called a bucky-
ball. For more about this stuff, try:
3)
 P. W. Fowler and D. E. Manolpoulos,
An Atlas of Fullerenes
, Oxford University Press,
Oxford, 1995.
M. S. Dresselhaus, G. Dresselhaus, and P. C. Eklund,
Science of Fullerenes and Car-
bon Nanotubules
, Academic Press, New York, 1994.
G. Chung, B. Kostant and S. Sternberg, fiGroups and the buckyballfl, in
Lie Theory
and Geometry
, eds. J.-L. Brylinski, R. Brylinski, V. Guillemin and V. Kac, Birkh
¨
auser,
Basel, 1994.
149
 WEEK 79 APRIL 1, 1996
In fact, for the person who has everything, you can now buy 99.95% pure
C
60
online.
But I digress. Coming back to the 3 Platonic groups... there is much more that's
special about them. Most of it requires a little knowledge of group theory to understand.
For example, they are the 3 different nite subgroups of
SO(3)
having irreducible repre-
sentations on
R
3
. And they are nice examples of nite reection groups. For more about
them from this viewpoint, try
 fiWeek 62fl
 and
 fiWeek 63fl
. Also, via the McKay correspon-
dence they correspond to the exceptional Lie groups
E
6
,
E
7
, and
E
8
Š see
 fiWeek 65fl
 for
an explanation of this!
Yet another interesting fact about these groups is buried in Galois' last letter, written
to the mathematician Chevalier on the night before Galois' fatal duel. He was thinking
about some groups we'd now call
PSL(2
; F
)
. Here
F
is a eld (for example, the real
numbers, the complex numbers, or
Z
p
, the integers mod
p
where
p
is prime).
PSL(2
; F
)
is a fiprojective special linear group over
F
.fl What does that mean? Well, rst of all,
SL(2
; F
)
is the
2

2
matrices with entries in
F
having determinant equal to
1
. These
form a group under good old matrix multiplication. The matrices in
SL(2
; F
)
that are
scalar multiples of the identity matrix form the ficenterfl
Z
of
SL(2
; F
)
Š the group of
guys who commute with everyone else. We can form the quotient group
SL(2
; F
)
=Z
, and
get a new group called
PSL(2
; F
)
.
Now, Galois was thinking about
PSL(2
;
Z
p
)
where
p
is prime. There's an obvious way
to get this group to act as permutations of
p
+ 1
things. Here's how! For any eld
F
,
the group
SL(2
; F
)
acts as linear transformations of the
2
-dimensional vector space over
F
, and it thus acts on the set of lines through the origin in this vector space... which is
called the fiprojective linefl over
F
. But anything in
SL(2
; F
)
that's a scalar multiple of
the identity doesn't move lines around, so we can mod out by the center and think of
the quotient group
PSL(2
; F
)
as acting on projective line. (By the way, this explains the
point of working with
PSL
instead of plain old
SL
.)
Now, an element of the projective line is just a line through the origin in
F
2
. We
can specify such a line by taking any nonzero vector
(
x; y
)
in
F
2
and drawing the line
through the origin and this vector. However,
(
x
0
; y
0
)
and
(
x; y
)
determine the same line
if
(
x
0
; y
0
)
is a scalar multiple of
(
x; y
)
. Thus lines are in 1-1 correspondence with vectors
of the form
(1
; y
)
or
(
x;
1)
. When our eld
F
is
Z
p
, there are just
p
+ 1
of these. So
PSL(2
;
Z
p
)
acts naturally on a set of
p
+ 1
things.
What Galois told Chevalier is that
PSL(2
;
Z
p
)
doesn't act nontrivially as permutation
of any set with fewer than
p
+ 1
elements if
p >
11
. This presumably means he knew
that
PSL(2
;
Z
p
)
does
act nontrivially on a set with only
p
elements if
p
= 5
,
7
, or
11
. For
example,
PSL(2
;
5)
turns out to be isomorphic to
A
5
, which acts on a set of 5 elements
in an obvious way.
PSL(2
;
7)
and
PSL(2
;
11)
act on a 7-element set and an 11-element
set, respectively, in sneaky ways which Kostant describes.
These cases,
p
= 5
,
7
and
11
, are the the only cases where this happens and
PSL(2
;
Z
p
)
is simple. (See
 fiWeek 66fl
 if you don't know what fisimplefl means.) In each case it is
very amusing to look at how
PSL(2
;
Z
p
)
acts nontrivially on a set with
p
elements and
consider the subgroup that doesn't move a particular element of this set. For example,
when
p
= 5
we have
PSL(2
;
5) =
A
5
, and if we look at the subgroup of even permuta-
tions of 5 things that leaves a particular thing alone, we get
A
4
. Kostant explains how
if we play this game with
PSL(2
;
7)
we get
S
4
, and if we play this game with
PSL(2
;
11)
we get
A
5
. These are the 3 Platonic groups again!!
But notice an extra curious coincidence.
A
5
is both
PSL(2
;
5)
and the subgroup
150
 WEEK 79 APRIL 1, 1996
of
PSL(2
;
11)
that xes a point of an 11-element set. This gives a lot of relationships
between
A
5
,
PSL(2
;
5)
, and
PSL(2
;
11)
. What Kostant does is take this and milk it for
all it's worth! In particular, it turns out that one can think of
A
5
as the vertices of the
buckyball, and describe which vertices are connected by an edge using the embedding
of
A
5
in
PSL(2
;
11)
. I won't say how this goes... read his paper!
This may even have some applications for fullerene spectroscopy, since one can use
symmetry to help understand spectra of compounds. (Indeed, this is one way group
theory entered chemistry in the rst place.)
Now let me return to talking about adjoint functors! I have been stressing the fact
that two functors
L
:
C ! D
and
R
:
D ! C
are adjoint if there is a natural isomorphism
between
Hom(
Lc; d
)
and
Hom(
c; R d
)
. We can say that an fiadjunctionfl is a pair of func-
tors
L
:
C ! D
and
R
:
D ! C
together with a natural isomorphism between
Hom(
Lc; d
)
and
Hom(
c; R d
)
. But there is another way to think about adjunctions which is also good.
In
 fiWeek 76fl
 we talked about an fiequivalencefl of categories. We can summarize it
this way: an fiequivalencefl of the categories
C
and
D
is a pair of functors
F
:
C ! D
and
G
:
D ! C
together with natural transformations
e
:
F G
)
1
D
and
i
: 1
C
)
GF
that are
themselves invertible. (Note that we are now writing products of functors in the order
that ordinary mortals typically do, instead of the backwards way we introduced in
 fiWeek
73fl
. Sorry! It just happens to be better to write it this way now.) Now, the concept of
fiadjunctionfl is a cousin of the concept of fiequivalencefl, and it's nice to have a denition
of adjunction that brings out this relationship.
First, consider what happens in the denition of adjunction if we take
c
=
R d
. Then
we have a natural isomorphism between
Hom(
LR d; d
)
and
Hom(
R d; R d
)
. Now there
is a special element of
Hom(
R d; R d
)
, namely the identity
1
R d
. This gives us a special
element of
Hom(
LR d; d
)
. Let's call this
e
d
:
LR d
!
d:
What is this morphism like in an example? Say
L
:
Set
!
Grp
takes each set to the
free group on that set, and
R
:
Grp
!
Set
takes each group to its underlying set. Then
if
d
is a group,
LR d
is the free group on the underlying set of
d
. There's an obvious
homomorphism from
LR d
to
d
, taking each word of elements in
d
and their inverses to
their product in
d
. That's
e
d
. It goes from the free thing on the underlying thing of
d
to
the thing
d
itself!
In fact, since everything in sight is natural, whenever we have an adjunction the
morphisms
e
d
dene a natural transformation
e
:
LR
)
1
D
Next, consider what happens in the denition of adjunction if we take
d
=
Lc
. Then
we have a natural isomorphism between
Hom(
c; R Lc
)
and
Hom(
Lc; Lc
)
. Now there is a
special element in
Hom(
Lc; Lc
)
, namely the identity
1
Lc
. This gives us a special element
in
Hom(
c; R Lc
)
. Let's call this
i
c
:
c
!
R Lc:
151
 WEEK 79 APRIL 1, 1996
Again, it's good to consider the example of sets and groups: if
c
is a set,
R Lc
is the
underlying set of the free group on
c
. There is an obvious way to map
c
into
R Lc
. That's
i
c
. It goes from the thing
c
to the underlying thing of the free thing on
c
.
As before, we get a natural transformation
i
: 1
C
)
R L
So, as in an equivalence, when we have an adjunction we have natural transformations
e
:
LR
)
1
D
and
i
: 1
C
)
R L
. Unlike in an equivalence, they needn't be natural
isomorphisms
, as the example of sets and groups shows. But they do have some cool
properties, which are nice to draw using pictures.
First, we draw
e
as a U-shaped thing:
L
R
The idea here is that
e
goes from
LR
down to the identity
1
D
, which we draw as finoth-
ingfl. We can think of
L
and
R
as processes, and the U-shaped thing as the meta-process
of
L
and
R
ficolliding into each other and cancelling outfl, like a particle and antiparticle.
(Lest you think that's just purple prose, wait and see! Eventually I'll explain what all this
has to do with antiparticles!) Similarly, we draw
i
as an upside-down-U-shaped thing:
R
L
In other words,
i
goes from the identity
1
C
to
R L
.
We can also use this sort of notation to talk about identity natural transformations.
For example, if we have any old functor
F
, there is an identity natural transformation
1
F
:
F
)
F
, which we can draw as follows:
F
F
We draw it as a boring vertical line because finothing is happeningfl as we go from
F
to
F
.
Now, I haven't talked much about the ways one can compose natural transforma-
tions like
i
and
e
, but remember that they are
2
-morphisms, or morphisms-between-
morphisms, in
Cat
(the
2
-category of all categories). This means that they are inherently
2
-dimensional, and in particular, one can compose them both fihorizontallyfl and fiverti-
callyfl. I'll explain this more next time, but for now please take my word for it! Using
152
 WEEK 79 APRIL 1, 1996
these composition operations, one can make sense of the following equations involving
i
and
e
:
R
R
=
R
R
and
L
L
=
L
L
In the rst equation we are asserting that a certain way of sticking together
i
and
e
and
some identity natural transformations gives
1
R
:
R
)
R
. In the second we are asserting
that some other way gives
1
L
:
L
)
L
.
I will explain these more carefully next time, but for now I mainly want to state that
we can also
dene
an adjunction to be a pair of functors
L
:
C ! D
and
R
:
D ! C
together with natural transformations
e
:
LR
)
1
D
and
i
: 1
C
)
R L
making the above
2 equations hold! This is the denition of fiadjunctionfl that is the most similar to the
denition of fiequivalencefl.
Now, topologically, these 2 equations simply say that if you have a wiggly curve like
or
you can pull it tight to get
153
 WEEK 79 APRIL 1, 1996
Thus, while
and
are not exactly fiinversesfl, there is some subtler sense in which they ficancel outfl. This
corresponds to the notion that while adjoint functors are not inverses, not even up to a
natural isomorphism, they still are filike inversesfl in a subtler sense.
Now this may seem like a silly game, drawing natural transformations as fistring
diagramsfl and interpreting adjoint functors as wiggles in the string. But in fact this is
part of a very big, very important, and very fun game: the relation between
n
-category
theory and the topology of submanifolds of
R
n
. Right now we are dealing with
Cat
,
which is a
2
-category, so we are getting into
2
-dimensional pictures. But when we get
into
3
-categories we will get into
3
-dimensional pictures, and knot theory... and what got
me into this whole business in the rst place: the relation between knots and physics. In
higher dimensions it gets even fancier.
So I will continue next time and explain the recipes for composing natural transfor-
mations, and the associated string diagrams, more carefully. To continue reading the
fiTale of
n
-Categoriesfl, see
 fiWeek 80fl
.
154
 WEEK 80 APRIL 20, 1996
Week 80
April 20, 1996
There are a number of interesting books I want to mention.
Huw Price's book on the arrow of time is nally out! It's good to see a philosopher of
science who not only understands what modern physicists are up to, but can occasionally
beat them at their own game.
Why is the future different from the past? This has been vexing people for a long
time, and the stakes went up considerably when Boltzmann proved his fiH-theoremfl,
which seems at rst to show that the entropy of a gas always increases, despite the time-
reversibility of the laws of classical mechanics. However, to prove the H-theorem he
needed an assumption, the fiassumption of molecular chaosfl. It says roughly that the
positions and velocities of the molecules in a gas are uncorrelated before they collide.
This seems so plausible that one can easily overlook that it has a time-asymmetry built
into it Š visible in the word fibeforefl. In fact, we aren't getting something for nothing in
the H-theorem; we are making a time-asymmetric assumption in order to conclude that
entropy increases with time!
The fiindependence of incoming causesfl is very intuitive: if we do an experiment on
an electron, we almost always assume our choice of how to set the dials is not correlated
to the state of the electron. If we drop this time-asymmetric assumption, the world looks
rather different... but I'll let Price explain that to you.
Anyway, Price is an expert at spotting covertly time-asymmetric assumptions. you
may remember from
 fiWeek 26fl
 that he even got into a nice argument with Stephen
Hawking about the arrow of time, thanks to this habit of his. You can read more about
it in:
1)
 Huw Price,
Time's Arrow and Archimedes' Point: New Directions for a Physics of Time
,
Oxford U. Press, Oxford, 1996.
Also, there is a new book out by Hawking and Roger Penrose on quantum gravity.
First they each present their own ideas, and then they duke it out in a debate in the
nal chapter. This book is an excellent place to get an overview of some of the main
ideas in quantum gravity. It helps if you have a little familiarity with general relativity,
or differential geometry, or are willing to fake it.
There is even some stuff here about the arrow of time! Hawking has a theory of how
it arose, starting from his marvelous fino-boundary boundary conditionsfl, which say that
the wavefunction of the universe is full of quantum uctuations corresponding to big
bangs which erupt and then recollapse in big crunches. The wavefunction itself has
no obvious fitime-asymmetryfl, indeed, time as we know it only makes sense
within
any
one of the quantum uctuations, one of which is presumably the world we know! But
Hawking thinks that each of these quantum uctuations, or at least most of them, should
have an arrow of time. This is what Price raised some objections to. Hawking seems to
argue that each quantum uctuation should fistart outfl rather smooth near its big bang
and develop more inhomogeneities as time passes, fiwinding upfl quite wrinkly near its
big crunch. But it's not at all clear what this fistarting outfl and fiwinding upfl means.
Possibly he is simply speaking vaguely, and all or most of the quantum uctuations can
155
 WEEK 80 APRIL 20, 1996
be shown to have one smooth end and wrinkly at the other. That would be an adequate
resolution to the arrow of time problem. But it's not clear, at least not to me, that
Hawking really showed this.
Penrose, on the other hand, has some closely related ideas. His fiWeyl curvature
hypothesisfl says that the Weyl curvature of spacetime goes to zero at initial singularities
(e.g. the big bang) and innity at nal ones (e.g. black holes). The Weyl curvature can be
regarded as a measure of the presence of inhomogeneity Š the fiwrinklinessfl I alluded
to above. The Weyl curvature hypothesis can be regarded as a time-asymmetric law built
into physics from the very start.
To see them argue it out, read
2)
 Stephen Hawking and Roger Penrose,
The Nature of Space and Time
, Princeton U.
Press, Princeton, 1996.
There are also a couple of more technical books on general relativity that I'd been
meaning to get ahold of for a long time. They both feature authors of that famous book,
3)
 Charles Misner, Kip Thorne and John Wheeler,
Gravitation
, Freeman Press, 1973,
which was actually the book that made me decide to work on quantum gravity, back
at the end of my undergraduate days. They are:
4)
 Ignazio Ciufolini and John Archibald Wheeler,
Gravitation and Inertia
, Princeton
U. Press, Princeton, 1995.
and
5)
 Kip Thorne, Richard Price and Douglas Macdonald, eds.,
Black Holes: The Mem-
brane Paradigm
, Yale U. Press, New Haven, 1986.
The book by Ciufolini and Wheeler is full of interesting stuff, but it concentrates on
figravitomagnetismfl: the tendency, predicted by general relativity, for a massive spinning
body to apply a torque to nearby objects. This is related to Mach's old idea that just as
spinning a bucket pulls the water in it up to the edges, thanks to the centrifugal force,
the same thing should happen if instead we make lots of stars rotate around the bucket!
Einstein's theory of general relativity was inspired by Mach, but there has been a long-
running debate over whether general relativity is fitruly Machianfl Š in part because
nobody knows what fitruly Machianfl means. In any event, Ciufolini and Wheeler argue
that gravitomagnetism exhibits the Machian nature of general relativity, and they give a
very nice tour of gravitomagnetic effects.
That is ne in theory. However, the gravitomagnetic effect has never yet been ob-
served! It was supposed to be tested by Gravity Probe B, a satellite ying at an altitude
of about 650 kilometers, containing a superconducting gyroscope that should precess at
a rate of 42 milliarcseconds per year thanks to gravitomagnetism. I don't know what
ever happened with this, though: the following web page says fiGravity Probe B is ex-
pected to y in 1995fl, but now it's 1996, right? Maybe someone can clue me in to the
latest news. . . . I seem to remember some arguments about funding the program.
6)
 Gravity Probe B,
https://web.archive.org/web/19970506010314/
http://stugyro.stanford.edu/RELATIVITY/GPB/GPB.html
.
156
 WEEK 80 APRIL 20, 1996
(Note added in 2002: now this webpage is gone; see
http://einstein.stanford.
edu/
for the latest story.)
Kip Thorne's name comes up a lot in conjuction with black holes and the LIGO Š or
Laser-Interferometer Gravitational-Wave Observatory Š project. As pairs of black holes
or neutron stars emit gravitational radiation, they should spiral in towards each other.
In their nal moments, as they merge, they should emit a fichirpfl of gravitational radi-
ation, increasing in frequency and amplitude until their ecstatic union is complete. The
LIGO project aims to observe these chirps, and any other sufciently strong gravitational
radiation that happens to be passing by our way. LIGO aims to do this by using laser
interferometry to measure the distance between two points about 4 kilometers apart to
an accuracy of about
10

18
meters, thus detecting tiny ripples in the spacetime metric.
For more on LIGO, try:
7)
 LIGO project home page,
http://www.ligo.caltech.edu/
.
Thorne helped develop a nice way to think of black holes by envisioning their event
horizon as a kind of fimembranefl with well-dened mechanical, electrical and magnetic
properties. This is called the membrane paradigm, and is useful for calculations and
understanding what black holes are really like. The book fiBlack Holes: The Membrane
Paradigmfl is a good place to learn about this.
Now let me return to the fiTale of
n
-Categoriesfl Š and in particular,
2
-categories.
So far I've said only that a
2
-category is some sort of structure with objects, morphisms
between objects, and
2
-morphisms between morphisms. But I have been attempting to
develop your intuition for
Cat
, the primordial example of a
2
-category. Remember,
Cat
is the
2
-category of all categories! Its objects are categories, its morphisms are functors,
and its
2
-morphisms are natural transformations Š these being dened in
 fiWeek 73fl
and again in
 fiWeek 75fl
.
How can you learn more about
2
-categories? Well, a really good place is the following
article by Ross Street, who is one of the great gurus of
n
-category theory. For example,
he was the one who invented
!
-categories!
8)
 Ross Street, fiCategorical structuresfl, in
Handbook of Algebra
, vol.
1
, ed. M. Hazewinkel,
Elsevier, Amsterdam, 1996.
Physicists should note his explanation of the YangŒBaxter and Zamolodchikov equations
in terms of category theory. If you have trouble nding this, you might try
9)
 G. Maxwell Kelly and Ross Street, fiReview of the elements of
2
-categoriesfl, in
Lecture Notes in Mathematics
420
, Springer, Berlin, 1974, pp. 75Œ103.
I can't really compete with these for thoroughness, but at least let me give the def-
inition of a
2
-category. I'll give a pretty nuts-and-bolts denition; later I'll give a more
elegant and abstract one. Readers who are familiar with
Cat
should keep this example
in mind at all times!
This denition is sort of long, so if you get tired of it, concentrate on the pictures!
They convey the basic idea. Also, keep in mind is that this is going to be sort of like the
denition of a category, but with an extra level on top, the
2
-morphisms.
157
 WEEK 80 APRIL 20, 1996
So: rst of all, a
2
-category consists of a collection of fiobjectsfl and a collection of
fimorphismsfl. Every morphism
f
has a fisourcefl object and a fitargetfl object. If the
source of
f
is
x
and its target is y, we write
f
:
x
!
y
. In addition, we have:
1)
 Given a morphism
f
:
x
!
y
and a morphism
g
:
y
!
Z
, there is a morphism
f g
:
x
!
Z
, which we call the ficompositefl of
f
and
g
.
2)
 Composition is associative:
(
f g
)
h
=
f
(
g h
)
.
3)
 For each object
x
there is a morphism
1
x
:
x
!
x
, called the fiidentityfl of x. For any
f
:
x
!
y
we have
1
x
f
=
f
1
y
=
f
.
You should visualize the composite of
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
Z
as follows:
x
f
!
y
g
!
Z :
So far this is exactly the denition of a category! But a
2
-category
also
consists of a
collection of fi2-morphismsfl. Every
2
-morphism
T
has a fisourcefl morphism
f
and a
target morphism
g
. If the source of
T
is
f
and its target is
g
, we write
T
:
f
)
g
.
If
T
:
f
)
g
, we require that
f
and
g
have the same source and the same target; for
example,
f
:
x
!
y
and
g
:
x
!
y
. You should visualize
T
as follows:
In addition, we have:
1
0
) Given a
2
-morphism
S
:
f
)
g
and a
2
-morphism
T
:
g
)
h
, there is a
2
-morphism
S T
:
f
)
h
, which we call the fivertical compositefl of
S
and
T
.
2
0
) Vertical composition is associative:
(
S T
)
U
=
S
(
T U
)
.
3
0
) For each morphism
f
there is a
2
-morphism
1
f
:
f
)
f
, called the fiidentityfl of
f
.
For any
T
:
f
)
g
we have
1
f
T
=
T
1
g
=
T
.
Note that these are just like the previous 3 rules. We draw the vertical composite of
S
:
f
)
g
and
T
:
g
)
h
like this:
Now for a twist. We also require that we can fihorizontallyfl compose 2-morphisms as
158
 WEEK 80 APRIL 20, 1996
follows:
So we also demand:
1
00
) Given morphisms
f ; g
:
x
!
y
and
f
0
; g
0
:
y
!
z
, and
2
-morphisms
S
:
f
)
g
and
T
:
f
0
)
g
0
, there is a
2
-morphism
S

T
:
f f
0
)
g g
0
, which we call the fihorizontal
compositefl of
S
and
T
.
2
00
) Horizontal composition is associative:
(
S

T
)

U
=
S

(
T

U
)
.
3
00
) The identities for vertical composition are also the identities for horizontal com-
position. That is, given
f ; g
:
x
!
y
and
T
:
f
)
g
we have
1
1
x

T
=
T

1
1
y
=
T
.
Finally, we demand the fiexchange lawfl relating horizontal and vertical composition:
(
S T
)

(
S
0
T
0
) = (
S

S
0
)(
T

T
0
)
This makes the following
2
-morphism unambiguous:
We can think of it either as the result of rst doing two vertical composites, and then one
horizontal composite, or as the result of rst doing two horizontal composites, and then
one vertical composite!
Here we can really see why higher-dimensional algebra deserves its name. Unlike cat-
egory theory, where we can visualize morphisms as 1-dimensional arrows, here we have
2
-morphisms which are intrinsically 2-dimensional, and can be composed both vertically
and horizontally.
Now if you are familiar with
Cat
, you may be wondering how we vertically and
horizontally compose natural transformations, which are the 2-morphisms in
Cat
. Let
me leave this as an exercise for now... there's a nice way to do it that makes
Cat
into
a
2
-category. This exercise is a good one to build up your higher-dimensional algebra
muscles.
In fact, we could have invented the above denition of
2
-category simply by thinking
a lot about
Cat
and what you can do with categories, functors, and natural transforma-
tions. I'm pretty sure that's more or less what happened, historically! Thinking hard
enough about
n
Cat
leads us on to the denition of
(
n
+ 1)
-categories. . . .
But that's enough for now. Typing those diagrams is hard work. To continue reading
the fiTale of
n
-Categoriesfl, see
 fiWeek 83fl
.
159
 WEEK 80 APRIL 20, 1996
I thank Keith Harbaugh for catching lots of typos and other mistakes in
 fiWeek 73fl
 Œ
fiWeek 80fl
.
160
 WEEK 81 MAY 12, 1996
Week 81
May 12, 1996
I think I'll take a little break on the continuing saga of
n
-categories. Instead I'll talk about
something which is secretly the very same subject, namely loop groups and their central
extensions. This is important in string theory. But rst I want to say a bit about some
very high-energy physics.
1)
 D. J. Bird
et al
, fiDetection of a cosmic ray with measured energy well beyond
the expected spectral cutoff due to cosmic microwave radiationfl,
The Astrophysical
Journal
441
(1995), 144Œ150. Also available as
astro-ph/9410067
P. Bhattacharjee and G. Sigl, fiMonopole annihilation and highest energy cosmic
raysfl,
Phys. Rev. D
51
(1995), 4079. Also available as
astro-ph/9412053
.
R. J. Protheroe and P. A. Johnson, fiAre topological defects responsible for the 300
EeV cosmic rays?fl,
Nucl. Phys. B - Proc. Suppl.
48
(1996), 485Œ487. Also available
as
astro-ph/9605006
.
In 1994, folks at the Fly's Eye air shower detector in Utah observed a cosmic ray
whose energy was about 320 EeV. In case you forget what an EeV is, it's a unit of energy
equal to a billion GeV, and a Gev is equal to a billion ev (electron volts). Current particle
accelerators routinely create particles with energies about a hundred GeV, but a few
hundred
EeV
is a whole different story! That's about 50 joules, the energy of a one-
kilogram mass moving at 10 meters/second, all packed in one particle!
Nobody knows what would produce cosmic rays of this energy. To make the puzzle
more mysterious, this energy is above the GreisenŒZatsepinŒKuz'min (or GZK) cutoff for
cosmic rays produced at moderate extragalactic distances (30 megaparsecs). The idea of
the GZK cutoff is that particles of extremely high energies whizzing through space would
interact signicantly with the cosmic microwave background radiation, losing energy to
produce pions.
So it seems that something is producing really high energy particles, and this some-
thing is not too far away, by cosmic standards. Established mechanisms don't get ener-
gies that high. A possibility studied by various authors including P. Bhattacharjee and G.
Sigl is that these super-energetic cosmic rays are produced by the decay of fitopological
defectsfl. Various grand unied theories, or GUTs, predict that the strong, weak, and
electromagnetic forces all act the same at really high temperatures, while at low temper-
atures (like any sort of temperature you'd nd around here) a fispontaneous symmetry
breakingfl occurs which makes them split up into their observed distinct personalities.
Mathematically this is a bit like how a magnet at low temperatures randomly picks
out a certain axis of magnetization, breaking the rotational symmetry it possesses at
high temperatures. And like in the case of a magnet, one would expect the possibility
of fitopological defectsfl where different regions of space pick different ways to break the
symmetry, leaving nasty spots like lumps in the carpet that can't be straightened out. Or-
dinary magnets typically exhibit
2
-dimensional fidomain wallsfl between domains having
different axes of magnetization. But in various GUTs folks have considered, one can also
get 1-dimensional ficosmic stringsfl and 0-dimensional fitopological solitonsfl including
161
 WEEK 81 MAY 12, 1996
magnetic monopoles Š particles with magnetic charge. None of these topological de-
fects have ever been observed, despite a fair amount of searching. Could super-energetic
cosmic rays be the result of a monopole-antimonopole collision?
Alas, Protheroe and Johnson's paper argues that in such decays lots of the energy
would go into the production of high-energy

rays... more than has been observed in
the super-energetic cosmic ray showers. So maybe the puzzle has some other answer.
The weekend before last I went to the 11th Geometry Festival, which was held at the
University of Maryland. Since I work on quantum gravity, I could be said to be a geometer
of sorts Š perhaps a quantum geometer. But geometry means a lot of different things
to different people, and this conference concentrated on some aspects of geometry that
I don't know much about. In particular, there were talks by Schmuel Weinberger, Bruce
Kleiner and G. Wei on the implications of positive and negative curvature for Riemannian
geometry.
A talk that was right up my alley was given by Jean-Luc Brylinski. It dealt with
themes from his papers with McLaughlin:
2)
 Jean-Luc Brylinski and Dennis A. McLaughlin, fiThe geometry of degree four char-
acteristic classes and of line bundles on loop spaces, Ifl,
Duke Math. Journal
75
(1994), 603Œ638. fiIIfl,
Duke Math. Journal
83
(1996), 105Œ139.
Jean-Luc Brylinski, fiCentral extensions and reciprocity lawsfl,
Cahiers de Topologie
et G
´
eom
´
etrie Diff
´
erentielle Cat
´
egoriques
38
(1997), 193Œ215.
Jean-Luc Brylinski, fiCoadjoint orbits of central extensions of gauge groupsfl,
Com-
mun. Math. Phys.
188
(1997), 351Œ365.
Jean-Luc Brylinski and Dennis A. McLaughlin, fiThe geometry of two dimensional
symbolsfl,
K-Theory
10
(1996), 215Œ237.
Let me say a bit about the math underlying these papers, the basic stuff that they build
on. One hot topic in mathematical physics in the last decade has been the study of filoop
groupsfl. Say you take any Lie group
G
. Then the filoop groupfl
LG
is the set of smooth
functions from the circle to
G
. This becomes a group with pointwise multiplication as
the group operation. This sort of group shows up in
2
-dimensional quantum eld theory,
where spacetime could be the cylinder. Then fispacefl is the circle, and if we are studying
gauge theory with gauge group
G
, the group of gauge transformations over space would
be the loop group
LG
. One main reason for being interested in
2
-dimensional quantum
eld theory is string theory: here we think of the
2
-dimensional worldsheet of the string
as a spacetime in its own right, and we are often interested in doing gauge theory over
this spacetime. For this reason, folks in string theory need to understand all they can
about unitary representations of loop groups.
Actually they are interested in
projective
representations of loop groups. Remember,
in quantum mechanics two vectors in a Hilbert space give the same expectation values
for any observable if they differ only by a phase. So it is perfectly ne for a group
representation
R
to satisfy the usual law
R
(
g
)
R
(
h
) =
R
(
g h
)
where
g
,
h
are group elements,
only up to a phase
. So in the denition of a projective
representation we weaken the above requirement to
R
(
g
)
R
(
h
) =
c
(
g ; h
)
R
(
g h
)
162
 WEEK 81 MAY 12, 1996
where
c
(
g ; h
)
is a phase depending on
g
and
h
. Folks call
c
(
g ; h
)
the ficocyclefl of the
projective representation.
A projective unitary representation of a group
H
can also be thought of as a repre-
sentation of a bigger group
e
H
called a ficentral extensionfl of
H
. The idea is that this
bigger group has a bunch of phases built into it to absorb the phase ambiguities in the
projective representation of
H
. Let
U(1)
be the unit circle in the complex plane, a group
under multiplication. This is the group of phases. We can think of
e
H
as
H

U(1)
given
a sneaky product designed to soak up the phases produced by the cocycle:
(
g ; a
)(
h; b
) = (
g h; abc
(
g ; h
))
:
We can dene a unitary representation
S
of
e
H
as follows:
S
(
g ; a
) =
R
(
g
)
a:
It's then obvious that
S
(
g ; a
)
S
(
h; b
) =
S
((
g ; a
)(
h; b
))
so
S
is really a representation. For this reason, if we are doing quantum theory and
we don't like projective representations, it's okay as long as we understand the central
extensions of our group of symmetries.
So, instead of thinking about projective representations of loop groups, we can think
about central extensions of loop groups. How does one get ahold of these? There is a
nice trick which Brylinski described in his talk. To get this trick, we need to assume a
bit about the group
G
. Let's assume it's a connected and simply-connected simple Lie
group. I'll explain that in a minute, but some good examples to keep in mind are
SU(
n
)
and
Spin(
n
)
; see
 fiWeek 61fl
 for the denitions and a bit of information about these
groups.
Now remember that
S
k
stands for the
k
-dimensional sphere, and
ˇ
k
(
X
)
of a topo-
logical space
X
stands for the set of continuous maps from
S
k
to
X
, modulo homotopy.
In other words, two continuous maps from
S
k
to
X
dene the same element of
ˇ
k
(
X
)
if
one can be continuously deformed to the other.
Saying that
G
is connected means that
ˇ
0
(
G
) = 0
. To understand this you need to
realize that
S
0
consists of two points. So
ˇ
0
(
G
) = 0
means that
G
consists of one piece,
any two points of which can be connected by a continuous path.
Saying that
G
is simply connected means that
ˇ
1
(
G
) = 0
. In other words, all loops
in
G
can be fipulled tightfl. A good example of a group that's
not
simply connected is
the group
SO(
n
)
of rotations in
n
dimensional space. This aw with
SO(
n
)
is why they
needed to invent
Spin(
n
)
; see
 fiWeek 61fl
.
As it turns out, every Lie group has
ˇ
2
(
G
) = 0
. So all 2-spheres in
G
can be pulled
tight too. Imagine taking a balloon and sticking it in
G
; then you can always shrink it
down to a point in a continuous way without it getting stuck around a hole in
G
.
Saying that
G
is simple is an algebraic rather than topological condition, and I ex-
plained this condition in
 fiWeek 63fl
. But it has topological ramications. It implies, for
example, that
ˇ
3
(
G
) =
Z
, the group of integers. So to each way of sticking a 3-sphere in
G
we can associate an integer. One way to compute this integer involves the Killing form
on the Lie algebra of
G
. This is a special inner product on the Lie algebra of
G
. Using
163
 WEEK 81 MAY 12, 1996
this inner product and the bracket in the Lie algebra we can convert 3 vectors
u
,
v
, and
w
in the Lie algebra into a number as follows:
W
(
u; v ; w
) =
k
h
[
u; v
]
; w
i
Here
k
is a constant that will make life simpler later. The special property of the Killing
form implies that
W
is totally antisymmetric, and we can use left multiplication to trans-
late
W
all over the group
G
obtaining a closed
3
-form on
G
. Call this
3
-form
W
, too.
Then, given any smooth function from
S
3
into
G
we can pull back
W
to
S
3
and integrate
it over
S
3
. If we choose the constant
k
right, the result will be an integer Š the integer
we were looking for.
Hmm, this is getting technical. Well, it'll keep getting more technical. Just stop
reading when it becomes unpleasant.
Okay, these topological facts about the group
G
have a bunch of cool consequences.
One trick usually goes by the name of the fiWZW actionfl, which refers to Wess, Zumino,
and Witten. Say we have smooth function
f
from
S
2
to
G
. Since
ˇ
2
(
G
) = 0
we can
extend
f
to a smooth function
F
from the
3
-dimensional ball,
D
3
, to
G
. (This is just
another way of fipulling the balloon tightfl as mentioned above.) Now we can use
F
to
pull back the magic
3
-form
W
to
D
3
, and then we can integrate the resulting
3
-form over
D
3
to get a number
S
(
f
)
called the WessŒZuminoŒWitten action.
Unfortunately, this number depends on the choice of the function
F
extending
f
to
the ball. Fortunately, it doesn't depend too much on
F
. Say we extended
f
to some other
function
F
0
from the ball to
G
. Then
F
together with
F
0
dene a map from
S
3
to
G
, and
we know from the previous stuff that the integral of the pullback of
W
over this
S
3
is
an integer. So changing our choice of an extension of
f
only changes
S
(
f
)
by an integer.
This means that the exponential of the WZW action:
exp(2
ˇ iS
(
f
))
is completely well-dened. This is nice in quantum physics, where the exponential of the
action is what really matters. Note also that this exponential is just a phase! So we are
getting a function
A
: Maps(
S
2
; G
)
!
U(1)
assigning a phase to any map
f
from
S
2
to
G
.
Now
Maps(
S
2
; G
)
is sort of like the loop group, since the loop group is just
Maps(
S
1
; G
)
.
In particular, it too becomes a group by pointwise multiplication. A bit of calculation
shows that
A
above is a group homomorphism:
A
(
f
)
A
(
g
) =
A
(
f g
)
:
This homomorphism is the key to nding the central extension of the loop group. Here's
how we do it. By now everyone but the experts has probably fallen asleep at the screen,
so I can pull out all the stops.
Here's a useful way to think of a central extensions: a central extension
e
H
of the
group
H
by the group
U(1)
is a special sort of short exact sequence of groups:
1
!
U(1)
!
e
H
!
H
!
1
164
 WEEK 81 MAY 12, 1996
By fishort exact sequence of groupsfl I simply mean that
U(1)
is a subgroup of
e
H
and that
e
H
modulo
U(1)
is
H
. What's special about central extensions is that
U(1)
is in the
center
of
e
H
. You can check that this denition of central extension matches up with our earlier
more lowbrow denition.
Now how do we get this short exact sequence? Well, it comes from a short exact
sequence of spaces:
fg !
S
1
!
D
2
!
S
2
! fg
This diagram means simply that we can think of the circle as a subspace of the
2
-
dimensional disc
D
2
in an obvious way, and then if we collapse this circle to a point the
disc gets squashed down to a 2-sphere. Now, from this short exact sequence we get a
short exact sequence of groups
1
!
Maps(
S
2
; G
)
!
Maps(
D
2
; G
)
!
Maps(
S
1
; G
)
!
1
In other words,
Maps(
S
2
; G
)
is a normal subgroup of
Maps(
D
2
; G
)
, and if we mod out
by this subgroup we get
Maps(
S
1
; G
)
. Now we can use the homomorphism
A
: Maps(
S
2
; G
)
!
U(1)
to get ourselves another exact sequence like this:
1
Maps(
S
2
; G
)
Maps(
D
2
; G
)
Maps(
S
1
; G
)
1
1
U(1)
e
L
Maps(
S
1
; G
)
1
i
A
j
1
i
j
Remembering that
Maps(
S
1
; G
)
is the loop group,
e
L
turns out to be the desired central
extension! Concretely we can think of
e
L
as a quotient group of
Maps(
D
2
; G
)

U(1)
by
the subgroup of pairs of the form
(
i
(
f
)
; A
(
f
))
with
f
in
Maps(
S
2
; G
)
.
There is something fascinating about how spheres of different dimensions Š
S
0
,
S
1
,
S
2
, and
S
3
Š conspire together with the topology of the group
G
to yield the central
extension of the loop group
LG
. It appears that what we are really studying are the
closely related cohomology groups:
Ł
H
0
(Maps(
S
3
; G
))
which is just another way of saying
ˇ
3
(
G
)
Ł
H
1
(Maps(
S
2
; G
))
which describes homomorphisms from
Maps(
S
2
; G
)
to
U(1)
Ł
H
2
(Maps(
S
1
; G
))
which describes central extensions of
Maps(
S
1
; G
)
Ł
H
3
(Maps(
S
0
; G
))
which is just another way of saying
H
3
(
G
)
, where
W
lives.
There is a fourth term in this series which I didn't get around to talking about; it's
Ł
H
4
(
B
G
)
where the degree 4 characteristic class for
G
-bundles, e.g. the 2nd Chern
class for
SU(
n
)
, lives.
Here
B
G
is the ficlassifying spacefl of
G
. I would like to understand more deeply
what's going on with this series, because the different terms have a lot to do with physics
in different dimensions Š dimensions 0 to 4, the filow dimensionsfl which are so specially
interesting.
I should conclude by noting that while a lot of this appeared in Brylinski's talk, and a
lot of it is probably common knowledge among topologists, it was in some conversations
with James Dolan that we worked out some of the patterns I mention here.
165
 WEEK 82 MAY 17, 1996
Week 82
May 17, 1996
I will continue to take a break from the tale of
n
-categories. As the academic year winds
to an end, an enormous pile of articles and books is building up on my desk. I can kill
two birds with one stone if I list some of them while ling them. Here is a sampling:
1)
Advances in Applied Clifford Algebras
, ed. Jaime Keller.
This is a homegrown journal for fans of Clifford algebras. What are Clifford algebras?
Well, let's start at the beginning, with the quaternions. . . .
As J. Lambek has pointed out, not many mathematicians can claim to have introduced
a new kind of number. One of them was the Sir William Rowan Hamilton. He knew about
the real numbers
R
, of course, and also the complex numbers
C
, which are the reals with
a square root of

e
2
e
1
:
Thus
C
2
is just the quaternions, with
e
1
,
e
2
, and
e
1
e
2
corresponding to Hamilton's
i
,
j
,
and
k
.
How about the
C
n
for larger values of
n
? Well, here is a little table up to
n
= 8
:
C
0
R
C
1
C
C
2
H
C
3
H
+
H
C
4
H
(2)
C
5
C
(4)
C
6
R
(8)
C
7
R
(8) +
R
(8)
C
8
R
(16)
What do these entries mean? Well,
R
(
n
)
means the
n

n
matrices with real entries.
167
 WEEK 82 MAY 17, 1996
Similarly,
C
(
n
)
means the
n

n
complex matrices, and
H
(
n
)
means the
n

n
quater-
nionic matrices. All these become algebras with the usual matrix addition and matrix
multiplication. Finally, if
A
is an algebra,
A
+
A
means the algebra consisting of pairs of
guys in
A
, with the obvious rules for addition and multiplication:
(
a; a
0
) + (
b; b
0
) = (
a
+
b; a
0
+
b
0
)
(
a; a
0
)(
b; b
0
) = (
ab; a
0
b
0
)
You might enjoy checking some of these descriptions of the Clifford algebras
C
n
for
n
up to 8. You have to nd the fiisomorphismfl Š the correspondence between the Clifford
algebra and the algebra I claim is really the same. This gets pretty tricky when
n
gets
big.
How about
n
larger than 8? Well, here a remarkable fact comes into play. Clifford
algebras display a certain sort of fiperiod 8fl phenomenon. Namely,
C
n
+8
consists of
16

16
matrices with entries in
C
n
! For a proof you might try
2)
 H. Blaine Lawson, Jr. and Marie-Louise Michelson,
Spin Geometry
, Princeton U.
Press, Princeton, 1989.
or
3)
 Dale Husemoller,
Fibre Bundles
, Springer, Berlin, 1994.
These books also describe some of the amazing consequences of this periodicity phe-
nomenon. The topology of
n
-dimensional manifolds is very similar to the topology of
(
n
+ 8)
-dimensional manifolds in some subtle but important ways! I should describe this
fiBott periodicityfl sometime, but for now let me leave it as a tantalizing mystery.
I will also have to take a rain check when it comes to describing the importance of
Clifford algebras in physics... let me simply note that they are crucial for understanding
spin-
1
=
2
particles. I talked a bit about this in
 fiWeek 61fl
.
The fiSpin Geometryfl book goes into a lot of detail on Clifford algebras, spinors,
the Dirac equation and more. The fiFibre Bundlesfl book concentrates on the branch of
topology called K-theory, and uses this together with Clifford algebras to tackle various
subtle questions, such as how many linearly independent vector elds you can nd on a
sphere.
4)
 Ralph L. Cohen, John D. S. Jones, and Graeme Segal, fiMorse theory and classifying
spacesfl, preprint as of Sept. 13, 1991.
This is a nice way to think about what's really going on with Morse theory. In Morse
theory we study the topology of a compact Riemannian manifold by putting a fiMorse
functionfl on it: a real-valued smooth function with only nondegenerate critical points.
The gradient of this function denes a vector eld and we use the way points ow along
this vector eld to chop the manifold up into convenient pieces or ficellsfl. A while back,
Witten discovered, or rediscovered, a very cute way to compute a topological invariant
called the fihomologyfl of the manifold using Morse theory. (I've heard that this was
previously known and then largely forgotten.)
Here the authors rene this construction. They cook up a category
C
from the Morse
function: the objects of
C
are critical points of the Morse function, and the morphisms are
168
 WEEK 82 MAY 17, 1996
piecewise gradient ow lines. This is a topological category, meaning that for any pair of
objects
x
and
y
the morphisms in
Hom(
x; y
)
form a topological space, and composition
is a continuous map. There is a standard recipe to construct the ficlassifying spacefl of
any topological category, invented by Segal in the following paper:
5)
 Graeme B. Segal, fiClassifying spaces and spectral sequencesfl,
Pub. IHES
34
(1968),
105Œ112.
I described classifying spaces for discrete groups in
 fiWeek 70fl
, and the more general
case of discrete groupoids in
 fiWeek 75fl
. The construction for topological categories is
similar: we make a big space by sticking in one point for each object, one edge for each
morphism, one triangle for each composable pair of morphisms:
x
y
z
f
g f
g
f
:
x
!
y
g
:
y
!
z
g f
:
x
!
z
and so on. The only new trick is to make sure this space gets a topology in the right way
using the topologies on the spaces
Hom(
x; y
)
.
Anyway, if we form this classifying space from the topological category
C
coming
from the Morse function on our manifold
M
, we get a space homotopic to
M
! In other
words, for many topological purposes the category
C
is just as good as the manifold
M
itself.
6)
 Ross Street, fiDescent theoryfl, preprint of talks given at Oberwolfach, Sept. 17Œ23,
1995.
Ross Street, fiFusion operators and cocycloids in monoidal categoriesfl,
Appl. Cat.
Str.
6
(1998), 177Œ191.
Street is one of the gurus of
n
-category theory, which he notes fimight be called post-
modern algebra (or even `post-modern mathematics' since geometry and algebra are
handled equally well by higher categories).fl His paper fiDescent theoryfl serves as a
rapid introduction to
n
-categories. But the real point of the paper is to explain the
role
n
-categories play in cohomology theory: in particular, how to do cohomology with
coefcients in an
!
-category!
7)
 Viqar Husain, fiIntersecting-loop solutions of the hamiltonian constraint of quan-
tum general relativityfl,
Nucl. Phys. B
313
(1989), 711Œ724.
Viqar Husain and Karel V. Kuchar, fiGeneral covariance, new variables, and dynam-
ics without dynamicsfl,
Phys. Rev. D
42
(1990), 4070Œ4077.
Viqar Husain, fiEinstein's equations and the chiral modelfl,
Phys. Rev. D
53
(1996),
4327. Also available as
gr-qc/9602050
.
Viqar is one of the excellent younger folks at the Center for Gravitational Physics and
Geometry at Penn State; I only had a bit of time to speak with him during my last
169
 WEEK 82 MAY 17, 1996
visit there, but I got some of his papers. The rst paper is from the good old days
when folks were just beginning to nd explicit solutions of the constraints of quantum
gravity using the loop representation Š it's still worth reading! The second introduced
a eld theory now called the HusainŒKuchar model, which has the curious property
of resembling gravity without the dynamics. The third studies
4
-dimensional general
relativity assuming there are two commuting spacelike Killing vector elds. Here he
reduces the theory to a
2
-dimensional theory which appears to be completely integrable
Š though it has not been proved to be so in the sense of admitting a complete set of
Poisson-commuting conserved quantities.
8)
The Interface of Knots and Physics
, ed. Louis H. Kauffman, Proc. Symp. Appl. Math.
51
, AMS, Providence, 1996.
This slim volum e contains the proceedings of an AMS fishort coursefl on knots and physics
held in San Francisco in January 1995, namely:
Ł
 Louis H. Kauffman, fiKnots and statistical mechanicsfl
Ł
 Ruth J. Lawrence, fiAn introduction to topological eld theoryfl
Ł
 Dror Bar-Natan, fiVassiliev and quantum invariants of braidsfl
Ł
 Samuel J. Lomonaco, fiThe modern legacies of Thomson's atomic vortex theory in
classical electrodynamicsfl
Ł
 John C. Baez, fiSpin networks in nonperturbative quantum gravityfl
William Kingon Clifford
Born May 4th, 1845
Died March 3rd, 1879
I was not, and was conceived
I loved, and did a little work
I am not, and grieve not.
And
Lucy, his wife
Died April 21st, 1929
Oh, two such silver currents when they join
Do glorify the banks that bound them in.
Š William Clifford's tomb
170
 WEEK 83 JUNE 10, 1996
Week 83
June 10, 1996
I'll return to the Tale of
n
-Categories this week, and continue to explain the mysteries of
duals and inverses. But rst let me describe two new papers by Connes.
1)
 Alain Connes, fiGravity coupled with matter and the foundation of non-commutative
geometryfl, available as
hep-th/9603053
.
Ali H. Chamseddine and Alain Connes, fiThe spectral action principlefl, available as
hep-th/9606001
.
The second paper here lls in details that are missing from the rst. Hopefully lots of you
know that Connes is the wizard of operator theory who turned to inventing a new branch
of geometry, finoncommutative geometryfl. The idea of algebraic geometry is that we can
study a space by studying the functions on that space Š which typically form some kind
of commutative algebra. If we let the algebra become noncommutative, it is no longer
functions on some space, but we can pretend it is nonetheless, and do geometry by anal-
ogy with the commutative case. This is very much based on the philosophy of quantum
mechanics, where the observables form a noncommutative algebra, yet are analogous
to the commutative algebras of observables of classical mechanics, these commutative
algebras consisting simply of functions on the classical space states.
In quantum mechanics, the failure of two observables to commute implies that they
cannot always be simultaneously measured with arbitrary accuracy; there is a very pre-
cise mathematical statement of Heisenberg's uncertainty principle that makes this quan-
titative. We can thus think of noncommutative geometry as fiquantum geometryfl, geom-
etry where the uncertainty principle of quantum mechanics has infected the very notion
of space itself! In noncommutative geometry it impossible to simultaneously measure all
the coordinates of a point with arbitrary accuracy, because they do not commute!
For the denitive introduction to noncommutative geometry, see Connes' book fiNon-
commutative Geometryfl, reviewed in
 fiWeek 39fl
. Already in this book Connes, working
with Lott, was beginning to explore the idea that the geometry of our physical universe
is noncommutative. Actually, they used ideas from noncommutative geometry to study
a weird kind of commutative geometry in which spacetime is fitwo-sheetedflŠtwo copies
of standard
4
-dimensional spacetime, very close together. In normal geometry it doesn't
even make sense to speak of two separate copies of spacetime being ficlose togetherfl,
since there is no way to get from one to the other! Tricks from noncommutative geom-
etry allow it to make sense. They found something amazing: if you do
U(1)

SU(2)
YangŒMills theory on this spacetime, you get the Higgs particle for free!
Sorry for the jargon. What it means is this: in the Standard Model of particle physics
we describe the electromagnetic force and the weak nuclear force in a unied way using
a theory called fi
U(1)

SU(2)
YangŒMills theoryfl, but then we postulate an extra particle,
the Higgs particle, which has the effect of making the electromagnetic force work quite
differently from the weak force. We say it fibreaks the symmetryfl between the two
forces. It has not yet been observed, though particle physicists hope to see it (or not!)
in experiments coming up fairly soon. It is a rather puzzling, ad hoc element of the
171
 WEEK 83 JUNE 10, 1996
Standard Model. The amazing thing about the Connes-Lott model is that it arises in a
natural way from the fact that spacetime has two sheets.
Connes and Lott also studied the strong force, but now Connes has introduced gravity
into his model. I haven't had time to absorb this new work yet, so let me simply say
what his current model of spacetime is, and list some of the concrete predictions the
new theory makes. His spacetime is the noncommutative algebra consisting of smooth
functions on good old
4
-dimensional Minkowski spacetime, taking values in the algebra
A
given by the direct sum
A
=
C
+
H
+
M
3
(
C
)
where
C
is the complex numbers,
H
is the quaternions, and
M
3
(
C
)
is the
3

3
complex
matrices. (Exercise: redo Connes' model, replacing
M
3
(
C
)
with the octonions. Hint:
develop nonassociative geometry and use Geoffrey Dixon's theory relating the electro-
magnetic, weak, and strong forces to the complex numbers, quaternions, and octonions,
respectively. See
 fiWeek 59fl
 for references to Dixon's work, and an explanation of quater-
nions and octonions.)
The Chamseddine-Connes model predicts that the sine squared of the Weinberg angle
Š an important constant in the theory of the electroweak force Š is between
:
206
and
:
210
. Unfortunately this disagrees with the experimental value of
:
2325
, but it's sort of
surprising that they can derive something this close, since in the Standard Model the
Weinberg angle is just an arbitrary parameter. They also derive a Higgs mass of 160Œ180
GeV, and expect accuracy comparable to their prediction of the Weinberg angle (about
10%).
Well worth pondering!
There is an interesting analogy between the dual of a vector space and the inverse of a
number which I would like to explain now. I assume you know that multiplying numbers
is a lot like tensoring vector spaces. For example, just as multiplication distributes over
addition, tensoring distributes over direct sums. Also, just as there is a number called
1
which is the unit for multiplication, there is a
1
-dimensional vector space, the ground
eld itself, which is the unit for tensoring. Let me take the unusual liberty of writing
tensor products by juxtaposition, so that
xy
is the tensor product of the vector space
x
and the vector space
y
, and let me call the
1
-dimensional vector space that's the unit for
tensoring simply fi
1
fl.
Now, if a number
x
has an inverse
y
, we have
y x
= 1
and
1 =
xy :
Similarly, if a vector space
x
has a dual
y
, we have linear maps
e
:
y x
!
1
and
i
: 1
!
xy
172
 WEEK 83 JUNE 10, 1996
What are these linear maps? Well, the whole point of the dual vector space y is that a
vector in
y
is a linear functional from
x
to
1
. This fidual pairingfl between vectors in
y
and those in
x
denes a linear map
e
:
y x
!
1
, often called the ficounitfl. On the other
hand, the space
xy
can be thought of as the space of linear transformations of
x
. The
linear map
i
: 1
!
xy
sends any scalar (i.e., any vector in
1
) to the corresponding scalar
multiple of the identity transformation of
x
.
So we see that dual vector spaces are a bit like inverse numbers, except that we don't
have
y x
= 1
and
1 =
xy
, and we don't even have that
y x
is
isomorphic
to
1
and
1
is
isomorphic
to
xy
. We just have some maps going from
y x
to
1
, and from
1
to
xy
.
These maps satisfy two equations, though. Here's the rst. We start with
x
, use the
obvious isomorphism to map to
1
x
, then use
i
: 1
!
xy
to map this to
xy x
, then use
e
:
y x
!
1
to map this to
x
1
, and then use the other obvious isomorphism to map back to
x
. This composite of maps should be the identity on
x
. What this says is that the identity
linear transformation of
x
really acts as the identity!
Stealing a trick from
 fiWeek 79fl
, we can draw this as follows. Draw the counit
e
:
y x
!
1
as follows:
y
x

e
and draw the unit
i
: 1
!
xy
as follows:
x
y

i
Then the above equation says that
x
x
x
y
x
=
x
x
Here the left side, which we read from top to bottom, corresponds to the composite
x
!
1
x
!
xy x
!
x
1
!
x
. (The factors of
1
are invisible in the picture, since they don't
do much.) The left side corresponds to the identity map
x
!
x
.
The second equation goes like this. We start with
y
, use the obvious isomorphism to
map to
y
1
, then use the unit to map this to
y xy
, then use the counit to map this to
1
y
,
and then use the other obvious isomorphism to map back to
y
. This composite should be
the identity on
y
. What this says is that the identity linear transformation of
x
also acts
dually as the identity on
y
! We can draw this as follows:
y
y
y
x
y
=
y
y
173
 WEEK 83 JUNE 10, 1996
If you now steal a peek at
 fiWeek 79fl
, you'll see that these two equations are just the
same equations used to dene adjoint functors in category theory! What's going on?
Well, dual vector spaces are analogous to adjoint functors, clearly. But more deeply,
what we have is an analogy between duals in any category with tensor products Š or
fimonoidal categoryfl Š and adjoints in any
2
-category.
What's a monoidal category, exactly? Roughly it's a category with some sort of fitensor
productfl and fiunit objectfl. But we can precisely dene the so-called fistrictfl monoidal
categories as follows: they are simply
2
-categories with one object. (Turn to
 fiWeek 80fl
for a denition of
2
-categories.) A
2
-category has objects, morphisms, and
2
-morphisms,
but if there is only one object, we can do the following relabelling trick:
2-morphisms
7!
morphisms
morphisms
7!
objects
objects
7!
Namely, we can forget about the object, call the morphisms fiobjectsfl, and call the
2
-
morphisms fimorphismsfl. But since all the new fiobjectsfl were really morphisms from
the original single object to itself, they can all be composed, or fitensoredfl. That's why
we get a category with fitensor productfl, and similarly, a fiunit objectfl.
So, just as a category with one object is just a monoid, a
2
-category with one object
is a monoidal category! This is one instance of a trick that I sketched many more cases
of in
 fiWeek 74fl
.
Now, in
 fiWeek 79fl
 I dened left and right adjoints of functors between categories.
Here the only thing I really needed about category theory was that
Cat
is a
2
-category
with categories as its objects, functors as its morphisms, and natural transformations as
its 2-morphisms. So we can dene left and right adjoints of morphisms in any
2
-category
by analogy as follows:
Suppose
a
and
b
are objects in a
2
-category. Then we say that the morphism
L
:
a
!
b
is a fileft adjointfl of the morphism
R
:
b
!
a
(and
R
is a firight adjointfl of
L
) if there are
2
-morphisms
e
:
R L
)
1
b
i
: 1
a
)
LR
satisfying two magic equations. If we draw
e
and
i
as we did above,
y
x

e
x
y

i
174
 WEEK 83 JUNE 10, 1996
then the two magic equations are
L
L
L
R
L
=
L
L
and
R
R
R
L
R
=
R
R
Alternatively, we can state these equations using the
2
-categorical notation described
in
 fiWeek 80fl
, by saying that the following vertical composites of
2
-morphisms are iden-
tity morphisms:
L
= 1
a
L
i

1
L
==
)
LR L
1
L

e
===
)
L
1
a
=
L
and
R
=
R
1
a
1
R

i
===
)
R LR
e

1
R
===
)
1
b
R
=
R
where

denotes the horizontal composite. If you look at these, and compare them to the
graphical notation above, you'll see they are really saying the same thing.
The punchline is, when our
2
-category has one object, we can think of it as a monoidal
category, and then these equations are the denition of fidualsfl Š one example being our
earlier denition of dual vector spaces in the monoidal category Vect of vector spaces!
So adjoint functors and dual vector spaces are both instances of the general notion
of adjoint
1
-morphisms in a
2
-category. Adjointness is a very basic concept.
I hope all that made some sense.
If this category theory stuff seems confusing, maybe you should read a 3-volume book
about it! I can see you smiling, but seriously, I nd the following reference very useful
(despite a certain number of annoying errors). You can nd a lot of good stuff about
adjoint functors, monoidal categories, and much much more in here:
2)
 Francis Borceux,
Handbook of Categorical Algebra
, Cambridge U. Press 1994.
Vol-
ume 1: Basic Category Theory
.
Volume 2: Categories and Structure
.
Volume 3:
Categories of Sheaves
.
To continue reading the fiTale of
n
-Categoriesfl, see
 fiWeek 84fl
.
175
 WEEK 84 JUNE 27, 1996
Week 84
June 27, 1996
While I try to limit myself to mathematical physics in This Week's Finds, I can't always
keep it from spilling over into other subjects... so if you're not interested in comput-
ers, just skip down to reference 8 below. A while back on
sci.physics
Matt McIrvin
pointed out that the closest thing we have to the computer of old science ction Š the
underground behemoth attended by technicians in white lab coats that can answer any
question you type in Š is AltaVista. I agree wholeheartedly.
In case you are a few months or years behind on the technological front, let me
explain: these days there is a vast amount of material available on the World-Wide Web,
so that the problem has become one of locating what you are interested in. You can
do this with programs known as search engines. There are lots of search engines, but
my favorite these days is AltaVista, which is run by DEC, and seems to be especially
comprehensive. So these days if you want to know, say, the meaning of life, you can just
go to
1)
 AltaVista,
http://www.altavista.digital.com/
type in fimeaning of lifefl, and see what everyone has written about it. You'll be none
the wiser, of course, but that's how it always worked in those old science ction stories,
too.
The intelligence of AltaVista is of course far less than that of a fruit y. But Matt's
comment made me think about how now, as soon as we develop even a rudimentary form
of articial intelligence, it will immediately have access to vast reams of information on
the Web... and may start doing some surprising things.
An example of what I'm talking about is the CYC project, Doug Lenat's $35 million
project, begun in 1984, to write a program with common sense. In fact, the project plans
to set CYC loose on the web once it knows enough to learn something from it.
2)
 CYC project homepage,
http://www.cyc.com/
The idea behind CYC is to encode ficommon sensefl as about half a million rules
of thumb, declarative sentences which CYC can use to generate inferences. To have
any chance of success, these rules of thumb must be organized and manipulated very
carefully. One key aspect of this is CYC 's ontology Š the framework that lets it know, for
example, that you can eat 4 sandwiches, but not 4 colors or the number 4. Most of the
CYC code is proprietary, but the ontology will be made public in July of this year, they
say. One can already read about aspects of it in
3)
 Douglas B. Lenat and R.V. Guha,
Building Large Knowledge-Based Systems: Repre-
sentation and Inference in the Cyc Project
, Addison-Wesley, Reading, Mass., 1990.
My network of spies informs me that many hackers are rather suspicious of CYC. For
an interesting and somewhat critical account of CYC at one stage of its development, see
4)
 Vaughan Pratt, fiCYC Reportfl,
http://boole.stanford.edu/pub/cyc.report
176
 WEEK 84 JUNE 27, 1996
Turning to something that's already very practical, I was very pleased when I found
one could use AltaVista to do fibacklinksfl. Certainly the World-Wide Web is in part
inspired by Ted Nelson's visionary but ill-starred Xanadu project.
5)
 Project Xanadu,
http://xanadu.net/the.project
Backlinking is one of the most tricky parts of Ted Nelson's vision, one often declared
infeasible, but one upon which he has always insisted. Basically, the idea is that you
should always be able to nd all the documents pointing
to
a given document, as well as
those to which it points. This allows
commentary
or
annotation
: if you read something,
you can read what other people have written about it. My spies inform me that the
World-Wide Web Committee is moving in this direction, but it is exciting that one can
already do fibacklinks browsingfl with the help of a program written by Ted Kaehler:
6)
 Ted Kaehler's backlinks browser,
http://www.foresight.org/backlinks1.3.1.
html
Go to this page at the start of your browsing session. Follow the directions and let
it create a new Netscape window for you to browse in. Whenever you want backlinks,
click in the original page, and click fiLinks to Other Pagefl. This launches an AltaVista
search for links to the page you were just looking at.
It works quite nicely. I hope you try it, because with backlinking the Web will become
a much more interesting and useful place, and the more people who know about it, the
sooner it will catch on. For more discussion of backlinking, see
7)
 Backlinking news at the Foresight Institute,
http://www.foresight.org/backlinks.
news.html
Robin Hanson's ideas on backlinking,
http://www.hss.caltech.edu/~hanson/
findcritics.html
I thank my best buddy Bruce Smith for telling me about CYC, Project Xanadu, and
Ted Kaehler's backlinks browser.
Now let me turn to some mathematics and physics.
8)
 Francesco Fucito, Maurizio Martellini and Mauro Zeni, fiThe BF formalism for QCD
and quark connementfl, available as
hep-th/9605018
.
9)
 Ioannis Tsohantjis, Alex C Kalloniatis, and Peter D. Jarvis, fiChord diagrams and
BPHZ subtractionsfl, available as
hep-th/9604191
.
These two papers both treat interesting relationships between topology and quan-
tum eld theory Š not the fitopological quantum eld theoryfl beloved of effete math-
ematicians such as myself, but the pedestrian sort of quantum eld theory that ordi-
nary working physicists use to study particle physics. So we are seeing an interesting
cross-fertilization here: rst quantum eld theory got applied to topology, and now the
resulting ideas are getting applied back to particle physics.
Why don't we see quarks roaming the streets freely at night? Because they are con-
ned! Conned to the hadrons in which they reside, that is. We mainly see two sorts
of hadrons: baryons made of three quarks, like the proton and neutron, and mesons
177
 WEEK 84 JUNE 27, 1996
made of a quark and an antiquark, like the pion or kaon. Why are the quarks conned in
hadrons? Well, roughly it's because if you grab a quark inside a hadron and try to pull it
out, the force needed to pull it doesn't decrease as you pull it farther out; instead, it re-
mains about constant. Thus the energy grows linearly with the distance, and eventually
you have put enough energy into the hadron to create another quark-antiquark pair, and
pop
Š you nd you are holding not a single quark but a quark together with a newly
born antiquark, that is, a meson! What's left is a hadron with a newly born quark as the
replacement for the one you tried to pull out!
That's a pretty heuristic description. In fact, particle physicists do not usually grab
hadrons and try to wrest quarks from them with their bare hands. Instead they smash
hadrons and other particles at each other and study the debris. But as a rough sketch of
the theory of quark connement, the above description is not
completely
silly.
There are various interesting things left to do, though. One is to try to get those
quarks out by means of sneaky tricks. The only way known is to
heat
a bunch of hadrons
to ridiculously high temperatures, preferably at ridiculously high pressures. I'm talking
temperatures like 2 trillion degrees, and densities comparable to that of nuclear matter!
This should yield a fiquark-gluon plasmafl in which quarks can zip around freely at enor-
mous energies. That's what the folks at the Relativistic Heavy Ion Collider are doing Š
see
 fiWeek 76fl
 for more.
This should certainly keep the experimentalists entertained. On the other hand, the-
orists can have lots of fun trying to understand more deeply why quarks are conned.
We'd like best to derive connement in some fairly clear and fairly rigorous way from
quantum chromodynamics, or QCD Š our current theory of the strong force, the force
that binds the quarks together. Unfortunately, mathematical physicists are still struggling
to formulate QCD in a rigorous way, so they can't yet turn to the exciting challenge of
proving that connement follows from QCD. And we certainly don't expect any simple
way to fiexactly solvefl QCD, since it is complicated and highly nonlinear. So what some
people do instead is computer simulations of QCD, in which they approximate spacetime
by a lattice and do a lot of number-crunching. They usually use a fairly measly-sounding
grid of something like
16

16

16

16
sites or so, since currently calculations take too
long when the lattice gets much bigger than that.
Numerical calculations like these have a lot of potential. In
 fiWeek 68fl
, for example,
I talked about how people found numerical evidence for the existence of a figlueballfl Š
a hadron made of no quarks, just gluons, the gluon being the particle that carries the
strong force. This glueball candidate seems to match the features of an observed particle!
Also, people have put a lot of work into computing the masses of more familiar hadrons.
So far I believe they have concentrated on mesons, which are simpler. Eventually we
should in principle be able to calculate things like the mass of the proton and neutron Š
which would be really thrilling, I think. Numerical calculations have also yielded a lot of
numerical evidence that QCD predicts connement.
Still, one would very much like some conceptual explanation for connement, even
if it's not quite rigorous. One way people try to understand it is in terms of fidual su-
perconductivityfl. In certain superconductors, magnetic elds can only penetrate as long
narrow tubes of magnetic ux. (For example, this happens in neutron stars Š see
 fiWeek
37fl
.) Now, just as electromagnetism consists of an fielectricfl part and a fimagneticfl part,
so does the strong force. But the idea is that connement is due to the
electric
part of
the strong force only being able to penetrate the vacuum in the form of long narrow
178
 WEEK 84 JUNE 27, 1996
tubes of eld lines. The electric and magnetic elds are fidualfl to each other in a precise
mathematical sense, so this is referred to as dual superconductivity. Quarks have the
strong force version of electric charge Š called ficolorfl Š and when we try to pull two
quarks apart, the strong electric eld gets pulled into a long tube. This is why the force
remains constant rather than diminishing as the distance between the quarks increases.
A while back, 't Hooft proposed an idea for studying connement in terms of dual
superconductivity and certain fiorderfl and fidisorderfl observables. It seems this idea has
languished to some extent due to a lack of necessary mathematical infrastructure. For
the last couple of years, Martellini has been suggesting to use ideas from topological
quantum eld theory to serve this role. In particular, he suggested treating YangŒMills
theory as a perturbation of
B F
theory, and applying some of the ideas of Witten and
Seiberg (who related connement in the supersymmetric generalization of YangŒMills
theory to Donaldson theory). In the paper with Fucito and Zeni, they make some of
these ideas precise. There are still some potentially serious loose ends, so I am very
interested to hear the reaction of others working on connement.
I have not studied the paper of Tsohantjis, Kalloniatis, and Jarvis in any detail, but
people studying Vassiliev invariants might nd it interesting, since it claims to relate the
renormalization theory of
'
3
theory to the mathematics of chord diagrams.
10)
 Masaki Kashiwara and Yoshihisa Saito, fiGeometric construction of crystal basesfl,
q-alg/9606009
.
The ficanonicalfl and ficrystalfl bases associated to quantum groups, studied by Kashiwara,
Lusztig, and others, are exciting to me because they indicate that the quantum groups are
just the tip of a still richer structure. Whenever you see an algebraic structure with a basis
in which the structure constants are nonnegative integers, you should suspect that you
are really working with a category of some sort, but in boiled-down or fidecategoriedfl
form.
Consider for example the representation ring
R
(
G
)
of a group
G
. This is a ring
whose elements are just the isomorphism classes of nite-dimensional representations
of
G
. Addition in
R
(
G
)
corresponds to taking the direct sum of representations, while
multiplication corresponds to taking the tensor product. Thus for example if
x
and
y
are irreducible representations of
G
Š or fiirrepsfl for short Š and
[
x
]
and
[
y
]
are the
corresponding basis elements of
R
(
G
)
, the product
[
x
][
y
]
is equal to a linear combina-
tion of the irreps appearing in
x


y
. These coefcients
are therefore nonnegative integers. They are an example of what I'm calling fistructure
constantsfl.
What's happening here is that the ring
R
(
G
)
is serving as a fidecategoriedfl version
of the category
Rep
(
G
)
of representations of the group
G
. Almost everything about
R
(
G
)
is just a decategoried version of something about
Rep
(
G
)
. For example,
R
(
G
)
is a
monoid under multiplication, while
Rep
(
G
)
is a monoidal category under tensor product.
R
(
G
)
is actually a commutative monoid, while
Rep
(
G
)
is a symmetric monoidal category
Š this being jargon for how the tensor product is ficommutativefl up to a nice sort of
isomorphism. In
R
(
G
)
we have addition, while in
Rep
(
G
)
we have direct sums, which
category theorists would call fibiproductsfl. And so on. The representation ring is a
common tool in group theory, but a lot of the reason for working with
R
(
G
)
is simply
179
 WEEK 84 JUNE 27, 1996
that we don't know enough about category theory and are too scared to work directly
with
Rep
(
G
)
. There are also
good
reasons for working with
R
(
G
)
, basically
because
it is
simpler and contains less information than
Rep
(
G
)
.
We can imagine that if someone handed us a representation ring
R
(
G
)
we might
eventually notice that it had a nice basis in which the structure constants were nonneg-
ative integers. And we might then realize that lurking behind it was a category,
Rep
(
G
)
.
And then all sorts of things about it would become clearer. . . .
Something similar like this seems to be happening with quantum groups! Ignoring a
lot of important technical details, let me just say that quantum groups turn out have nice
bases in which the structure constants are nonnegative integers, and the reason is that
lurking behind the quantum groups are certain categories. What sort of categories? Cat-
egories of fiLagrangian subvarieties of the cotangent bundles of quiver varietiesfl. Yikes!
I don't think I'll explain
that
mouthful! Let me just note that a quiver is itself a cute little
category that you cook up by taking a graph and thinking of the vertices as objects and
the edges as morphisms, like this:
 !  !  !  ! 
If you do this to a graph that's the Dynkin diagram of a Lie group Š see
 fiWeek 62fl
 and
the weeks following that Š then the fun starts! Dynkin diagrams give Lie groups, but
also quantum groups, and now it turns out that they also give rise to certain categories
of which the quantum groups are decategoried, boiled-down versions. . . . I don't un-
derstand all this, but I certainly intend to, because it's simply amazing how a world of
complex symmetry emerges from these Dynkin diagrams.
For more on this stuff try the paper by Crane and Frenkel referred to in
 fiWeek 38fl
 and
fiWeek 50fl
. It suggests some amazing relationships between this stuff and
4
-dimensional
topology. . . .
Let me conclude by reminding you where I am in the fiTale of
n
-Categoriesfl, and
where I want to go next. So far I have spoken mainly of 0-categories,
1
-categories, and
2
-categories, with lots of vague allusions as to how various patterns generalize to higher
n
. Also, I have concentrated mainly on the related notions of equality, isomorphism,
equivalence, and adjointness. Equality, isomorphism and equivalence are the most natu-
ral notions of fisamenessfl when working in 0-categories,
1
-categories, and
2
-categories,
respectively. Adjointness is a closely related but more subtle and exciting concept that
you can only start talking about once you get to the level of
2
-categories. People got
tremendously excited by it when they started working with the
2
-category
Cat
of all
small categories, because it explained a vast number of situations where you have a way
to go back and forth between two categories, without the categories being fithe samefl
(or equivalent). Another exciting thing about adjointness is that it really highlights the
relation between
2
-categories and
2
-dimensional topology Š thus pointing the way to a
more general relation between
n
-categories and
n
-dimensional topology. From this point
of view, adjointness is all about fifoldsfl:
180
 WEEK 84 JUNE 27, 1996
and their ability to cancel:
=
=
This concept of fidoubling backfl or fibacktrackingfl is a very simple and powerful one,
so it's not surprising that it is prevalent throughout mathematics and physics. It is an
essentially
2
-dimensional phenomenon (though it occurs in higher dimensions as well),
so it can be understood most generally in the language of
2
-categories.
(In physics, fidoubling backfl is related to the notion of antiparticles as particle moving
backwards in time, and appears in the Feynman diagrams for annihilation and creation
of particle/antiparticle pairs. For those familiar with the category-theoretic approach to
Feynman diagrams, the stuff in
 fiWeek 83fl
 about dual vector spaces should sufce to
make this connection precise.)
Next I will talk about another
2
-dimensional concept, the concept of fijoiningfl or
fimergingfl:
This is probably even more powerful than the concept of fifoldingfl: it shows up whenever
we add numbers, multiply numbers, or in many other ways combine things. The
2
-
categorical way to understand this is as follows. Suppose we have an object
x
in a
2
-category, and a morphism
f
:
x
!
x
. Then we can ask for a
2
-morphism
M
:
f
2
)
f :
If we have such a thing, we can draw it as a traditional
2
-categorical diagram:
x
x
x
f
f
f
M
181
 WEEK 84 JUNE 27, 1996
or dually as a fistring diagramfl
f
f

M
f
Regardless of how you draw it, the
2
-morphism
M
:
f
2
)
f
represents a process turning
two copies of
f
into one. And as we'll see, all sorts of fancy ways mathematicians have
of studying this sort of process Š fimonoidsfl, fimonoidal categoriesfl, and fimonadsfl Š
are special cases of this sort of situation.
To continue reading the fiTale of
n
-Categoriesfl, see
 fiWeek 89fl
.
182
 WEEK 85 JULY 14, 1996
Week 85
July 14, 1996
I'm spending this month at the Erwin Schr
¨
odinger Institute in Vienna, where Abhay
Ashtekar and Peter Aichelburg are running a workshop called Mathematical Problems of
Quantum Gravity.
Ashtekar is one of the founders of an approach to quantizing gravity called the loop
representation. I've explained this approach in
 fiWeek 7fl
,
 fiWeek 43fl
, and other places,
but let me just remind you of the basic idea. In the traditional approach to reconciling
general relativity with quantum theory, excitations of the gravitational eld were de-
scribed by small ripples in the geometry of at spacetime, or figravitonsfl. In the loop
representation, they are instead described by collections of loops, which we can think of
as fiux tubes of areafl oating in an otherwise utterly featureless void. More recently,
the loop approach has been supplemented by a technical device known as fispin net-
worksfl: roughly speaking, a spin network is a graph whose edges are labelled by spins
0
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
with an edge of spin
j
corresponding to a ux tube carrying area equal
to
p
j
(
j
+ 1)
times the square of the Planck length Š the fundamental length scale in
quantum gravity, about
10

35
meters. For more on spin networks, try
 fiWeek 55fl
.
Quantum gravity has always been a tough subject. After a lot of work, a lot of
people concluded that the traditional approach to quantum gravity didn't make sense,
mathematically. This led to string theory, an attempt to quantize gravity together with
all the other forces and particles. But in the late 1980s, Rovelli and Smolin revived hopes
of quantizing gravity alone by introducing the loop representation.
One doesn't expect the loop representation to describe much real physics until one
introduces other forces and particles. Pure gravity is just a warm-up exercise Š but it's
not at all easy! When the loop representation was born, it was rather sketchy at many
points. A lot of mathematical problems had to be overcome to make it as precise as it
is now. . . . and there are a lot of formidable difculties left, any one of which could
spell doom for the theory. Luckily, progress has been rapid. Many of the problems which
seemed hopelessly beyond our reach a few years ago can now be formulated precisely,
and maybe even solved. The idea of this workshop is to start tackling these problems.
A lot has been going on! People give talks at 11 in the morning, while afternoons are
devoted to more informal discussions in small groups. There are general introductory
talks on Tuesdays, more technical talks on Thursdays, and short talks on research in
progress on some other days.
To give a bit of the avor of the workshop, let me describe things day by day. I'll need
to describe some days very sketchily, though, or I'll never nish writing this!
Ł
Wednesday, July 3
Š Rodolfo Gambini spoke on gauge-invariance in the extended
loop representation. The idea of the loop representation is to study the gravita-
tional vector potential by studying certain integrals of it around loops. Mathemati-
cians call this the trace of the holonomy, and physicists call it a Wilson loop or the
trace of a path-ordered exponential. In the loop representation, states of quan-
tum gravity are described by certain functions that eat Wilson loops and spit out
complex numbers... i.e., that assign an fiamplitudefl to each Wilson loop.
183
 WEEK 85 JULY 14, 1996
In quantum eld theory you often need to average a quantum eld over some
3
-dimensional region of space or
4
-dimensional region of spacetime to get a well-
dened operator. Wilson loops are rather singular because a loop is a one-dimensional
object. On the other hand, they are nice because they are gauge-invariant: they
don't change when we do a gauge transformation to the vector potential.
In the fiextendedfl loop representation one tries to make the integral less singu-
lar by not dealing with actual loops, but certain analogous integrals over all
3
-
dimensional space. Heuristic calculations suggest that they are gauge-invariant,
but Troy Schilling noticed a while ago that they aren't always
really
gauge-invariant
Š basically because the the path-ordered exponential is given by a certain Taylor
series, and nasty things can happen when you manipulate innite series without
checking if your manipulations are legitimate! See:
1)
 Troy Schilling, fiNon-covariance of the generalized holonomies: Examplesfl,
available as
gr-qc/9503064
.
There has been a certain amount of competition between the extended loop repre-
sentation, developed by Gambini and various coauthors, and Ashtekar's approach.
Thus Schilling's result was seen as a blow against the extended loop representa-
tion. In Gambini's talk, he argued that gauge-invariance is rigorously maintained
by certain extended loops, e.g. those for which the power series has nitely many
terms. The most famous examples of functions of extended loops with only nitely
many terms are the Vassiliev invariants, which come up in knot theory (see
 fiWeek
3fl
). Gambini and Pullin have claimed that certain Vassiliev invariants are states of
quantum gravity, so these are of special interest.
The feeling was that we needed to compare these different loop representations
more carefully because they both have advantages.
Also, Renate Loll spoke about fiLattice Gravityfl. See
 fiWeek 55fl
 for a bit more
on this. Her talk led to an interesting discussion of the meaning of the limit, as
the lattice spacing goes to zero, of quantum gravity as done on a lattice. Does it
make sense? One needs, apparently, to look at ones formula for the Hamiltonian
constraint on the lattice, and see if it depends on the Planck length in a manner
other than
having the Planck length as an overall prefactor. Various people tried to
do the calculation on the spot, and got mixed up.
Ł
Thursday, July 4
Š Thomas Thiemann spoke on fiThe Hamiltonian Constraint for
Lorentzian Canonical Quantum Gravityfl. This was a big bombshell. The Hamilto-
nian constraint in quantum gravity is one of the biggest, baddest problems we are
facing. It's the analog of Schrodinger's equation in quantum mechanics, but it's a
constraint:
H  
= 0
:
All the dynamics of the theory is contained in this equation, yet we only roughly
understand how to dene it in a rigorous way. Thiemann, a student of Ashtekar
who is now a postdoc at Harvard, had put the following 5 papers on the general
relativity preprint server right before the workshop. The rst one gives a rigorous
denition of the Hamiltonian constraint!
184
 WEEK 85 JULY 14, 1996
2)
 Thomas Thiemann, fiQuantum Spin Dynamics (QSD)fl, available as
gr-qc/
9606089
.
Thomas Thiemann, fiQuantum Spin Dynamics (QSD) IIfl, available as
gr-qc/
9606090
.
Thomas Thiemann, fiAnomaly-free formulation of non-perturbative, four-
dimensional Lorentzian quantum gravityfl,
Phys. Lett. B
380
(1996) 257Œ264.
Also available as
gr-qc/9606088
.
Thomas Thiemann, fiClosed formula for the matrix elements of the volume
operator in canonical quantum gravityfl, available as
gr-qc/9606091
.
Thomas Thiemann, fiA length operator for canonical quantum gravityfl, avail-
able as
gr-qc/9606092
.
It is interesting to compare fiQuantum Spin Dynamicsfl to the paper by Ashtekar
and Lewandowksi, so far available only in draft form to a select few, in which they
gave a rigorous denition of the square root of the Hamiltonian constraint. The
advantage of fiQSDfl is that it deals directly with the Hamiltonian constraint, rather
than its square root, and that it does this using some ingenious formulas for the
Hamiltonian constraint of Lorentzian gravity in terms of the Hamiltonian constraint
for Riemannian gravity and the total volume and total extrinsic curvature of the
universe (which we assume is compact).
You see, quantum gravity comes in two avors, Lorentzian and Riemannian, de-
pending on whether we work with real time Š the obviously sensible thing to do
Š or imaginary time Š not at all obviously sensible, but with a curious math-
ematical charm to it, which has won many hearts. The interplay between these
two has long been a bugaboo of the loop representation. The Lorentzian theory
is harder to work with, so lots of people cheat and study the Riemannian theory.
Sometimes they do this covertly, with a guilty conscience, so in some papers it's
left unclear which theory the author is actually working with! Thiemann's work,
however, seems to exploit the interplay between the theories in a benign way Š
related to earlier ideas of Ashtekar, but different. I would like to understand this
interplay more deeply.
Due to jetlag I woke up at 4 am on the morning of this talk, and I couldn't get back
to sleep, so I read his paper. When I came to the Institute at 9 am Š a shockingly
early hour for people working on quantum gravity Š I was sure nobody would be
there yet. But as I entered I bumped into Carlo Rovelli. It turned out he had stayed
up all night reading Thiemann's paper, too excited to sleep!
After this talk everyone was busily trying to learn Thiemann's stuff, trying to gure
out if it is physically correct, and trying to gure out what to do next.
Ł
Tuesday, July 9
Š Abhay Ashtekar gave a general talk on the fiQuantum Theory
of Geometryfl. Most of it was well-known stuff to fans of the loop representation,
but one new tidbit concerned the noncommutativity of area operators. Since the
area of surfaces in space depends only on the metric on space, not on its rst time
derivative, one might expect their quantum analogs to commute, since the metric
and its rst time derivative are analogous to position and momentum in quantum
mechanics. But they don't commute! In a later talk, Ashtekar explained that this is
185
 WEEK 85 JULY 14, 1996
not really a strange new feature of quantum gravity, but one which has its classical
analog.
Ł
Wednesday, July 10
Š Kirill Krasnov gave a talk on a paper we started working
on together just recently, fiQuantization of diffeomorphism invariant theories with
fermionsfl. Kirill is a young Ukrainian physicist whom I rst met last summer in
Warsaw; he had written a nice paper on the loop representation of quantum gravity
coupled to electromagnetism and fermions:
3)
 Kirill Krasnov, fiQuantum loop representation for fermions coupled to EisteinŒ
Maxwell eldfl,
Phys. Rev. D
53
(1996), 1874; available as
gr-qc/9506029
.
When I met him again here, it turned out he was continuing this work, and also
making it more rigorous. Now, I had for some time been meaning to write some-
thing with Hugo Morales-Tecotl showing that a slight generalization of spin net-
work states form a basis of states for such theories. These states had already ap-
peared, for example, in his work with Rovelli:
4)
 Carlo Rovelli and Hugo Morales-Tecotl, fiFermions in quantum gravityfl,
Phys.
Rev. Lett.
72
(1994), 3642Œ3645.
Carlo Rovelli and Hugo Morales-Tecotl,
Nucl. Phys. B
451
(1995), 325. Also
available as
gr-qc/9401011
.
But we had never gotten around to it. So, I decided to team up with Kirill and
write a paper on this stuff.
186
 WEEK 86 AUGUST 6, 1996
Week 86
August 6, 1996
Let me continue my reportage of what happened at the Mathematical Problems of Quan-
tum Gravity workshop in Vienna. I will only write about quantum gravity aspects here.
I had an interesting conversation with Bertram Kostant in which he explained to me the
deep inner secrets of the exceptional Lie group
E
8
. However, my writeup of that has
grown to the point where I will save it for some other week.
By the way, my course on
n
-category theory is not over! I'm merely taking a break
from it, and will return to it after this workshop.
So....
Ł
Wednesday, July 10th
Š Jerzy Lewandowski gave a talk on the fiSpectrum of the
Area Operatorfl. As I've mentioned a few times before, one of the exciting things
about the loop representation of quantum gravity is that the spectrum of the area
operator associated to any surface is discrete. In other words, area is quantized!
Let me describe the area operator a bit more precisely. Before I tell you what the
area operator is, I have to tell you what it operates on. Remember from
 fiWeek 43fl
that there are various Hilbert spaces oating around in the canonical quantization
of gravity. First there is the fikinematical state spacefl. In the old-fashioned metric
approach to quantum gravity, known as geometrodynamics, this was supposed
to be
L
2
(Met)
, where
Met
is the space of Riemannian metrics on space. (We
take as space some 3-manifold
S
, which for simplicity we assume is compact.)
The problem was that nobody knew how to rigorously dene this Hilbert space
L
2
(Met)
. In the finew variablesfl approach to quantum gravity, the kinematical
state space is taken instead to be
L
2
(
A
)
, where
A
is the space of connections on
some trivial
SU(2)
bundle over
S
. This
can
be dened rigorously.
Here's the idea, roughly. Fix any graph
g
, with nitely many edges and vertices,
embedded in
S
. Let
A
g
, the space of connections on that graph, be
SU(2)
n
where
n
is the number of edges in
e
. Thus a connection on a graph tells us how to
parallel transport things along each edge of that graph Š an idea familiar from
lattice gauge theory.
L
2
(
A
g
)
is well-dened because
SU(2)
has a nice measure on
it, namely Haar measure, so
A
g
gets a nice measure on it as well.
Now if one graph
g
is contained in another graph
h
, the space
L
2
(
A
g
)
is contained
in the space
L
2
(
A
h
)
in an obvious way. So we can form the union of all the Hilbert
spaces
L
2
(
A
g
)
and get a big Hilbert space
L
2
(
A
)
. Mathematicians would say that
L
2
(
A
)
is the fiprojective limitfl of the Hilbert spaces
L
2
(
A
g
)
, but let's not worry
about that.
So that's how we get the space of fikinematical statesfl in the loop representation
of quantum gravity. The space of physical states is then obtained by imposing
constraints: the Gauss law constraint (i.e., gauge-invariance), the diffeomorphism
constraint (i.e., invariance under diffeomorphisms of S) and the Hamiltonian con-
straint (i.e., invariance under time evolution). States in the physical state space are
supposed to only contain information that's invariant under all coordinate trans-
formations and gauge transformations Š the really physical information.
187
 WEEK 86 AUGUST 6, 1996
I explained these constraints to some extent in
 fiWeek 43fl
, and I don't really want
to worry about them here. But let me just mention that the Gauss law constraint is
easy to impose in a mathematically rigorous way. The diffeomorphism constraint
is harder but still possible, and the Hamiltonian constraint is the big thorny ques-
tion plaguing quantum gravity Š see
 fiWeek 85fl
 for some recent progress on this.
The area operators I'll be talking about are self-adjoint operators on the space of
kinematical states,
L
2
(
A
)
, and are a preliminary version of some related operators
one hopes eventually to get on the physical state space, after much struggle and
sweat.
To dene an operator on
L
2
(
A
)
it's enough to dene it on
L
2
(
A
g
)
for every graph
g
and then check that these denitions t together consistently to give an operator
on the big space
L
2
(
A
)
. So let's take a graph
g
and a surface
s
in space. The area
operator we're after is supposed to be the quantum analog of the usual classical
formula for the area of
s
. The usual classical area is a function of the metric on
space; similarly, the quantum area is an operator on the space
L
2
(
A
)
.
The area operator only cares about the points where the graph intersects the sur-
face. We assume that there are only nitely many points where it does so, apart
from points where the edges are tangent to the surface. (To make this assumption
reasonable, we need to assume, e.g., that the space
S
has a real-analytic structure
and the surface and graph are analytic Š an annoying technicality that I have been
seeking to eliminate.)
The area operator is built using three operators on
L
2
(SU(2))
called
J
1
,
J
2
, and
J
3
, the self-adjoint operators corresponding to the 3 generators of
SU(2)
Š which
often show up in physics as the three components of angular momentum! Alter-
natively, we can think of all three together as one vector-valued operator
J
, the
fiangular momentum operatorfl. Note that
L
2
(
A
g
)
is just the tensor product of one
copy of the Hilbert space
L
2
(SU(2))
for each edge of our graph
g
. Thus for any edge
e
we get an angular momentum operator
J
(
e
)
that acts on the copy of
L
2
(SU(2))
corresponding to the edge
e
in question, leaving the other copies alone.
This, then, is how we dene the operator on
L
2
(
A
g
)
corresponding to the area of
the surface
s
. Pick an orientation for the surface
s
. For any point where the graph
g
intersects
s
, let
J
(in)
denote the sum of the angular momentum operators of
all edges intersecting
s
at the point in question and pointing fiinwardsfl relative to
our chosen orientation. Similarly, let
J
(out)
be the sum of the angular momentum
operators of edges intersecting
s
at the point in question and pointing fioutwardsfl.
(Note: edges tangent to the surface contribute neither to
J
(in)
nor
J
(out)
.) Now
sum up, over all points where the graph intersects the surface, the following quan-
tity:
p
(
J
(in)

J
(out))
where the dot denotes the obvious sort of dot product of vector-valued operators.
Multiply by half the Planck length squared and you've got the area operator!
This very beautiful and simple formula was derived by Ashtekar and Lewandowski,
but the rst people to try to quantize the area operator were Rovelli and Smolin;
see
188
 WEEK 86 AUGUST 6, 1996
1)
 Carlo Rovelli and Lee Smolin, fiDiscreteness of area and volume in quantum
gravityfl,
Nucl. Phys. B
442
(1995), 593Œ619. Also available as
gr-qc/
9411005
.
Abhay Ashtekar and Jerzy Lewandowski, fiQuantum theory of geometry I:
area operatorsfl,
Class. Quant. Grav.
14
(1997) A55. Also available as
gr-qc/
9602046
.
In his talk Jerzy showed how to work the spectrum of the area operator (which
is discrete) and showed how it could depend on whether the surface
s
cuts space
into two parts or not.
Later that day, Mike Reisenberger, Matthias Blau, Carlo Rovelli and I talked about
the relation between string theory and the loop representation of quantum gravity.
Mike has been working on a very interesting fistate sum modelfl for quantum grav-
ity; that is, a discretized model in which spacetime is made of
4
-simplices (the 4d
version of tetrahedra), elds are thought of as ways of labelling the faces, edges
and so on by spins, elements of
SU(2)
and the like, and the path integral is replaced
by a sum over these labellings. This works out quite nicely for quantum gravity in
3 dimensions Š see
 fiWeek 16fl
 Š but it's much more challenging in 4 dimensions.
One nice feature of these state sum models for quantum gravity is that they may be
reinterpreted as sums over fiworldsheetsfl Š surfaces mapped into spacetime. Since
the spacetime is discrete, so are these surfaces Š they're made of lots of triangles
Š but apart from that, having a path integral that's a sum over worldsheets is
pleasantly reminscent of string theory. Indeed, once upon a time I proposed that
the loop representation of quantum gravity and string theory were two aspects of
some theory still waiting to be fully understood:
2)
 John Baez, fiStrings, loops, knots, and gauge eldsfl, in
Knots and Quantum
Gravity
, ed. J. Baez, Oxford U. Press, Oxford, 1994. Available as
hep-th/
9309067
, 34 pages.
The problem was getting a concrete way to relate the Lagrangian for the string
theory to the Lagrangian for gravity (or whatever gauge theory one started with).
Iwasaki tackled this problem in 3d quantum gravity using state sum models:
3)
 Junichi Iwasaki, fiA reformulation of the Ponzano-Regge quantum gravity model
in terms of surfacesfl, University of Pittsburgh, 11 pages in LaTeX format avail-
able as
gr-qc/9410010
.
Later, Reisenberger extended this approach to deal with certain 4d theories which
are simpler than quantum gravity, like
B F
theory:
4)
 Michael Reisenberger, fiWorldsheet formulations of gauge theories and grav-
ityfl, available as
gr-qc/9412035
.
In all of these theories, one computes the action for the worldsheets by summing
something over places where they intersect. In other words, they fiinteractfl at
intersections.
189
 WEEK 86 AUGUST 6, 1996
But the really exciting thing would be to do something like this for Mike's new state
sum model for 4d quantum gravity. And the real challenge would be to relate this
Š if possible! Š to conventional string theory. In a coffeeshop I suggested that one
might do this by using the usual formula for the action in (bosonic) string theory.
This is simply the
area
of the string worldsheet with respect to some background
metric. The loop representation of quantum gravity doesn't make reference to any
background metric; the closest approximation to a classical metric is a fiweavefl
state in which space is tightly packed with lots of loops or spin networks. From
the 4d point of view, we'd expect this to correspond to a spacetime packed with
lots of worldsheets. Now, given the relation between area and intersection num-
ber in the loop representation (see above!), one might expect the area of a given
worldsheet to be roughly proportional to the number of its intersections with the
other worldsheets in this fiweavefl. But this is what one would expect in any theory
where the worldsheets interact at intersections. So, one could hope that Mike's
state sum model would be approximately equivalent to a string theory of the sort
string theorists study.
There are lots of obvious problems with this idea, but it led to an interesting con-
versation, and I am still not convinced that it is crazy.
Ł
Thursday, July 11th
Š Jorge Pullin spoke on skein relations and the Hamiltonian
constraint in lattice quantum gravity. His idea was that the Hamiltonian constraint
contains a fitopological factorfl which serves as a skein relation on loop states.
Ł
Friday, July 12th
Š Abhay Ashtekar gave a talk on fiNoncommutativity of Area
Operatorsfl. This explained how the rather shocking fact that the area operators
for two intersecting surfaces needn't commute actually has a perfect analog in
classical general relativity.
Mike Reisenberger spoke on fiEuclidean Simplicial GRfl. This presented the details
of his state sum model. Since he hasn't published this yet, and since I am getting a
bit tired out, I won't describe it here.
Ł
Monday, July 15th
Š Renate Loll gave a talk on the volume and area operators in
lattice gravity. I wrote a bit about her work on the volume operator in
 fiWeek 55fl
,
and more can be found in:
5)
 Renate Loll, fiThe volume operator in discretized quantum gravityfl, available
as
gr-qc/9506014
.
Renate Loll, fiSpectrum of the volume operator in quantum gravityfl, available
as
gr-qc/9511030
.
Also, Jerzy Lewandowski spoke on his work with Ashtekar on the volume operator
in the continuum theory:
6)
 Jerzy Lewandowski, fiVolume and quantizationsfl, available as
gr-qc/9602035
.
Abhay Ashtekar and Jerzy Lewandowski, fiQuantum theory of geometry II:
volume operatorsfl, manuscript in preparation.
190
 WEEK 86 AUGUST 6, 1996
The volume operator is more tricky than the area operator, and various proposed
formulas for it do not agree. This is summarized quite clearly in Jerzy's paper.
In fact, I have already left Vienna by now. I was too busy there to keep up with This
Week's Finds, but my life is a bit calmer now and I will try to nish these reports
soon.
191
 WEEK 87 AUGUST 20, 1996
Week 87
August 20, 1996
Let me continue summarizing what happened during July at the Mathematical Problems
of Quantum Gravity workshop in Vienna. The rst two weeks concentrated on the foun-
dations of the loop representation of quantum gravity; the next week was all about black
holes!
Ł
Tuesday, July 16th
Š Ted Jacobson gave an overview of fiIssues of Black Hole
Thermodynamicsfl. There is a lot to say about this subject and I won't try to repeat
his marvelous talk here. Let me just mention a very interesting technical point he
made. The original Bekenstein-Hawking formula for the entropy of a black hole is
S
=
A=
(4
~
G
)
where
A
is the area of the event horizon,
~
is Planck's constant, and G is Newton's
constant. One way to try to derive this is from the partition function of a quantum
eld theory involving gravity and other elds. Jacobson sketched a heuristic cal-
culation along these lines. When you do this calculation it's natural to worry why
the other elds, representing various forms of matter, don't seem to contribute
to the answer above. Also, when we do quantum eld theory, there is often a
difference between the fibarefl coupling constants we put into the theory and the
firenormalizedfl coupling constants that are what the theory predicts we'll observe
experimentally. So it's natural to worry about whether it's the bare or renormalized
Newton's constant
G
that enters the above formula Š even though quantum grav-
ity is so unlike most other quantum eld theories that it's unclear that this worry
makes sense, ultimately.
Anyway, the nice thing is that these two worries cancel each other out. In other
words: yes, it's the renormalized Newton's constant
G
Š the physically measured
one Š that enters the above formula. But at least to rst order in
~
, the difference
between the bare
G
and the renormalized
G
is precisely due to the interactions
between gravity and the matter elds (including the self-interaction of the gravita-
tional eld). In other words, the matter elds really
do
contribute to the black hole
entropy, but this contribution is absorbed into the denition of the renormalized
G
.
In the most extreme case, the bare
1
=G
is zero, and the renormalized
1
=G
is entirely
due to interactions between matter and gravity. This is Andrei Sakharov's theory
of fiinduced gravityfl. According to Jacobson, in this case all of the black hole
entropy is fientanglement entropyfl Š this being standard jargon for the way that
two parts of a quantum system can each have entropy due to correlations, even
though the whole system has zero entropy. Unfortunately my notes do not allow
me to reconstruct the wonderful argument whereby he showed this. (See
 fiWeek
27fl
 for a more detailed explanation of entanglement entropy.)
Ł
Wednesday July 17th
Š There was a talk on fiColombeau theoryfl by a mathemati-
cian whose name I unfortunately failed to catch. Colombeau theory is a theory that
192
 WEEK 87 AUGUST 20, 1996
allows you to multiply distributions, just like they said in school that you weren't
allowed to do. So if for example you want to square the Dirac delta function, you
can do it in the context of Colombeau theory. There has been a certain amount of
debate, however, on whether Colombeau theory allows you to this multiplication
in a
useful
way. There were a lot of physicists at this talk who would be willing
and eager to master Colombeau theory if it let one solve the physics problems
they wanted to solve. However, after much discussion, it appears that they didn't
buy it. I believe that at best Colombeau theory provides a useful framework for
understanding the ambiguities one encounters when multiplying distributions.
I say fiambiguitiesfl rather than fidisastersfl because while the square of the Dirac
delta function has no sensible interpretation as a distribution, there are many cases,
such as when you try to multiply the Dirac delta function and the Heaviside func-
tion, wh ere you can interpret the result as a distribution in a variety of ways. These
ambiguous cases are the ones of greatest interest in physics. A nice place to see
this in quantum eld theory is in
1)
 G. Scharf,
Finite Quantum Electrodynamics: the Causal Approach
, Springer,
Berlin, 1995.
If you want to learn about Colombeau theory you can try:
2)
 J. F. Colombeau,
Multiplication of Distributions: a Tool in Mathematics, Numer-
ical Engineering, and Theoretical Physics
, Lecture Notes in Mathematics
1532
,
Springer, Berlin, 1992.
Later that day I had nice conversation with Jerzy Lewandowski on the approach to
the loop representation where one uses smooth, rather than analytic, loops. (See
fiWeek 55fl
 for more on this issue.)
Ł
Thursday, July 18th
Š Carlo Rovelli spoke on fiBlack Hole Entropyfl, reporting
some work he did with Kirill Krasnov. They have a nice approach to comput-
ing the black hole entropy using the loop representation of quantum gravity. A
common goal among quantum gravity folks is to recover the Bekenstein-Hawking
formula from some full-edged theory of quantum gravity Š the original deriva-
tion being a curious fisemiclassicalfl hybrid of quantum and classical reasoning. In
a statistical mechanical approach, entropy should be the logarithm of the num-
ber of microstates some system can have in a given macrostate. So one wants to
count states somehow. Basically what Rovelli and Krasnov do is count the num-
ber of ways a surface can be pierced by a spin network so as to give it a certain
area. (This uses the formula for the area operator I described in
 fiWeek 86fl
.) They
get an entropy proportional to the area, but not with the same constant as in the
Bekenstein-Hawking formula.
There were some hopes that taking matter elds into account might give the right
constant. But since everyone had been to Ted Jacobson's talk, this led to much
interesting wrangling over whether Rovelli and Krasnov were using the bare or
renormalized Newton's constant
G
, and whether the concept of bare and renor-
malized
G
even m akes sense, ultimately! Also, there are some extremely important
193
 WEEK 87 AUGUST 20, 1996
puzzles about what the right way to count states is, in these loop representation
computations.
For more, try:
3)
 Carlo Rovelli, fiLoop quantum gravity and black hole physicsfl, available as
gr-qc/9608032
.
Kirill Krasnov, fiThe Bekenstein bound and non-perturbative quantum grav-
ityfl, available as
gr-qc/9603025
.
Kirill Krasnov, fiOn statistical mechanics of gravitational systemsfl, available as
gr-qc/9605047
.
Ł
Friday, July 19th
Š Don Marolf spoke on fiBlack hole entropy in string theoryfl. He
attempted valiantly to describe the string-theoretic approach to computing black
hole entropy to an audience only generally familiar with string theory. I will not
try to summarize his talk, except to note that he mainly discussed the case of a
black hole in 5 dimensions, which was really a fiblack stringfl in 6 dimensions Š
a solution with translational symmetry in the 6th dimension, but where the extra
6th dimension is so tiny that ordinary
5
-dimensional folks think they've just got a
black hole. (By the way, even the
6
-dimensional approach is really just a way of
talking about a string theory that fundamentally lives in 10 dimensions. This stuff
is not for the faint-hearted.)
Here are a few papers on this subject by Marolf and Horowitz:
4)
 Gary Horowitz, fiThe origin of black hole entropy in string theoryfl, available
as
gr-qc/9604051
.
Gary Horowitz and Donald Marolf, fiCounting states of black strings with trav-
eling wavesfl, available as
hep-th/9605224
.
Gary Horowitz and Donald Marolf, fiCounting states of black strings with trav-
eling waves IIfl, available as
hep-th/9606113
.
Ł
Monday, July 22nd
Š Kirill Krasnov spoke on fiThe EisteinŒMaxwell Theory of
Black Hole Entropyfl. This was a report on attempts to see how his calculations
of the black entropy in the loop representation changed when he took the elec-
tromagnetic eld into account. The calculations were very tentative, for certain
technical reasons I won't go into here, but they made even clearer the importance
of the issue of how one counts states when computing entropy in this approach.
Later, I had a nice conversation with Carlo Rovelli about my hopes for thinking of
fermions (e.g., electrons) as the ends of wormholes in the loop representation of
quantum gravity. We came up with a nice heuristic argument to get the right Fermi
statistics for these wormhole ends. Hopefully we can make this all more precise at
some later date.
Ł
Tuesday, July 23rd
Š Ted Jacobson gave informal talks on two subjects, the rst
of which was fiTransplanckian puzzle: origin of outgoing black hole modesfl. This
194
 WEEK 87 AUGUST 20, 1996
dealt with the puzzling fact that in the standard computation of Hawking radia-
tion, the rather low-frequency radiation which leaves the hole is the incredibly red-
shifted offspring of high-frequency modes which swung past the horizon shortly af-
ter the hole's formation Š modes whose wavelength is far smaller than the Planck
length!
What if spacetime is figrainyfl in some way at the Planck scale? Jacobson studied
this using an analogy introduced by Unruh. If you have uid owing down a
narrowing pipe, and at some point the velocity of the uid ow exceeds the speed
of sound in the uid, there will be a fisonic horizonfl. In other words, there is
a line where the uid ow exceeds the speed of sound, and no sound can work
its way upstream across that line. Now if you quantize the theory of sound in
a simple-minded way you get fiphononsfl Š which have indeed been observed in
solid-state physics. Unruh showed that in the case at hand you would get fiHawking
radiationfl of phonons from the sonic horizon, going upstream and getting shifted
to lower frequencies as they go.
Jacobson considered what would happen if you actually took into account the
graininess of the uid. (He considered the theory of liquid helium, to be spe-
cic.) The graininess at the molecular scale means that the group velocity of waves
drops at very high frequencies. So what happens instead of fiHawking radiationfl
is something rather different. Start with a high-frequency wave attempting to go
upstream, starting from upstream of the sonic horizon. Its group velocity is very
slow so it fails miserably and gets swept toward the sonic horizon, like a hapless
poor swimmer getting pulled to the edge of a waterfall despite trying to swim up-
stream. But as it gets pulled near the h orizon its wavelength increases, and thus
group velocity increases, thus allowing it to shoot upstream at the last minute!
(An analogous process is apparently familiar in plasma physics under the name of
fimode conversionfl.) In this scenario, the Hawking radiation winds up resulting
from incoming modes through this process of mode conversion Š modes that have
short wavelength, but not as short as the intermolecular spacing (or Planck length,
in the gravitational case.)
Ted Jacobson's second talk was even more interesting to me, but I'll postpone that
for next Week.
Here, by the way, is a paper related to the talk by Pullin discussed in
 fiWeek 86fl
:
5)
 Hugo Fort, Rodolfo Gambini and Jorge Pullin, fiLattice knot theory and quan-
tum gravity in the loop representationfl, available as
gr-qc/9608033
.
195
 WEEK 88 AUGUST 26, 1996
Week 88
August 26, 1996
This issue concludes my report of what happened at the Mathematical Problems of Quan-
tum Gravity workshop in Vienna. I left the workshop at the end of July, so my reportage
ends there, but the workshop went on for a few more weeks after that. I'll be really
bummed out if I nd out that they solved all the problems with quantum gravity after I
left.
Before I launch into my day-by-day account of what happened, let me note that I've
written a little introduction to Thiemann's work on the Hamiltonian constraint, which
he presented at the workshop (see
 fiWeek 85fl
):
1)
 John Baez, fiThe Hamiltonian constraint in the loop representation of quantum
gravityfl, available at
http://math.ucr.edu/home/baez/hamiltonian/
.
A less technical version of this appears in Jorge Pullin's newsletter
Matters of Gravity
,
issue 8, at
http://www.phys.lsu.edu//mog/mog8/node7.html
.
Okay... I'll start out simple today since there is something nice and simple to ponder:
Ł
Tuesday, July 23rd
Š Ted Jacobson spoke on the fiGeometry and Evolution of
Degenerate Metricsfl. One of the interesting things about Ashtekar's reformulation
of general relativity is that it extends general relativity to the case of degenerate
metrics, that is, metrics where there are vectors whose dot product with all other
vectors is zero. However, one needs to be very careful because different versions
of Ashtekar's formulation give
different
ways of handling degenerate metrics.
To see why in a simple example, remember that the usual metric on Minkowski
spacetime is nondegenerate and in nice coordinates looks like

1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 0
1
C
C
A
In other words, where the speed of light is zero only in the
z
direction. Basically
what happens is that spacetime gets foliated with a lot of
3
-dimensional slices, and
on each one you get the equations of
3
-dimensional general relativity.
Ł
Friday, July 26th
Š Thomas Strobl spoke on
2
-dimensional gravity. I don't under-
stand his work well enough yet to have anything much to say, but the most inter-
esting thing about it to
me
is that it allows one to see how quantum groups emerge
from the
G=G
gauged WessŒZuminoŒWitten model (a certain
2
-dimensional topo-
logical quantum eld theory), by describing this theory as the quantization of a
Poisson
˙
-model Š a eld theory where the elds take values in a Poisson mani-
fold. For more, try:
3)
 Peter Schaller and Thomas Strobl, A brief introduction to Poisson
˙
-models,
available as
 hep-th/9507020
.
Peter Schaller and Thomas Strobl, Poisson
˙
-models: a generalization of 2d
gravity-YangŒMills systems, available as
 hep-th/9411163
.
Later, I had a great conversation with Mike Reisenberger and Carlo Rovelli on
reformulating the loop representation of quantum gravity in terms of surfaces em-
bedded in spacetime. This again touched upon my interest in relating string theory
and the loop representation. They are writing a paper on this which should be on
the preprint servers pretty soon, so I'll wait until then to talk about it.
Ł
Saturday, July 27th
Š Carlo Rovelli explained some things about the problem of
time to me.
Ł
Monday, July 30th
Š I spoke about relative states and entanglement entropy in
two-part quantum systems (see
 fiWeek 27fl
) and the applications of these ideas to
topological quantum eld theory and quantum gravity. A lot of this came from my
attempts to understand the relation between quantum gravity and ChernŒSimons
theory, and Lee Smolin's work where he tries to use this relation to derive the
Bekenstein bound on the entropy of a system in terms of its surface area (see
fiWeek 56fl
).
An interesting little fact that I needed to use is that if you have a two-part quan-
tum system in a pure state Š a state of zero entropy Š the two parts, regarded
individually, can themselves have entropy, but the entropies of the two parts are
equal. I worked this out using the symmetry of the situation but Walter Thirring,
199
 WEEK 88 AUGUST 26, 1996
who attended the talk, pointed out that it can also be derived from a wonderful
general fact: the triangle inequality! Namely, if your two-part system has entropy
S
, and the two parts individually have entropies
S
1
and
S
2
, then
S
can never be
less than
j
S
1

k
)
-dimensional. (The 0-dimensional object
x
is now
the 2-dimensional fibackground.fl) For more on string diagrams, see:
10)
 Ross Street, fiCategorical structuresfl, in
Handbook of Algebra
, vol.
1
, ed. M. Hazewinkel,
Elsevier, 1996.
This diagram may also remind physicists (if any of them are still reading this) of a
Feynman diagram, in particular a 3-gluon vertex in QCD. It's no coincidence! I'll have to
say more about that later, though.
To continue reading the fiTale of
n
-Categoriesfl, see
 fiWeek 92fl
.
206
 WEEK 90 SEPTEMBER 30, 1996
Week 90
September 30, 1996
If you've been following This Week's Finds, you know that I'm in love with symmetry.
Lately I've been making up for my misspent youth by trying to learn more about simple
Lie groups. They are, roughly speaking, the basic building blocks of the symmetry groups
of physics.
In trying to learn about them, certain puzzles come up. In July I asked Bertram
Kostant about one that's been bugging me for years: fiWhy does
E
8
exist?fl In a word, his
answer was: fiTriality!fl This was incredibly exciting to me; it completely blew my mind.
But I should start at the beginning. . . .
In my youth, I found the classication of simple Lie groups to be unintuitive and an-
noying. I still do, but over the years I've realized that suffering through this classication
theorem is the necessary entrance fee to a whole world of symmetry. I gave a tour of
this world in
 fiWeek 62fl
 Œ
 fiWeek 65fl
, but here I want to make everything as simple as
possible, so I won't assume you've read that stuff. Experts should jump directly to the
end of this article and read backwards until it becomes boring.
A Lie group is a group that can be given coordinates for which all the group op-
erations are innitely differentiable. A good example is the group
SO(
n
)
of rotations
in
n
-dimensional Euclidean space. You can multiply rotations by doing rst one and
then the other, or mathematically by doing matrix multiplication. Every rotation has an
inverse, given mathematically by the inverse matrix. Since matrices are just bunches
of numbers, you can coordinatize
SO(
n
)
, at least locally, and in terms of these coordi-
nates the operations of multiplication and taking inverses are innitely differentiable, or
fismoothfl, so
SO(
n
)
is a Lie group.
Using the magic of calculus, we can think of tangent vectors at the identity element
of
SO(
n
)
as fiinnitesimal rotationsfl. So for example, taking
n
= 3
, let's start with the
rotation by the angle
t
about the
z
axis, given by the matrix:
0
@
cos
t

J
x
J
z
=
J
y
:
207
 WEEK 90 SEPTEMBER 30, 1996
If you have never done it, there are few things in life as rewarding at this point as
computing
J
x
and
J
y
for yourself and checking the above ficommutation relationsfl.
Folks usually write the ficommutatorsfl on the left hand side using brackets, like this:
[
J
x
; J
y
] =
J
z
;
[
J
y
; J
z
] =
J
x
;
[
J
z
; J
x
] =
J
y
:
These relations are lurking in the denition of quaternions and also the vector cross
product. Quaternions and cross products are good for understanding rotations in
3
-
dimensional space; they let us describe innitesimal rotations and their failure to com-
mute. Here we are calling a spade a spade and working directly with the algebra of
innitesimal rotations, which folks call
so
(3)
. (For related stuff, see
 fiWeek 5fl
.)
Okay. The point is, we can do this trick for any Lie group! The space of fiinnitesimal
group elementsfl, or more precisely tangent vectors at the identity element of a Lie group,
is called the fiLie algebra of the groupfl. It's a vector space whose dimension is the
dimension of the group, and it always has a bracket operation on it satisfying certain
axioms (listed in
 fiWeek 3fl
).
The classication of Lie groups can be reduced to the classication of Lie algebras,
because the Lie algebra almost determines the Lie group. More precisely, every Lie al-
gebra is the Lie algebra of a unique Lie group that is fisimply connectedfl Š i.e., one for
which every loop in it can be continuously shrunk to a point. People understand how to
get from any Lie group to a simply connected one (called its fiuniversal coverfl), so if we
understand simply connected Lie groups, we pretty much understand all Lie groups. See
fiWeek 61fl
 for an instance of this philosophy.
Now classifying Lie algebras is just a matter of heavy-duty linear algebra. Let me
explain what the fisimplefl Lie algebras are; you'll have to take my word for it that under-
standing these is a big step towards understanding all Lie algebras.
At one extreme in the world of Lie groups are the commutative, or fiabelianfl Lie
groups. Here multiplication is commutative, so
[
x; y
] = 0
for all
x
and
y
in the Lie
algebra of the group. At the other extreme are the fisemisimplefl Lie groups. Here every
element in the Lie algebra is of the form
[
x; y
]
for some
x
and
y
: roughly, if we bracket
the whole Lie algebra with itself, we get itself back again. The sem isimple Lie algebras
turn out to be incredibly important in physics, where they are the typical figauge groupsfl
of eld theories.
The fisimplefl Lie algebras are the building blocks of the semisimple ones: every
semisimple Lie algebra can be broken down into pieces that are simple. (Technically,
we say it's a fidirect sumfl of simple Lie algebras). We say a Lie group is simple if its Lie
algebra is simple.
So: what are the simple Lie algebras? They were classied, thanks to some heroic
work by Killing and Cartan, in the early part of the 20th century. To keep life simple
(ahem) I'll only give the classication of those simple Lie algebras whose corresponding
Lie groups are
compact
Š meaning roughly that they are nite in size. (For example,
SO(
n
)
is compact.) It turns out that if we understand the compact ones, we can under-
stand the noncompact ones too.
So, here are the Lie algebras of the compact simple Lie groups! There are 4 straight-
forward innite families and 5 delightful and puzzling exceptions. The 4 innite fami-
208
 WEEK 90 SEPTEMBER 30, 1996
lies are easy to understand and are called ficlassical groupsfl. They are the workhorses of
mathematics and physics. The other 5 are called fiexceptional groupsfl. They have always
seemed very mysterious to me.
The 4 innite families are:
Ł
A
n
: This is the Lie algebra of
SU(
n
)
, the group of
n

n
complex matrices that
preserve lengths (i.e., are unitary) and have determinant
1
. This Lie algebra is also
called
su
(
n
)
.
Ł
B
n
: This is the Lie algebra of
SO(2
n
+ 1)
, the group of
(2
n
+ 1)

(2
n
+ 1)
real
matrices that preserve lengths (i.e., are orthogonal) and have determinant
1
. This
Lie algebra is also called
so
(2
n
+ 1)
.
Ł
C
n
: This is the Lie algebra of
Sp(
n
)
, the group of
n

n
quaternionic matrices that
preserve lengths. This Lie algebra is also called
sp
(
n
)
.
Ł
D
n
: This is the Lie algebra of
SO(2
n
)
, the group of
2
n

2
n
real matrices that
preserve lengths and have determinant
1
. This Lie algebra is also called
so
(2
n
)
.
You may justly wonder why the heck they are called
A
n
,
B
n
,
C
n
, and
D
n
, and why
we separated out the even and odd cases of
SO(
n
)
as we did! This is explained in
 fiWeek
64fl
, and I don't want to worry about it here. Anyway, glossing over some nuances, we
see that these guys are all pretty much just groups of rotations in real, complex, and
quaternionic vector spaces.
The 5 exceptions are as follows:
Ł
F
4
: A 52-dimensional Lie algebra.
Ł
G
2
: A 14-dimensional Lie algebra.
Ł
E
6
: A 78-dimensional Lie algebra.
Ł
E
7
: A 133-dimensional Lie algebra.
Ł
E
8
: A 248-dimensional Lie algebra.
Here I am being rather reticent about what these Lie algebras Š or the corresponding
Lie groups, which go by the same names Š actually
are!
The reason is that it's not so
easy to explain. One can certainly describe the exceptional Lie groups as groups of
matrices with certain complicated properties, but often this is done in a way that leaves
one utterly puzzled as to the real reason why these simple Lie groups exist.
Of course, the answer to fiwhyfl a mathematical object exists is a matter of taste. You
may feel satised if you can easily construct it from other objects you know and love, or
you may feel satised once it is so tightly woven into your overall scheme of things that
you can't imagine life without it.
In any case, I have long been asking people why the exceptional Lie groups exist, but
without much luck. Until recently I only felt happy about one of them, the one called
G
2
: it's the group of rotations of the octonions! The real numbers, complex numbers,
quaternions and octonions are the only finormed division algebrasfl Š a property which
makes it easy to dene rotation groups Š but the octonions are weirder than the other
209
 WEEK 90 SEPTEMBER 30, 1996
three because, unlike the others, they are not associative. (See
 fiWeek 59fl
 and
 fiWeek
61fl
 for details.) One might expect a series of simple Lie groups coming from rotations
in octonionic vector spaces, like the other classical series... but there isn't one! The
only simple Lie group like this is the group of rotations of a
one
-dimensional octonionic
vector space,
G
2
. (More precisely, we say that
G
2
is the group of automorphisms of the
octonions, that is, the linear transformations that preserve the octonion product. These
all preserve lengths.)
The idea that the exceptional groups are all related to octonions is sort of pleasing,
because one might easily
expect
that the reals, complexes and quaternions give nice
innite series of ficlassicalfl Lie groups, while the octonions, being much more bizarre,
give only 5 bizarre fiexceptionalfl Lie groups. Indeed, in
 fiWeek 64fl
 I described how
F
4
and
E
6
are related to the octonions... but in a pretty complicated way! As for
E
7
and
E
8
, here until recently I had always been completely in the dark. This is all the more
irksome because the biggest, most mysterious exceptional Lie group of all,
E
8
, plays an
important role in string theory!
Luckily, on Thursday July 11th I ran into Bertram Kostant, who had been attending
the previous workshop here at the Erwin Schr
¨
odinger Institute. As I described in
 fiWeek
79fl
, Kostant is one of the expert's experts on group theory. So I got up my nerve and
asked him, fiWhy does
E
8
exist?fl And he told me! Best of all, he explained both
E
8
and
F
4
in terms of a principle that I knew was crucial for understanding
G
2
and the
octonions: the principle of triality!
I sketched a description of triality in
 fiWeek 61fl
. Let me just summarize the idea here.
One of the main way to understand Lie algebras is to understand their firepresentationsfl.
A representation of a Lie algebra is simply a function from it to the space of
n

n
matrices
that preserves the bracket operation. (The
n

n
matrices form a Lie algebra with the
commutator as the bracket operation.) For example,
so
(
n
)
has a representation where we
map each element to an
n

n
matrix in the most utterly obvious way: each element
is
an
n

n
matrix, so don't do anything to it! This is called the fivectorfl representation, because
this is how we do innitesimal rotations to vectors. But
so
(
n
)
also has representations
called fispinorfl representations. In physics, the vector representation describes spin-
1
particles, while the spinor representations describe spin-
1
=
2
particles.
Spinor representations work differently depending on whether the dimension
n
is
even or odd. (This is one reason why people distinguish the even and odd
n
cases
of
so
(
n
)
in that classication of simple Lie algebras above!) When
n
is odd there is
one spinor representation. That's why in ordinary
3
-dimensional space there is just one
kind of spinor to worry about, as you learn when you learn about spin-
1
=
2
particles
in undergraduate quantum mechanics. When
n
is even there are two different spinor
representations, called the fileft-handedfl and firight-handedfl spinor representations. This
shows up when you do quantum mechanics taking special relativity Š and
4
-dimensional
spacetime Š into account. For example, the way neutrinos transform under rotations
is described by the left-handed spinor representation, while anti-neutrinos are described
by right-handed spinors.
When
n
is even, both the spinor representations of
so
(
n
)
are of dimension
2
n=
2

1
=
n
, so the spinor represen-
tations are just as big as the vector representation. This might lead one to hope that in
some sense they are fithe samefl as the vector representation. This is actually true, but in
210
 WEEK 90 SEPTEMBER 30, 1996
a subtle way. . . . they are not fiequivalentfl representations in the standard sense of Lie
algebra theory, but something sneakier is true.
The Lie algebra
so
(8)
has interesting symmetries! It has a little symmetry group
with 6 elements, the same as the symmetries of a equilateral triangle, and using these
6 symmetries we can permute the vector, left-handed spinor, and right-handed spinor
representations into each other however we please!
For example, one of these symmetries switches the left-handed and right-handed
spinor representations, but leaves the vector representation alone. Actually, this symme-
try works in any even dimension, not just dimension 8. Its analogue in
4
-dimensional
spacetime is called fiparityfl, a symmetry that turns left-handed particles into right-handed
ones and vice versa. The fact that there are no right-handed neutrinos means that the
laws of nature do not actually have this symmetry... but it's still very important in math
and physics.
What's special about dimension 8 is that there are symmetries switching the vector
representation and the spinor representations. For example: if we take an element
x
of
so
(8)
, apply the right symmetry of
so
(8)
to turn it into another element of
so
(8)
, and
then use the right-handed spinor representation to it to turn it into a matrix, we get the
same thing as if we just used the vector representation to turn
x
into a matrix.
Now
so
(8)
is the Lie algebra of the Lie group
SO(8)
, but
SO(8)
is not fisimply con-
nectedfl in the sense dened above. The simply connected group whose Lie algebra is
SO(
n
)
is called
Spin(
n
)
. I gave an introduction to these fispin groupsfl in
 fiWeek 61fl
, and
I don't want to say much about them here, except for this: the triality symmetries of
so
(8)
do not give symmetries of
SO(8)
, but they do give symmetries of
Spin(8)
. Experts
say the group of outer automorphisms modulo inner automorphisms of
SO(8)
is
S
3
(the
group of permutations of 3 things).
Pretty sneaky, how a group of symmetries can have its own group of symmetries, no?
As we'll now see, this is what gives birth to
G
2
,
F
4
,
E
8
, and the octonions.
To get
G
2
is pretty simple; we look at those elements of
Spin(8)
that are xed (i.e.,
unaffected) by all the triality symmetries, and these form a subgroup, which is
G
2
.
For the rest, we need one more fact: there is a way to fimultiplyfl a left-handed spinor
and a right-handed spinor and get a vector. This is true in all even dimensions, not just
n
= 8
, so in particular it is familiar to particle theorists who live in
4
-dimensional space-
time. As I noted, what happens to a neutrino when you rotate (or Lorentz transform) it is
described using left-handed spinors, while anti-neutrinos are described by right-handed
spinors. Similarly, photons are described by vectors. So as far as
rotational
properties go,
one could think of a photon as a bound state of a neutrino and an antineutrino. This led
Schr
¨
odinger (or someone) to propose at one point that photons were actually neutrino-
antineutrino pairs. Subsequent experiments showed this theory has lots of problems,
and nobody sane believes it any more. Still, it's sort of cute.
Now, in 8 dimensions, it shouldn't be surprising that we can also multiply a left-
handed spinor and a vector to get a right-handed spinor, and so on. The point is, you
can just use triality to permute the three representations whichever way you please...
they are not really all that different.
So in particular, you can multiply two
8
-dimensional vectors and get another vector.
And this gives us the octonions!
Now how about
F
4
and
E
8
? This is the cool stuff Kostant told me about. Here I will
describe the Lie algebras, not the Lie groups.
211
 WEEK 90 SEPTEMBER 30, 1996
Let's call the right-handed and left-handed spinor representations
S
+
and
S

1)
=
2
numbers to describe a rotation in
n
dimensions. Hey! Look! 52
is the dimension of
F
4
! So maybe this thing is
F
4
.
Yes, it is! Here's how it works. To make this gadget into a Lie algebra Š which turns
out to be
F
4
Š we need a way to take the fibracketfl of any two elements in it. We already
know how to take the bracket of two guys in
so
(8)
, so that's no problem. Since
so
(8)
acts
as transformations of
S
+
and
S


V
and get another such guy. If you do
it right Š I've been pretty vague, so I leave it to you to ll in the details Š you can get
this bracket to satisfy the Lie algebra axioms, and you get
F
4
!
Emboldened with our success, we now look at the vector space
so
(8)

so
(8)

End(
S
+
)

End(
S

)
. Putting all this stuff together we get a Lie algebra, if we do it right Š and
it's
E
8
. At least that's what Kostant said; I haven't checked it.
So now we see, at least roughly, how triality gives birth to the octonions,
G
2
,
F
4
,
and
E
8
. That leaves
E
8
's filittle brothersfl
E
6
and
E
7
. These are contained in
E
8
as Lie
subalgebras, but apart from that I don't know any especially beautiful way to get ahold
of them, except for the way to get
E
6
from
3

3
matrices of octonions, which I described
in
 fiWeek 64fl
.
For some references to this stuff, try:
1)
 Claude C. Chevalley,
The Algebraic Theory of Spinors
, Columbia U. Press, New York,
1954.
2)
 F. Reese Harvey,
Spinors and Calibrations
, Perspectives in Mathematics,
9
, Aca-
demic Press, Boston, 1990.
3)
 Ian R. Porteous,
Topological Geometry
, Cambridge U. Press, Cambridge, 1981.
4)
 Ian R. Porteous,
Clifford Algebras and the Classical Groups
, Cambridge U. Press,
Cambridge, 1995.
5)
 Hans Freudenthal and H. de Vries,
Linear Lie Groups
, Academic Press, New York,
1969.
6)
 Alex J. Feingold, Igor B. Frenkel, and John F. X. Rees,
Spinor Construction of Vertex
Operator Algebras, Triality, and
E
(1)
8
, Contemp. Math.
121
, AMS, Providence, 1991.
I haven't looked at all these books lately, and the only source I
know
contains the above
construction of
E
8
from triality is the last one, by Feingold, Frenkel, and Rees.
Now let me allow myself to get a bit more technical.
I am still not entirely happy, by any means, because what I'd really like would be
a simple explanation of why these exceptional simple Lie algebras arise from triality,
and no others
. In other words, I'd like a classication of the simple Lie algebras that
proceeded not by the usual exhaustive (and exhausting) case-by-case study of Dynkin
diagrams, but by some less combinatorial and more fisyntheticfl approach. For example,
it would be nice to really see a good explanation of how the reals, the complexes, the
quaternions and octonions each give rise to a family of simple Lie algebras, and one gets
all
of them this way.
On the other hand, don't think I'm knocking the Dynkin diagram stuff. As I explained
in
 fiWeek 62fl
 Œ
 fiWeek 64fl
, what's really fundamental to the Dynkin diagram approach
seems to be the not the Lie algebras themselves but their root lattices. Taking lattices as
fundamental to the study of symmetry
does
seem to be a good idea, since it gets you to
not just the simple Lie algebras described above, but also the fiKacŒMoody algebrasfl so
important in string theory and other forms of
2
-dimensional physics, as well as marvelous
things like the Leech lattice and the Monster group.
The Dynkin diagram approach also makes it clear
why
triality exists: symmetries of
Dynkin diagrams always give outer automorphisms of the corresponding Lie algebras,
213
 WEEK 90 SEPTEMBER 30, 1996
and as you examine the Dynkin diagrams of
D
n
, you get
D
2
=
so
(4)
=


D
3
=
so
(6)
=



D
4
=
so
(8)
=




D
6
=
so
(10)
=





and you can just
see
how when you get to
so
(8)
there is that amazing triality symmetry,
ashing briey into being before reverting to the boring old duality symmetry which only
interchanges the left-handed and right-handed spinor representations, corresponding to
the two dots on the far right of the Dynkin diagram. (The dot on the far left corresponds
to the vector representation.)
Of course, people don't usually talk about
D
2
or
D
3
, because
D
2
is two copies of
A
1
,
and
D
3
is the same as
A
3
. However, there is no shame in doing so, and indeed a lot of
insight to be gained: the fact that
D
2
consists of two copies of
A
1
corresponds to the
isomorphism
so
(4) =
su
(2)

su
(2)
;
while the fact that
D
3
is the same as
A
3
corresponds to the isomorphism
so
(6) =
su
(4)
:
Each of these could easily serve as the springboard for a very long and interesting
discussion. However, I will refrain. Here let me simply note that you can always fifoldfl a
Dynkin diagram using one of its symmetries, and if you do this to
D
4
using triality you
214
 WEEK 90 SEPTEMBER 30, 1996
go from
D
4
=




down to
G
2
=

>
6

(Here the number 6 means that the two roots are at an angle of
ˇ =
6
from each other.
People usually just draw a triple line to indicate this. The arrow points from the long root
to the shorter root.) This corresponds to how
G
2
is the subgroup of
Spin(8)
consisting of
elements that are invariant under triality. You can also go from
E
6
=






down to
F
4
=


>
4


by folding along the reection symmetry. And Friedrich Knop told me a neat way to get
triality symmetry
from
F
4
, if you happen to have
F
4
around: the long roots of
F
4
form
a root system of type
D
4
, which denes an embedding of
Spin(8)
into the Lie group
F
4
(more precisely, the compact real form). On the other hand, the two short simple roots
dene an embedding of
SU(3)
in
F
4
. The Weyl group of
SU(3)
is
S
3
and can be lifted
to
SU(3)
, so we have an
S
3
subgroup of
F
4
. This acts by conjugation on the
Spin(8)
subgroup, implementing the triality symmetries!
But I digress. My main point is, the Dynkin diagram symmetries do give a nice
way to understand outer automorphisms of simple Lie groups, and these provide some
important ties between simple Lie algebras, including triality, which links the ficlassicalfl
world to the fiexceptionalfl world. But it is also nice to try to understand these in a
somewhat more ficonceptualfl way. This is one of the reasons I'm interested in 2-Hilbert
spaces: they seem to help one understand this stuff from a new angle. But more on
those, later. They tie into the
n
-category stuff I'm always talking about. I will return to
that tale soon, and I'll keep building up some of the tools we need, until we are ready to
launch into a description of 2-Hilbert spaces.
In writing this Week's Finds, I benetted greatly from email correspondence with
Robt Bryant, Christopher Henrich, Geoffrey Mess, Friedrich Knop, and others.
215
 WEEK 91 OCTOBER 6, 1996
Week 91
October 6, 1996
For a while now I've been meaning to nish talking about monads and adjunctions, and
explain what that has to do with the 4-color theorem. But rst I want to say a little bit
more about fitrialityfl, which was the subject of
 fiWeek 90fl
.
Triality is a cool symmetry of the innitesimal rotations in 8-dimensional space. It
was only last night, however, that I gured out what triality has to do with 3 dimensions.
Since it's all about the number
three
obviously triality should originate in the symmetries
of
three
-dimensional space, right? Well, maybe it's not so obvious, but it does. Here's
how.
Take good old three-dimensional Euclidean space with its usual basis of unit vectors
i
,
j
, and
k
. Look at the group of all permutations of
f
i; j ; k
g
. This is a little 6-element
group which people usually call
S
3
, the fisymmetric group on 3 lettersfl.
Every permutation of
f
i; j ; k
g
denes a linear transformation of three-dimensional
Euclidean space in an obvious way. For example the permutation
p
with
p
(
i
) =
j ; p
(
j
) =
k ; p
(
k
) =
i
determines a linear transformation, which we'll also call
p
, with
p
(
ai
+
bj
+
ck
) =
aj
+
bk
+
ci:
In general, the linear transformations we get this way either preserve the cross product,
or switch its sign. If
p
is an even permutation we'll get
p
(
v
)

p
(
w
) =
p
(
v

w
)
while if
p
is odd we'll get
p
(
v
)

p
(
w
) =

j :
Now, any permutation
p
of
f
i; j ; k
g
also determines a linear transformation of the quater-
nions, which we'll also call
p
. For example, the permutation
p
I gave above has
p
(
a
+
bi
+
cj
+
dk
) =
a
+
bj
+
ck
+
di:
216
 WEEK 91 OCTOBER 6, 1996
The quaternion product is related to the vector cross product, and so one can check that
for any quaternions
q
and
q
0
we get
p
(
q q
0
) =
p
(
q
)
p
(
q
0
)
if
p
is even, and
p
(
q
0
q
) =
p
(
q
0
)
p
(
q
)
if
p
is odd. So we are getting triality to act as some sort of symmetries of the quaternions.
Now sitting inside the quaternions there is a nice lattice called the fiHurwitz integral
quaternionsfl. It consists of the quaternions
a
+
bi
+
cj
+
dk
for which either
a
,
b
,
c
,
d
are all integers, or all half-integers. Here I'm using physics jargon, and referring to any
number that's an integer plus
1
=
2
as a fihalf-integerfl. A half-integer is
not
any number
that's half an integer!
You can think of this lattice as the
4
-dimensional version of all the black squares on a
checkerboard. One neat thing is that if you multiply any two guys in this lattice you get
another guy in this lattice, so we have a fisubringfl of the quaternions. Another neat thing
is that if you apply any permutation of
f
i; j ; k
g
to a guy in this lattice, you get another
guy in this lattice Š this is easy to see. So we are getting triality to act as some sort of
symmetries of this lattice. And
that
is what people
usually
call triality.
Let me explain, but now let me use a lot of jargon. (Having shown it's all very simple,
I now want to relate it to the complicated stuff people usually talk about. Skip this if
you don't like jargon.) We saw how to get
S
3
to act as automorphisms and antiautomor-
phisms of
R
3
with its usual vector cross product... or alternatively, as automorphisms
and antiautomorphisms of the Lie algebra
so
(3)
. From that we got an action as automor-
phisms and antiautomorphisms of the quaternions and the Hurwitz integral quaternions.
But the Hurwitz integral quaternions are just a differently coordinatized version of the
4
-dimensional lattice
D
4
! So we have gotten triality to act as symmetries of the
D
4
lat-
tice, and hence as automorphisms of the Lie algebra
D
4
, or in other words
so
(8)
, the Lie
algebra of innitesimal rotations in 8 dimensions. (For more on the
D
4
lattice see
 fiWeek
65fl
, where I describe it using different, more traditional coordinates.)
Actually I didn't invent all this stuff, I sort of dug it out of the literature, in particular:
1)
 John H. Conway and Neil J. A. Sloane,
Sphere Packings, Lattices and Groups
, Grundlehren
der mathematischen Wissenschaften
290
, Springer, Berlin, 1993.
and
2)
 Frank D. (Tony) Smith, fiSets and
C
n
; quivers and ADE; triality; generalized super-
symmetry; and
D
4
-
D
5
-
E
6
fl, available as
hep-th/9306011
.
But I've never quite seen anyone come right out and admit that triality arises from the
permutations of the unit vectors
i
,
j
, and
k
in 3d Euclidean space.
I should add that Tony Smith has a bunch of far-out stuff about quaternions, octo-
nions, Clifford algebras, triality, the
D
4
lattice Š you name it! Š on his home page:
3)
 Tony Smith's home page,
http://valdostamuseum.org/hamsmith/
217
 WEEK 91 OCTOBER 6, 1996
He engages in more free association than is normally deemed proper in scientic
literature Š you may raise your eyebrows at sentences like fithe Tarot shows the Lie
algebra structure of the
D
4
-
D
5
-
E
6
