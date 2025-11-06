D
;
E
;
F
;
and
G
. These
were real Lie algebras; we can also switch viewpoint and work with complex Lie algebras
if we like, in which case we simply say we're studying the complex simple Lie algebras,
as opposed to their ficompact real formsfl.
Unfortunately, I didn't say much about what these Lie algebras actually are! Basically,
they go like this:
76
 WEEK 64 SEPTEMBER 23, 1995
A
n
Š The Lie algebra
A
n
is just
sl
n
+1
(
C
)
, the
(
n
+ 1)

(
n
+ 1)
complex matrices with
vanishing trace, which form a Lie algebra with the usual bracket
[
x; y
] =
xy

y x
. The
compact real form of
sl
n
(
C
)
is
su
n
, and the corresponding compact Lie group is
SU(
n
)
,
the
n

n
unitary matrices with determinant
1
. The symmetry group of the electroweak
force is
U(1)

SU(2)
, where
U(1)
is the
1

1
unitary matrices. The symmetry group of
the strong force is
SU(3)
. The study of
A
n
is thus a big deal in particle physics. People
have also considered figrand unied theoriesfl with symmetry groups like
SU(5)
.
B
n
Š The Lie algebra
B
n
is
so
2
n
+1
(
C
)
, the
(2
n
+ 1)

(2
n
+ 1)
skew-symmetric
complex matrices with vanishing trace. The compact real form of
so
n
(
C
)
is
so
n
, and
the corresponding compact Lie group is
SO(
n
)
, the
n

n
real orthogonal matrices with
determinant
1
, that is, the rotation group in Euclidean
n
-space. For some basic cool facts
about
SO(
n
)
, check out
 fiWeek 61fl
.
C
n
Š The Lie algebra
C
n
is
sp
n
(
C
)
, the
2
n

2
n
complex matrices of the form

A B
C D

where
B
and
C
are symmetric, and
D
is minus the transpose of
A
. The compact real
form of
sp
n
(
C
)
is
sp
n
, and the corresponding compact Lie group is called
Sp(
n
)
. This is
the group of
n

n
quaternionic matrices which preserve the usual inner product on the
space
H
n
of
n
-tuples of quaternions.
D
n
Š The Lie algebra
D
n
is
so
2
n
(
C
)
, the
2
n

2
n
skew-symmetric complex matrices
with vanishing trace. See
B
n
above for more about this. It may seem weird that
SO(
n
)
acts so differently depending on whether
n
is even or odd, but it's true: for example,
there are fileft-handedfl and firight-handedfl spinors in even dimensions, but not in odd
dimensions. Some clues as to why are given in
 fiWeek 61fl
.
Those are the ficlassicalfl Lie algebras, and they are things that are pretty easy to
reinvent for yourself, and to get interested in for all sorts of reasons. As you can see,
they are all about firotationsfl in real, complex, and quaternionic vector spaces.
The remaining ones are called fiexceptionalfl, and they are much more mysterious.
They were only discovered when people gured out the classication of simple Lie alge-
bras. As it turns out, they tend to be related to the octonions! Some other week I will
say more about them, but for now, let me just say:
F
4
Š This is a 52-dimensional Lie algebra. Its smallest representation is
26
-dimensional,
consisting of the traceless
3

3
hermitian matrices over the octonions, on which it pre-
serves a trilinear form.
G
2
Š This is a
14
-dimensional Lie algebra, and the compact Lie group corresponding
to its compact real form is also often called
G
2
. This group is just the group of symmetries
(automorphisms) of the octonions! In fact, the smallest representation of this Lie algebra
is 7-dimensional, corresponding to the purely imaginary octonions.
E
6
Š This is a 78-dimensional Lie algebra. Its smallest representation is
27
-dimensional,
consisting of all the
3

3
hermitian matrices over the octonions this time, on which it
preserves the anticommutator.
E
7
Š This is a 133-dimensional Lie algebra. Its smallest representation is 56-dimensional,
on which it preserves a tetralinear form.
E
8
Š This is a 248-dimensional Lie algebra, the biggest of the exceptional Lie alge-
bras. Its smallest representation is 248-dimensional, the so-called fiadjointfl representa-
tion, in which it acts on itself. Thus in some vague sense, the simplest way to understand
77
 WEEK 64 SEPTEMBER 23, 1995
the Lie group corresponding to
E
8
is as the symmetries of itself! (Thanks go to Dick Gross
for this charming information; I think he said all the other exceptional Lie algebras have
representations smaller than themselves, but I forget the sizes.) In
 fiWeek 20fl
 I described
a way to get its root lattice (the
8
-dimensional lattice spanned by the roots) by playing
around with the icosahedron and the quaternions.
People have studied simple Lie algebras a lot this century, basically studied the hell
out of them, and in fact some people were getting a teeny bit sick of it recently, when
along came some new physics that put a lot of new life into the subject. A lot of this
new physics is related to string theory and quantum gravity. Some of this physics is ficon-
formal eld theoryfl, the study of quantum elds in 2-dimensional spacetime that are
invariant under all conformal (angle-preserving) transformations. This is important in
string theory because the string worldsheet is
2
-dimensional. Some other hunks of this
physics go by the name of fitopological quantum eld theoryfl, which is the study of quan-
tum elds, usually in 3 dimensions so far, that are invariant under
all
transformations
(or more precisely, all diffeomorphisms).
Every simple Lie algebra gives rise to an fiafne Lie algebrafl and a fiquantum groupfl.
The symmetries of conformal eld theories are closely related to afne Lie algebras, and
the symmetries of topological quantum eld theories are quantum groups. I won't tell
you what afne Lie algebras and quantum groups ARE, since it would take quite a while.
Instead I'll refer you to a good good introduction to this stuff:
1)
 J
¨
urgen Fuchs,
Afne Lie Algebras and Quantum Groups
, Cambridge U. Press, Cam-
bridge 1992.
Let me whiz through his table of contents and very roughly sketch what it's all about.
1.
Semisimple Lie algebras
This is a nice summary of the theory of semisimple Lie algebras (remember, those
are just direct sums of simple Lie algebras) and their representations. Especially if
you are a physicist, a slick summary like this might be a better way to start learning
the subject than a big fat textbook on the subject. He covers the Dynkin diagram
stuff and much, much more.
2.
Afne Lie algebras
This starts by describing KacŒMoody algebras, which are certain
innite-dimensional
analogs of the simple Lie algebras. Fuchs concentrates on a special class of these,
the afne Lie algebras, and describes the classication of these using Dynkin dia-
grams. The main nice thing about the afne Lie algebras is that their corresponding
innite-dimensional Lie groups are very nice: they are almost filoop groupsfl. If we
have a Lie group
G
, the loop group
LG
is just the set of all smooth functions from
the circle to
G
, which we make into a group by pointwise multiplication. If you're
a physicist, this is obviously relevant to string theory, because at each time, a string
is just a circle (or bunch of circles), and if you are doing gauge theory on the string,
with symmetry group
G
, the gauge group is then just the loop group
LG
. So you'd
expect the representation theory of loop groups and their Lie algebras to be really
important.
You'd
almost
be right, but there is a slight catch. In quantum theory, what counts
are the fiprojectivefl representations of a group, that is, representations that satisfy
78
 WEEK 64 SEPTEMBER 23, 1995
the rule
g
(
h
(
v
)) = (
g h
)(
v
)
up to a phase
. (This is because fiphases are unobservable
in quantum theoryfl Š one of those mottos that needs to be carefully interpreted
to be correct.) The projective representations of the loop group
LG
correspond to
the honest-to-goodness representations of a ficentral extensionfl of
LG
, a slightly
fancier group than
LG
itself. And the Lie algebra of
this
group is called an afne
Lie algebra.
So, people who like gauge theory and string theory need to know a lot about afne
Lie algebras and their representations, and that's what this chapter covers. A real
heavy-duty string theorist will need to know more about KacŒMoody algebras, so
if you're planning on becoming one of those, you'd better also try:
2)
 Victor Kac,
Innite Dimensional Lie Algebras
, Cambridge U. Press, Cambridge,
1990.
You'll also need to know more about loop groups, so try:
3)
 Andrew Pressley and Graeme Segal,
Loop Groups
, Oxford U. Press, Oxford,
1986.
3.
WZW theories
Well, I just said that physicists liked afne Lie algebras because they were the
symmetries of conformal eld theories that were also gauge theories. Guess what:
a WessŒZuminoŒWitten, or WZW, theory, is a conformal eld theory that's also a
gauge theory! You can think of it as the natural generalization of the wave equation
in 2 dimensions (which is conformally invariant, btw) from the case of real-valued
elds to general
G
-valued elds, where
G
is our favorite Lie group.
4.
Quantum groups
When you quantize a WZW theory whose symmetry group
G
is some simple Lie
group, something funny happens. In a sense, the group itself also gets quantized!
In other words, the algebraic structure of the group, or its Lie algebra, gets fide-
formedfl in a way that depends on the parameter
~
(Planck's constant). I have
muttered much about quantum groups on This Week's Finds, especially concern-
ing their relevance to topological quantum eld theory, and I will not try to explain
them any better here! Eventually I will discuss a bunch of books that have come
out on quantum groups, and I hope to give a mini-introduction to the subject in
the process.
5.
Duality, fusion rules, and modular invariance
The previous chapter described quantum groups as abstract algebraic structures,
showing how you can get one from any simple Lie algebra. Here Fuchs really shows
how you get them from quantizing a WZW theory. WZW theories are invariant un-
der conformal transformations, and quantum groups inherit lots of cool properties
from this fact. For example, suppose you form a torus by taking the complex plane
and identifying two points if they differ by any number of the form
nz
1
+
mz
2
,
79
 WEEK 64 SEPTEMBER 23, 1995
where
z
1
and
z
2
are xed complex numbers and
n
,
m
are arbitrary integers. For
example, we might identify all these points:
Re(
z
)
Im(
z
)
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
The resulting torus is a fiRiemann surfacefl and it has lots of transformations, called
fimodular transformationsfl. The group of modular transformations is the discrete
group
SL(2
;
Z
)
of
2

2
integer matrices with determinant
1
; I leave it as an easy
exercise to guess how these give transformations of the torus. (This is an example
of a fimapping class groupfl as discussed in
 fiWeek 28fl
.) In any event, the way the
the WZW theory transforms under modular transformations translates into some
cool properties of the corresponding quantum group, which Fuchs discusses. That's
roughly what fimodular invariancefl means.
Similarly, fifusion rulesfl have to do with the thrice-punctured sphere, or fitrinionfl,
which is another Riemann surface. And fidualityfl has to do with the sphere with
four punctures, which can be viewed as built up from trinions in either of two
fidualfl ways:
80
 WEEK 64 SEPTEMBER 23, 1995
or
This is one of the reasons string theory was rst discovered Š we can think of the
above pictures as two Feynman diagrams for interacting strings, and the fact that
they are really just distorted versions of each other gives rise to identities among
Feynman diagrams. Similarly, this fact gives rise to identities satised by the fusion
rules of quantum groups.
So Š Fuchs' book should make clear how, starting from the austere beauty of the Dynkin
diagrams, we get not only simple Lie groups, but also a wealth of more complicated
structures that people nd important in modern theoretical physics.
Mathematics, rightly viewed, possesses not only truth, but supreme beauty
Š a beauty cold and austere, like that of sculpture, without appeal to any
part of our weaker nature, without the gorgeous trappings of painting or
music, yet sublimely pure, and capable of a stern perfection such as only the
greatest art can show.
Š Bertrand Russell.
81
 WEEK 65 OCTOBER 3, 1995
Week 65
October 3, 1995
This time I'll nish up talking about fiADE classicationsfl for a while, although there is
certainly more to say. Recall where we were: the following diagrams correspond to the
simple Lie algebras, and they also dene certain lattices, the firoot latticesfl of those Lie
algebras:
A
n
, which has
n
dots like this:




B
n
, which has
n
dots, where
n >
1
:



>
4

C
n
, which has
n
dots, where
n >
2
:



<
4

D
n
, which has
n
dots, where
n >
3
:






E
6
,
E
7
, and
E
8
:
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





F
4
:


>
4


82
 WEEK 65 OCTOBER 3, 1995
G
2
:

>
6

The dots in one of these fiDynkin diagramsfl correspond to certain set of basis vectors,
or firootsfl, of the lattice. The lines, with their decorative numbers and arrows, give
enough information to recover the lattice from the diagram. In particular, two dots that
are not connected by a line correspond to roots that are at a 90 degree angle from each
other, while two dots connected by an unnumbered line correspond to roots that are at
a 60 degree angle from each other. Numbered lines mean the angle between roots is
something else, and the arrows point from the longer to the shorter root in this case, as
partially explained in
 fiWeek 63fl
.
However, we will now concentrate on the cases
A
;
D
;
and
E
, where all the roots are
90 or 60 degrees from each other, and they are all the same length Š usually taken to
be length 2. These are the fisimply lacedfl Dynkin diagrams. I want to explain what's so
special about them! But rst, I should describe the corresponding lattices more explicitly,
to make it clear how simple they really are.
The following information, and more, can be found in Chapter 4 of:
1)
 J. H. Conway and N. J. A. Sloane,
Sphere Packings, Lattices and Groups
, Springer,
Berlin, 1993.
which I described in more detail in
 fiWeek 20fl
.
So, what are
A
;
D
;
and
E
like?
A
. We can describe the lattice
A
n
as the set of all
(
n
+1)
-tuples of integers
(
x
1
; : : : ; x
n
+1
)
such that
x
1
+
  
+
x
n
+1
= 0
:
It's a fun exercise to show that
A
2
is a
2
-dimensional hexagonal lattice, the sort of lattice
you use to pack pennies as densely as possible. Similarly,
A
3
gives a standard way of
packing grapefruit, which is in fact the densest lattice packing of spheres in 3 dimen-
sions. (Hsiang has claimed to have shown it's the densest packing, lattice or not, but this
remains controversial.)
D
. We can describe
D
n
as the set of all
n
-tuples of integers
(
x
1
; : : : ; x
n
)
such that
x
1
+
  
+
x
n
is even
:
Or, if you like, you can imagine taking an
n
-dimensional checkerboard, coloring the
cubes alternately red and black, and taking the center of each red cube. In four di-
mensions,
D
4
gives a denser packing of spheres than
A
4
; in fact, it gives the densest
lattice packing possible. Moreover,
D
5
gives the densest lattice packing of in dimension
5. However, in dimensions 6, 7, and 8, the
E
n
lattices are the best!
E
. We can describe
E
8
as the set of 8-tuples
(
x
1
; : : : ; x
8
)
such that the
x
i
are either all
integers or all half-integers Š a half-integer being an integer plus
1
=
2
Š and
x
1
+
  
+
x
8
is even
:
Each point has 240 closest neighbors. Alternatively, as described in
 fiWeek 20fl
, we can
describe
E
8
in a slick way in terms of the quaternions. Another neat way to think of
E
8
83
 WEEK 65 OCTOBER 3, 1995
is in terms of the octonions! Not too surprising, perhaps, since the octonions and
E
8
are
both
8
-dimensional, but it's still sorta neat. For the details, check out
2)
 Geoffrey Dixon, fiOctonion X-product and
E
8
latticesfl, available as
hep-th/9411063
.
Briey, this goes as follows. In
 fiWeek 59fl
 we described a multiplication table for
the fiseven dwarvesfl Š a basis of the imaginary octonions Š but there are lots of other
multiplication tables that would also give an algebra isomorphic to the octonions. Given
any unit octonion
a
, we can dene an fioctonion

-productfl as follows:
b

c
= (
ba
)(
a

c
)
where
a

is the conjugate of
a
(as dened in
 fiWeek 59fl
) and the product on the right-
hand side is the usual octonion product, parenthesized because it ain't associative. For
exactly 480 choices of the unit octonion
a
, the

-product gives us a new multiplication
table for the seven dwarves, such that we get an algebra isomorphic to the octonions
again! 240 of these choices have all rational coordinates (in terms of the seven dwarves),
and these are precisely the 240 closest neighbors of the origin in a copy of the
E
8
lattice!
The other 240 have all irrational coordinates, and these are the closest neighbors to the
origin of a
different
copy of the
E
8
lattice. (Here we've rescaled the
E
8
lattice so the
nearest neighbors have distance
1
from the origin, instead of
p
2
as above.)
Once we have
E
8
in hand, we can get its little pals
E
7
and
E
6
as follows. To get
E
7
, just take all the vectors in
E
8
that are perpendicular to some closest neighbor of the
origin. To get
E
6
, nd a copy of the lattice
A
2
in
E
8
(there are lots) and then take all the
vectors in
E
8
perpendicular to everything in that copy of
A
2
.
So, now that we have a nodding acquaintance with
A
;
D
;
and
E
, let me describe some
of the many places they show up. First, what's so great about these lattices, apart from
the fact that they're the root lattices of simple Lie algebras, with a special fisimply-lacedfl
property? I don't think I really understand the answer to this in a deep way, but I know
various things to say!
First, Witt's theorem says that the
A
;
D
;
and
E
lattices and their direct sums are the
only integral lattices having a basis consisting of vectors
v
with
k
v
k
2
= 2
. Here a lattice
is fiintegralfl if the dot product of any two vectors in it is an integer. In fact, any integral
lattice having a basis consisting of vectors with
k
v
k
2
equal to
1
or
2
is a direct sum of
copies of
A
;
D
;
and
E
lattices and the integers, thought of as a
1
-dimensional lattice.
This makes ADE classications pop up in various places in math and physics. For ex-
ample, there is a cool relationship between the ADE diagrams and the symmetry groups
of the Platonic solids, called the McKay correspondence. Briey, this is what you do to
get it. First, learn about
SO(3)
and
SU(2)
from
 fiWeek 61fl
 or somewhere. Then, take the
symmetry group of a Platonic solid, or more generally any nite subgroup
G
of
SO(3)
.
Since
SO(3)
has
SU(2)
as a double cover, you can get a double cover of
G
, say
e
G
, sitting
inside
SU(2)
. For example, if
G
was the symmetry group of the icosahedron,
e
G
would
be the icosians (see
 fiWeek 24fl
).
Since
e
G
is nite, it has nitely many irreducible representations. Draw a dot for
each of the irreducible representations. One of these will be
2
-dimensional, coming from
the spin-
1
=
2
representation of
SU(2)
. Now, when you tensor this 2d rep with any other
irreducible rep
R
, you get a direct sum of irreducible reps; draw one line from the dot
for
R
to each other dot for each time that other irreducible rep appears in this direct
84
 WEEK 65 OCTOBER 3, 1995
sum. What do you get? Well, you get an fiafne Dynkin diagramfl of type
A
;
D
;
or
E
,
which is like the usual Dynkin diagram but with an extra dot thrown in (corresponding
to the trivial rep of
e
G
). And, you get all of them this way!
In fact, playing around with this stuff some more, you can get the afne Dynkin
diagrams of the other simple Lie algebras. There is a lot more to this... you should
probably look at:
3)
 John McKay, fiGraphs, singularities and nite groupsfl, in
Proc. Symp. Pure Math.
vol
37
, AMS, Providence, Rhode Island, 1980, pp. 183Œ186.
D. Ford and John McKay, fiRepresentations and Coxeter graphsfl, in
The Geometric
Vein
Coxeter Festschrift (1982), Springer, Berlin, pp. 549Œ554.
John McKay, fiA rapid introduction to ADE theoryfl, available at
http://math.ucr.
edu/home/baez/ADE.html
.
4)
 Pavel Etinghof and Mikhail Khovanov, fiRepresentations of tensor categories and
Dynkin diagramsfl, available as
hep-th/9408078
.
McKay does lots of other mindblowing group theory. He's clearly in tune with the
symmetries of the universe... and occasionally he deigns to post to the net! A beautiful
way of thinking about the McKay correspondence in terms of category theory appears in
the paper by Etinghof and Khovanov; what we are really doing, it turns out, is classifying
the representations of the tensor category of unitary representations of
SU(2)
. This ten-
sor category is generated by one object, the spin-
1
=
2
representation, meaning that every
other representation sits inside some tensor power of that one. This way of thinking of
it is important in
5)
 J
¨
urg Fr
¨
ohlich and Thomas Kerler,
Quantum Groups, Quantum Categories, and Quan-
tum Field Theory
, Lecture Notes in Mathematics
1542
, Springer, Berlin, 1991.
Here Fr
¨
ohlich and Kerler give a classication of certain fiquantum categoriesfl that show
up in conformal eld theory and topological quantum eld theory. These are certain
braided tensor categories with properties like those of the categories of representations
of quantum groups at roots of unity. In such categories, every object has a fiquantum
dimensionfl, which need not be integral, and Fr
¨
ohlich and Kerler concentrate on those
categories which are generated by a single object of quantum dimension less than
2
,
getting an ADE-type classication of them. The category of representations of
SU(2)
, on
the other hand, is generated by a single object of dimension equal to
2
Š the spin-
1
=
2
representation Š so Fr
¨
ohlich and Kerler are basically generalizing the McKay stuff to
certain quantum groups related to
SU(2)
.
Where else do ADE diagrams show up? Well, here I won't try to say anything about
their role in the representation theory of fiquiversfl, or in singularity theory; these are
covered pretty well in here:
6)
 M. Hazewinkel, W. Hesselink, D. Siermsa, and F. D. Veldkamp, fiThe ubiquity of
CoxeterŒDynkin diagrams (an introduction to the ADE problem)fl,
Niew. Arch.
Wisk.
,
25
(1977), 257Œ307. Also available at
https://ir.cwi.nl/pub/10039/
10039D.pdf
.
85
 WEEK 65 OCTOBER 3, 1995
Instead, I'll mention something more recent. In string theory, there is a Lie algebra
called the Virasoro algebra that plays a crucial role; its almost just the Lie algebra of the
group of diffeomorphisms of the circle, but it's actually just one dimension bigger, being
a ficentral extensionfl thereof; projective representations of the Lie algebra of the group
of diffeomorphisms of the circle correspond to honest representations of the Virasoro
algebra. An important task in string theory was to classify the unitary representations of
the Virasoro algebra having a given ficentral chargefl
c
(this describes the action of that
one extra dimension) and ficonformal weightfl
h
(this describes the action of dilations).
It turns out that to get unitary reps one needs
c
and
h
to be nonnegative. The represen-
tations with
c
between
0
and
1
are especially nice, for reasons I don't really understand,
and they are called fiminimal modelsfl. An ADE classication of these was conjectured by
Capelli and Zuber, and proved by
7)
 Capelli and Zuber,
Commun. Math. Phys.
113
(1987) 1.
8)
 Kato,
Mod. Phys. Lett. A
2
(1987) 585.
Friedan, Qiu, and Shenker also played a big role in this, in part by guring out the
allowed values of
c
. For a good introduction to this stuff and what it has to do with
honest
physics
(which I admit I've been slacking off on here), try:
9)
 Claude Itzykson and Jean-Michel Drouffe,
Statistical Field Theory, 1: From Brown-
ian Motion to Renormalization and Lattice Gauge Theory
, and
2: Strong Coupling,
Monte Carlo Methods, Conformal Field Theory and Random Systems.
Cambridge U.
Press, 1989.
I will probably come back to this ADE stuff as time goes by, since I'm sort of fascinated
by it, and hopefully folks can refer back to the last few weeks when I do, so they'll re-
member what I'm talking about. But in the next few Weeks I want to catch up with some
new developments in math and physics that have happened in the last few months....
A mathematician, like a painter or poet, is a maker of patterns. If his patterns
are more permanent than theirs, it is because they are made with ideas.
Š
G. H. Hardy
86
 WEEK 66 OCTOBER 10, 1995
Week 66
October 10, 1995
Well, I want to get back to talking about some honest physics, but I think this week I
won't get around to it, since I can't resist mentioning two tidbits of a more mathematical
sort. The rst one is about
ˇ
, and the second one is about the Monster. The second one
does
have a lot to do with string theory, if only indirectly.
First, thanks to my friend Steven Finch, I just found out that Simon Plouffe, Peter
Borwein and David Bailey have computed the ten billionth digit in the hexadecimal (i.e.,
base 16) expansion of
ˇ
. They use a wonderful formula which lets one compute a given
digit of
ˇ
in base 16 without needing to compute all the preceding digits! Namely,
ˇ
=
1
X
n
=0

4
8
n
+ 1

1
in
H
for all
g
in
G
.
This condition means that you cannot form the fiquotient groupfl
G=H
, which one can
think of as a fimore simpliedfl version of
G
.
The classication of the nite simple groups is one of remarkable achievements of
20th-century mathematics. The entire proof of the classication theorem is estimated to
take 10,000 pages, done by many mathematicians. To start learning about it, try:
4)
 Ron Solomon, fiOn nite simple groups and their classicationfl,
Notices Amer.
Math. Soc.
45
, February 1995, 231Œ239.
and the references therein. Again, there are some innite families and 26 exceptions
called the fisporadicfl groups. The biggest of these is the Monster, with
246

320

59

76

112

133

17

19

23

29

31

41

47

59

71
= 808017424794512875886459904961710757005754368000000000
elements. It is a kind of Mt. Everest of the sporadic groups, and all the routes to it I know
involve a tough climb through all sorts of exceptional structures:
E
8
(see
 fiWeek 65fl
),
the Leech lattice (see
 fiWeek 20fl
), the Golay code, the Parker loop, the Griess algebra,
and more. I certainly don't understand this stuff....
Even before the Monster was proved to exist, it started casting its enormous shadow
over mathematics. For example, consider the theory of modular functions. What are
those? Well, consider a lattice in the complex plane, like this:
Re(
z
)
Im(
z
)
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
88
 WEEK 66 OCTOBER 10, 1995
These are important in complex analysis, as described in
 fiWeek 13fl
. To describe one of
these you can specify two fiperiodsfl
!
1
and
!
2
, complex numbers such that every point
in the lattice of the form
n!
1
+
m!
2
:
But this description is redundant, because if we choose instead to use
!
0
1
=
a!
1
+
b!
2
!
0
2
=
c!
1
+
b!
2
we'll get the same lattice as long as the matrix of integers

a b
c d

is invertible and its inverse also consists of integers. These transformations preserve the
fihandednessfl of the basis
!
1
,
!
2
if they have determinant
1
, and that's generally a good
thing to require. The group of
2

2
invertible matrices over the integers with determinant
1
is called
SL(2
;
Z
)
, or the fimodular groupfl in this context. I said a bit about it and its
role in string theory in
 fiWeek 64fl
.
Now, if we are only interested in parametrizing the different
shapes
of lattices, where
two rotated or dilated versions of the same lattice count as having the same shape, it
sufces to use one complex number, the ratio
˝
=
!
1
!
2
:
We might as well assume
˝
is in the upper halfplane,
H
, while we're at it. But for the
reason given above, this description is redundant; if we have a lattice described by
˝
,
and a matrix in
SL(2
;
Z
)
, we get a new guy
˝
0
which really describes the same shaped
lattice. If you work it out,
˝
0
=
a˝
+
b
c˝
+
d
:
So the space of different possible shapes of lattices in the complex plane is really the
quotient
H =
SL(2
;
Z
)
:
Now, a function on this space is just a function of
˝
that doesn't change when you replace
˝
by
˝
0
as above. In other words, it's basically just a function depending only on the shape
of a 2d lattice. Now it turns out that there is essentially just one finicefl function of this
sort, called
j
; all other finicefl functions of this sort are functions of
j
. (For experts, what
I mean is that the meromorphic
SL(2
;
Z
)
-invariant functions on
H
union the point at
innity are all rational functions of this function
j
.)
It looks like this:
j
(
˝
) =
q

1
+ 744 + 196884
q
+ 21493706
q
2
+
  
where
q
= exp(2
ˇ i˝
)
. In fact, starting from a simple situation, we have quickly gotten
into quite deep waters. The simplest explicit formula I know for
j
involves lattices in
24
-dimensional space! This could easily be due to my limited knowledge of this stuff,
89
 WEEK 66 OCTOBER 10, 1995
but it suits my present purpose: rst, we get a vague glimpse of where
E
8
and the Leech
lattice come in, and second, we get a vague glimpse of the mysterious signicance of the
numbers 24 and 26 in string theory.
So what is this
j
function, anyway? Well, it turns out we can dene it as follows.
First form the Dedekind eta function

(
q
) =
q
1
24
1
Y
n
=1
(1

q
n
)
:
This is not invariant under the modular group, but it transforms in a pretty simple way.
Then take the
E
8
lattice Š remember, that's a very nice lattice in 8 dimensions, in fact
the only fieven unimodularfl lattice in 8 dimensions, meaning that the inner product of
any two vectors in the lattice is even, and the volume of each fundamental domain in it
equals
1
. Now take the direct sum of 3 copies of
E
8
to get an even unimodular lattice
L
in 24 dimensions. Then form the theta function

(
q
) =
X
x
2
L
q
h
x;x
i
=
2
:
In other words, we take all lattice points
x
and sum
q
to the power of their norm squared
over
2
. Now we have
j
(
˝
) =

(
q
)

(
q
)
24
:
Quite a witches' brew of a formula, no? If someone could explain to me the deep
inner reason for
why
this works, I'd be delighted, but right now I am clueless. I will
say this, though: we could replace
L
with any other even unimodular lattice in 24 di-
mensions and get a function differing from
j
only by a constant. Guess how many even
unimodular lattices there are in 24 dimensions? Why, 24, of course! These fiNiemeier lat-
ticesfl were classied by Niemeier in 1968. All but one of them have vectors with length
squared equal to
2
, but there is one whose shortest vector has length squared equal to
4
, and that's the Leech lattice. This one has a very charming relation to
26
-dimensional
spacetime, described in
 fiWeek 20fl
.
Since the constant term in
j
can be changed by picking different lattices in 24 di-
mensions, and constant functions aren't very interesting anyway, we can say that the
rst interesting coefcient in the above power series for
j
is 196884. Then, right around
when the Monster was being dreamt up, McKay noticed that the dimension of its small-
est nontrivial representation, namely 196883, was suspiciously similar. Coincidence?
No. It turns out that all the coefcients of
j
can be computed from the dimensions of
the irreducible representations of the Monster! Similarly, Ogg noticed in the study of the
modular group, the primes 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59 and 71 play
a special role. He went to a talk on the Monster and noticed the ficoincidencefl. Then
he wrote a paper offering a bottle of Jack Daniels to anyone who could explain it. This
was the beginning of a subject called fiMonstrous Moonshinefl... the mysterious relation
between the Monster and the modular group.
Well, as it eventually turned out, one way to get ahold of the Monster is as a group
of symmetries of a certain algebra of observables for a string theory, or more precisely, a
fivertex operator algebrafl:
90
 WEEK 66 OCTOBER 10, 1995
5)
 Igor Frenkel, James Lepowsky, and Arne Meurman,
Vertex Operator Algebras and
the Monster
, Academic Press, Boston, 1988.
The relation of string theory to modular invariance and 26 dimensional spacetime then
fiexplainsfl some of the mysterious stuff mentioned above. (By the way, the authors of
the above book say the fact that there are 26 sporadic nite simple groups is just a
coincidence. I'm not so sure myself. . . not that I understand any of this stuff, but it's just
too spooky how the number 26 keeps coming up all over!)
Anway, now let me fast-forward to some recent news. I vaguely gather that people
would like to explain the relation between the Monster and string theory more deeply,
by nding a
24
-dimensional manifold having the Monster as symmetries, and cooking
up a eld theory of maps from the string worldsheet to this fiMonster manifoldfl, so that
the associated vertex operator algebra would have a good reason for having the Monster
as symmetries. Apparently Hirzebruch has offered a prize for anyone who could do this
in a nice way, by nding a fi24-manifold with
p
1
= 0
whose Witten genus is
(
j

C
P
2
. If its intersection form is even, we don't know yet, but if the fi11/8
conjecturefl is true, it must be a connected sum of
K3
's and
S
2

S
2
's. Here I cannot
resist adding that
K3
is a 4-manifold whose intersection form is
E
8

E
8

H

H

H
,
where
H
is the
2

2
matrix

0 1
1 0

and
E
8
is the nondegenerate symmetric
8

8
matrix describing the inner products of
vectors in the wonderful lattice, also called
E
8
, which I discussed in
 fiWeek 65fl
. So
E
8
raises its ugly head yet again.... By the way,
H
is just the intersection form of
S
2

S
2
,
while the intersection form of
C
P
2
is just the
1

1
matrix
(1)
.
Even if the 11/8 conjecture is not true, we could if necessary resort to Wall's theo-
rem, which implies that any 4-manifold becomes homeomorphic Š even diffeomorphic
Š to a connected sum of the 5 basic types of fibubblesfl after one takes its connected sum
with sufciently many copies of
S
2

S
2
. This suggests that if Euclidean path integral is
dominated by the case where there are lots of virtual black holes around, Hawking's ar-
guments could be correct at the level of diffeomorphism, rather than merely homeomor-
phism. Indeed, he says that fiin the wormhole picture, one considered metrics that were
94
 WEEK 67 OCTOBER 23, 1995
multiply connected by wormholes. Thus one concentrated on metrics [I'd say topolo-
gies!] with large values of the rst Betti number[....] However, in the quantum bubbles
picture, one concentrates on spaces with large values of the second Betti number.fl
4)
 Ted Jacobson, fiThermodynamics of spacetime: the Einstein equation of statefl,
Phys. Rev. Lett.
75
(1995), 1260Œ1263. Also available as
gr-qc/9504004
.
Well, here's another paper on quantum gravity, also very good, which seems at rst
to directly contradict Hawking's paper. Actually, however, I think it's another piece in
the puzzle. The idea here is to derive Einstein's equation from thermodynamics! More
precisely, fiThe key idea is to demand that this relation hold for all the local Rindler causal
horizons through each spacetime point, with [the change in heat] and [the temperature]
interpreted as the energy ux and Unruh temperature seen by an accelerated observer
just inside the horizon. This requires that gravitational lensing by matter energy distorts
the causal structure of spacetime in just such a way that the Einstein equation holdsfl.
It's a very clever mix of classical and quantum (or semiclassical) arguments. It suggests
that all sorts of quantum theories on the microscale could wind up yielding Einstein's
equation on the macroscale.
5)
 Lee Smolin, fiThe Bekenstein bound, topological quantum eld theory and plural-
istic quantum eld theoryfl, available as
gr-qc/9508064
.
This is a continued exploration of the themes of Smolin's earlier paper, reviewed in
 fiWeek
56fl
 and
 fiWeek 57fl
. Particularly interesting is the general notion of fipluralistic quantum
eld theoryfl, in which different observers have different Hilbert spaces. This falls out
naturally in the
n
-categorical approach pursued by Crane (see
 fiWeek 56fl
), which I am
also busily studying.
6)
 Daniel Armand-Ugon, Rodolfo Gambini, Octavio Obregon and Jorge Pullin, fiTo-
wards a loop representation for quantum canonical supergravityfl,
Nucl. Phys. B
460
(1996), 615Œ631. Also available as
hep-th/9508036
.
Some knot theorists and quantum group theorists had better take a look at this! This pa-
per considers the analog of
SU(2)
ChernŒSimons theory where you use the supergroup
GSU(2)
, and perturbatively work out the skein relations of the associated link invariant
(up to a certain low order in
~
). If someone understood the quantum supergroup fiquan-
tum
GSU(2)
fl, they could do this stuff nonperturbatively, and maybe get an interesting
invariant of links and 3-manifolds, and make some physicists happy in the process.
7)
 Roh Suan Tung and Ted Jacobson, fiSpinor one-forms as gravitational potentialsfl,
Class. Quant. Grav.
12
(1995), L51ŒL55. Also available as
gr-qc/9502037
.
This paper writes out a new Lagrangian for general relativity, closely related to the action
that gives general relativity in the Ashtekar variables. It's incredibly simple and beautiful!
I am hoping that if I work on it someday, it will explain to me the mysterious relation
between quantum gravity and spinor elds (see the end of
 fiWeek 60fl
).
8)
 Joseph Polchinski and Edward Witten, fiEvidence for heteroticŒtype I string dual-
ityfl,
Nucl. Phys. B
460
(1996), 525Œ540. Also available as
hep-th/9510169
.
95
 WEEK 67 OCTOBER 23, 1995
I'm no string theorist, so I've been lagging vastly behind the new work on fidualitiesfl
that has revived interest in the subject. Roughly speaking, though, it seems folks have
discovered a host of secret symmetries relating supercially different string theories...
making them, in some deeper sense, the same. The heterotic and type I strings are
two of the most famous string theories, so if they were really equivalent as this paper
suggests, it would be very interesting.
96
 WEEK 68 OCTOBER 29, 1995
Week 68
October 29, 1995
Okay, now the time has come to speak of many things: of topoi, glueballs, communica-
tion between branches in the many-worlds interpretation of quantum theory, knots, and
quantum gravity.
1)
 Robert Goldblatt,
Topoi: the Categorial Analysis of Logic
, Dover, Mineola, New
York, 2006. Also available as
https://projecteuclid.org/ebooks/books-by-
independent-authors/Topoi-The-Categorial-Analysis-of-Logic/toc/bia/
1403013939
.
If you've ever been interested in logic, you've got to read this book. Unless you learn a bit
about topoi, you are really missing lots of the fun. The basic idea is simple and profound:
abstract the basic concepts of set theory, so as to dene the notion of a fitoposfl, a kind of
universe like the world of classical logic and set theory, but far more general!
For example, there are fiintuitionisticfl topoi in which Brouwer reigns supreme Š
that is, you can't do proof by contradiction, you can't use the axiom of choice, etc.
There is also the fieffective toposfl of Hyland in which Turing reigns supreme Š for
example, the only functions are the effectively computable ones. There is also a finitaryfl
topos in which all sets are nite. So there are topoi to satisfy various sorts of ascetic
mathematicians who want a stripped-down, minimal form of mathematics.
However, there are also topoi for the folks who want a mathematical universe with
lots of horsepower and all the options! There are topoi in which everything is a function
of time: the membership of sets, the truth-values of propositions, and so on all depend
on time. There are topoi in which everything has a particular group of symmetries. Then
there are
really
high-powered things like topoi of sheaves on a category equipped with a
Grothendieck topology....
And so on: not an attempt to pick out fithefl universe of logic and mathematics, but
instead, an effort to systematically examine a bunch of them and how they relate to each
other. The details can be intimidating, but Goldblatt explains them very nicely. A glance
at the subject headings reveal some of the delights in store: fielementary truthfl, filocal
truthfl, figeometric logicfl, etc.
What is a topos, precisely? Well, most people would need to limber up a little bit
before getting the precise denition... so let me just start you off with some mental
stretching exercises. In classical logic we are used to working with two truth values,
True
and
False
. Let's call the set of truth values


that I was talking about.
To get deeper into topos theory, try:
3)
 Michael Barr and Charles Wells,
Toposes, Triples and Theories
, Springer, Berlin,
1983. Also available as
http://www.tac.mta.ca/tac/reprints/articles/12/
tr12abs.html
.
Now let me catch up on some things more directly related to physics:
4)
 Frank Close, fiAre glueballs and hybrids found?fl, in
Hadron'95: The 6th Interna-
tional Conference on Hadron Spectroscopy, the University of Manchester, Manchester,
UK, 10th-14th July 1995
, World Scientic, Singapore, 1996. Also available as
hep-ph/9509245
.
5)
 J. Sexton, A. Vaccarino and D. Weingarten, fiNumerical evidence for the observation
of a scalar glueballfl,
Phys. Rev. Lett.
75
(1995), 4563-4566. Also available as
hep-lat/9510022
.
Thanks go to Greg Kilcup for bringing these to my attention. Have they found a glue-
ball??? That would be really exciting. What's a glueball, you ask? Well, quantum
chromodynamics, our best theory of the strong force, says that that the strong force is
carried by particles called figluonsfl. Like electromagnetism, the strong force is a gauge
eld, but it's a nonabelian gauge eld, so the gluons themselves have charge, or ficolorfl.
Thus they interact in a nonlinear way. This is what lets them bind together quarks in such
a tight way. But perhaps, in addition to pairs of quarks and antiquarks held together by
gluons Š i.e., mesons Š and triples of quarks held together by gluons Š i.e., baryons
Š there could be short-lived assemblages consisting entirely of gluons, held together by
their self-interactions. These are called glueballs, but we don't know if these exist.
However, to my surprise, it turns out that there are now some candidates out there!
The rst paper suggests that the
f
0
(1500)
, a neutral spin-zero particle with mass around
1500 MeV, is a glueball. The second paper argues instead that this is basically a quark-
antiquark pair (made of a strange quark and a strange antiquark... where fistrangefl is
the technical name for one of the 6 quarks!). It presents evidence from a numerical
simulation and argues that the fi

fl or
f
J
(1710)
, a neutral particle with even spin and
mass 1710 MeV, is a glueball. Part of the subtlety here is that, thanks to the superposition
99
 WEEK 68 OCTOBER 29, 1995
principle, there is not a perfectly sharp distinction between a glueball with some virtual
quark-antiquark pairs in it, and a quark-antiquark pair with a bunch of virtual gluons in
it. There can be fihybridsfl that are a bit of both a linear combination of a meson and a
glueball! (This phenomenon of fihybridizationfl is also familiar in chemistry.)
It's tough to do nonperturbative computations in nonlinear gauge eld theories Š
basically one needs to approximately compute a path integral, using Monte Carlo tech-
nique, approximating spacetime by a lattice (in this case, a
16

16

16

24
lattice).
Computing the properties of a glueball and matching it with an experimentally observed
particle would be a marvelous conrmation of quantum chromodynamics. In addition,
I nd there to be something charming about the idea that in a nonabelian gauge theory
we could have a particle made simply of the gauge eld itself.
5)
 R. Plaga, fiProposal for an experimental test of the many-worlds interpretation of
quantum mechanicsfl, available as
quant-ph/9510007
.
John Gribbin brought this one to my attention and asked me what I thought about it.
Basically, the idea here is to isolate an ion from its environment in an fiion trapfl, and then
perform a measurement on it with two possible outcomes on another quantum system,
and to excite the ion only if the rst outcome occurs, before the ion has had time to
fidecoherefl or get fientangledfl with the environment. Then one checks to see if the ion is
excited. The idea is that even if we didn't see the outcome that made us excite the ion,
we might see the ion excited, because it was excited in the other fiworldfl or fibranchfl
Š the one in which we
did
see the outcome that made us excite the ion. The author
gets fairly excited himself, suggesting that fioutside physics, interworld communication
would lead to truly mind-boggling possibilitiesfl.
Does this idea really make sense? First of all, I don't think of this sort of thing as a test
of the many-worlds interpretation; I think that all suf ciently sensible interpretations of
quantum mechanics (not necessarily
very
sensible, either!) give the same concrete pre-
dictions for all experiments, when it comes to what we actually observe. They may make
us tell very different stories about what is happening behind the scenes, but not of any
testable sort. As soon as one comes up with something that makes different predictions,
I think it is (more or less by denition) not a new fiinterpretationfl of quantum theory but
an actual new theory. And I don't think the many-worlds interpretation is that.
So the question as I see it is simply, will this experiment work? Will we sometimes see
the ion excited even when we didn't excite it? It seems hard; usually the decoherence
between the two fibranchesfl prevents this kind of fiinter-world communicationfl (not that
I'm particularly fond of this way of talking about it). What exactly is supposed to make
this case different? The problem is that the paper is quite sketchy at the crucial point...
just when the rabbit being pulled from the hat, as it were. I haven't put much time into
analyzing it, but some people interested in this sort of thing might enjoy having a go at
it.
6)
 Nicholas Landsman, fiAgainst the WheelerŒDeWitt equationfl, available as
gr-qc/
9510033
.
I haven't read this one yet, but I had some nice talks with Landsman about his ideas
on quantization of constrained systems (see
 fiWeek 60fl
) back when I was in Cambridge,
100
 WEEK 68 OCTOBER 29, 1995
England. Quantizing constrained systems is the main problem with the so-called ficanon-
icalfl approach to quantum gravity (see
 fiWeek 43fl
), so I was eager to see it applied to
gravity, and I guess that's what he's done. The title of the paper is deliberately provoca-
tive... hmmm, I guess I'd better read it soon! Here's the abstract:
The ADM approach to canonical general relativity combined with Dirac's method
of quantizing constrained systems leads to the WheelerŒDeWitt equation. A
number of mathematical as well as physical difculties that arise in connection
with this equation may be circumvented if one employs a covariant Hamilto-
nian method in conjunction with a recently developed, mathematically rigorous
technique to quantize constrained systems using Rieffel induction. The classical
constraints are cleanly separated into four components of a covariant momen-
tum map coming from the diffeomorphism group of spacetime, each of which
is linear in the canonical momenta, plus a single nite-dimensional quadratic
constraint that arises in any theory, parametrized or not. The new quantiza-
tion method is carried through in a minisuperspace example, and is found to
produce a fiwavefunction of the universefl. This differs from the proposals of
both Vilenkin and Hartle-Hawking for a closed FRW universe, but happens to
coincide with the latter in the open case.
7)
 Pavel Etingof and David Kazhdan, fiQuantization of Lie bialgebras, Ifl, available as
q-alg/9506005
.
fiQuantization of Poisson algebraic groups and Poisson homogeneous spacesfl, avail-
able as
q-alg/9510020
.
It sounds like Etinghof and Kazhdan are making serious progress on some questions of
Drinfeld about when you can quantize Lie bialgebras and their kin. More stuff I need
to read! I need to invent a time machine and keep running it backwards to make my
weekends longer and read this stuff!
8)
 Steve Carlip, fiStatistical mechanics and black hole entropyfl, available as
gr-qc/
9509024
.
Claudio Teitelboim, fiStatistical thermodynamics of a black hole in terms of surface
eldsfl, available as
hep-th/9510180
.
Steve Carlip's paper is a nice introduction to recent ideas, many of them his, on deriving
black hole area/entropy relations by thinking of the entropy as associated to degrees of
freedom of a eld living on the event horizon. I haven't read Teitelboim's paper, but it
sounds related.
9)
 Jorge Griego, fiIs the third coefcient of the Jones knot polynomial a quantum state
of gravity?fl, available as
gr-qc/9510051
.
fiThe Kauffman bracket and the Jones polynomial in quantum gravityfl, available
as
gr-qc/9510050
.
In the loop representation of quantum gravity, states of quantum gravity give rise to
link invariants. Which link invariants, though? The Kauffman bracket comes from a
101
 WEEK 68 OCTOBER 29, 1995
state of quantum gravity with cosmological constant... that is something I understand
pretty well by now. But Gambini and Pullin also have an argument suggesting that the
second coefcient of the Jones polynomial (also known as the Arf invariant) is a state of
quantum gravity without cosmological constant. I've tried to make this argument more
rigorous and never succeeded. They also oated a conjecture that
all
the coefcients of
the Jones polynomial are states of quantum gravity. This confuses me a lot, because the
Jones polynomial depends on the orientations of the components of a link, while states
of quantum gravity should give link invariants that are independent of orientations. I
guess all the odd coefcients of the Jones polynomial are orientation dependent. Thus
I'm not shocked that Griego has done calculations indicating that the third coefcient
does
not
come from a state of quantum gravity.
102
 WEEK 69 NOVEMBER 11, 1995
Week 69
November 11, 1995
One of the great things about starting to work on quantum gravity was getting to know
some of the people in the eld. Ever since the development of string theory and the loop
representation of quantum gravity, there has been a fair amount of interest in under-
standing how quantum theory and gravity t together. Indeed, now th at the Standard
Model seems to be giving a spectacularly accurate description of all the forces
except
gravity, quantum gravity is one of the few really big mysteries left when it comes to
working out the basic laws of physics Š or at least, one of the few
obvious
big mysteries.
(As soon as one mystery starts becoming less mysterious, new mysteries tend to become
more visible.) But back when particle physics was big business, only a few rather special
sorts of people were seriously devoted to quantum gravity. These people seem to be
often more than averagely interested in philosophy, often more interested in mathemat-
ics (which is one of the few solid handholds in this slippery subject), and always more
resigned to the fact that Nature does not reveal all her secrets very readily.
One of these folks is Chris Isham, whom I rst saw at a conference in Seattle in
1991. The conference was on classical eld theory but somehow he, Abhay Ashtekar,
and Renate Loll sneaked in and gave some talks on the loop representation of quantum
gravity. This is when I rst became really interested in this subject, which I was later to
work on quite a bit. I remember Isham saying how he had been working on quantum
gravity for many years, and that he'd gotten used to the fact that nothing ever worked,
but that
this
approach
seemed
to be working so far. He went on to talk about work he'd
done with Ashtekar on making the loop representation rigorous, which was based on
GelfandŒNaimark spectral theory. He said that as a student, when he'd learned about this
theory, he was really excited, because it completely depends on the fact that if we have
a space
X
, we can think of any point
x
in
X
as a functional on the space of functions
on
X
, basically dening by dening
x
(
f
)
to be
f
(
x
)
. He said this with a laugh, but I
knew what he meant, because I too had found this idea tremendously exciting when I
rst learned the GelfandŒNaimark theory. I guess it's something about how what seems
at rst like some sort of bizarre joke can turn out to be very useful....
Anyway, later, when I decided to work on this sort of thing and was trying to learn
more about quantum gravity, I found his review article on the problem of time (see
 fiWeek
9fl
) tremendously helpful, and I constantly recommend it to everyone who is trying to
get their teeth into this somewhat elusive issue. So it's not surprising that Isham gures
prominently in the following nice popular article on the problem of time:
1)
 Marcia Bartusiak, fiWhen the universe began, what time was it?fl,
Technology Review
(edited at the Massachusetts Institute of Technology), November/December 1995,
pp. 54-63.
If you can nd this, read it: it also features Karel Kuchar and Carlo Rovelli.
This spring, I visited Isham at Imperial College in London and found him to be just as
interesting in person as in print, and not at all scary... a bit of an cynic about all existing
approaches to quantum gravity (probably because he sees so clearly how awed they all
are), but thoroughly good-humored about it and perfectly open to all sorts of ideas, even
my own nutty ideas about
n
-categories and physics.
103
 WEEK 69 NOVEMBER 11, 1995
Anyway, Isham has recently written a review article on quantum gravity that gives a
nice overview of the basic issues of the eld:
2)
 C. J. Isham, fiStructural issues in quantum gravityfl, plenary session lecture given
at the GR14 conference, Florence, August 1995, available as
gr-qc/9510063
.
One interesting thing about it is the emphasis on the question of whether spacetime is
really a manifold the way we all usually think, or perhaps something that just looks like a
manifold at sufciently large distance scales. This is one of those fundamental issues that
is rather hard to make direct progress on; one has to sort of sneak up on it, but it's nice to
see someone boldly holding the problem up for examination. Often the most important
issues are the ones everyone is scared to talk about, because they are so intractable.
Much of Abhay Ashtekar's early work dealt with asymptotically at solutions of Ein-
stein's equation, but in about 1986 he somehow invented a new formulation of general
relativity, which everyone now calls the finew variablesfl or fiAshtekar variablesfl. In terms
of these new variables general relativity looks a whole lot more like YangŒMills theory
(the theory of all the forces
except
gravity), and this let Rovelli and Smolin formulate a
radical new approach to quantum gravity, the filoop representationfl. (For a fun, non-
technical introduction to this, try the article by Bartusiak reviewed in
 fiWeek 10fl
.)
Nowadays, Ashtekar is the main person behind the drive to make the loop represen-
tation of quantum gravity into a mathematically rigorous theory. Thus it's natural that
after that rst time in Seattle I would wind up seeing him pretty often... rst at Syra-
cuse University and then at the Center for Gravitational Physics and Geometry which
he started at Penn State. It's really impressive how he has organized people into an ef-
fective team there, and how he is systematically converting people's hopes and dreams
concerning the loop representation into a beautiful set of rigorous
theorems
. For a good
mathematical introduction to his program, see his paper reviewed in
 fiWeek 7fl
. A less
mathematical introduction is:
3)
 Abhay Ashtekar, fiPolymer geometry at Planck scale and quantum Einstein equa-
tionsfl,
Int. J. Mod. Phys. D
5
(1996), 629Œ648. Also available as
hep-th/9601054
.
I have also seen Renate Loll fairly often in the years since that Seattle conference. She
is younger than Ashtekar and Isham (in fact, she was a postdoc with Isham at one point),
hence less intimidating to me, which meant that I really enjoyed pestering her with
stupid questions when I was just starting to learn about this loop representation stuff.
One of her specialities is lattice gauge theory, and recently she has developed a lattice
version of quantum gravity that is eminently suitable for computer calculations. The last
time I saw her was at a conference in Warsaw this spring (as reported in
 fiWeek 55fl
 and
fiWeek 56fl
). In the process of working on her lattice approach, she gave Rovelli and
Smolin a big shock by turning up an error in their computation of the volume operator
in quantum gravity. A state of quantum gravity can be visualized roughly as a graph
embedded in space, with edges labelled by spins. Rovelli and Smolin had thought there
were states of nonzero volume corresponding to graphs with only trivalent vertices (3
edges meeting a vertex, that is). As it turns out, they'd made a sign error, and these
states have zero volume; you need a quadrivalent vertex to get some volume. She has
just written a paper on this topic:
104
 WEEK 69 NOVEMBER 11, 1995
4)
 Renate Loll, fiSpectrum of the volume operator in quantum gravityfl, 14 pages in
plain tex, with 4 gures (postscript, compressed and uu-encoded), available as
gr-qc/9511030
.
The abstract reads as follows:
The volume operator is an important kinematical quantity in the non-perturbative
approach to four-dimensional quantum gravity in the connection formulation.
We give a general algorithm for computing its spectrum when acting on four-
valent spin network states, evaluate some of the eigenvalue formulae explicitly,
and discuss the role played by the Mandelstam constraints.
fiNothing is too wonderful to be true, if it be consistent with the laws of
nature, and in such things as these, experiment is the best test of such con-
sistency.fl
Š Faraday, laboratory diaries, entry 10,040, March 19, 1849.
105
 WEEK 70 NOVEMBER 26, 1995
Week 70
November 26, 1995
Probably many of the mathematicians reading this know about the Newton Institute in
Cambridge, a mathematics institute run by Sir Michael Atiyah. It's a cozy little building,
in a quiet neighborhood a certain distance from the center of town, which one can
reach by taking a nice walk or bike ride over the bridge near Trinity College, across
Grange Road, and down Clarkson Road. Inside it's one big space, with stairways slightly
reminiscent of a certain picture by Escher, with a nice little library on the rst oor, tea
and coffee on the 3rd oor, blackboards in the bathrooms... everything a mathematician
could want. This is where Wiles rst announced his proof of Fermat's last theorem, and
they sell T-shirts there commemorating that fact, which are unfortunately too small to
contain the proof itself... as they do not refrain from pointing out.
I just got back from a conference there on New Connections between Mathematics
and Computer Science. It was organized by Jeremy Gunawardena, who was eager to
expose computer scientists and mathematicians to a wide gamut of new interactions
between the two subjects. I spoke about
n
-categories in logic, topology and physics.
Since I don't know anything about computer science, when I rst got the invitation
I thought it was a mistake: a wrong email address or something! But Gunawardena
assured me otherwise. I assumed the idea was that
n
-categories, being so abstract, must
have
some
application to just about
everything
, even computer science. Luckily, some
other speakers at the conference gave some very nice applications of
n
-category theory
to computer science, so now I know they really exist.
Unfortunately I had to miss the beginning of the conference, and therefore missed
some interesting talks of a geometrical nature by Smale, Gromov, Shub and others. Let
me say a bit about some of the talks I did catch. You can nd a list of all the speakers
and abstracts of their talks here:
1)
 Jeremy Gunawardena, fiNew connections between mathematics and computer sci-
ence: reports, abstracts and bibliography of a workshopfl, January 1996. Available
at
https://www.hpl.hp.com/techreports/96/HPL-BRIMS-96-02.pdf
Richard Jozsa gave an interesting talk on quantum computers, in part outlining Peter
Shor's work (see
 fiWeek 34fl
) on efcient factoring via quantum computation, but also
presenting some new results on ficounterfactual quantum computationfl. It turns out that
Š in principle Š in some cases you can get a quantum computer to help you answer
a question, even without running it, just as long as you
could have
run it! (I should
add that in practice a lot of things make this quite impractical.) This is a new twist on
the Elitzur-Vaidman bomb-testing paradox about how if you have a bunch of bombs and
half of them are duds, and the only way you can test a bomb is by lighting the fuse and
seeing if it goes off, you can still get a bomb you're sure will work, if you use quantum
mechanics. The trick involves getting a fuse that's so sensitive that even one photon
will make the bomb go off, and then setting up a beam-splitter, and using the bomb to
measure which path the photon followed, before recombining the beams. Check out:
2)
 Avshalom C. Elitzur and Lev Vaidman, fiQuantum mechanical interaction-free mea-
106
 WEEK 70 NOVEMBER 26, 1995
surementsfl,
Foundations of Phys.
23
(1993), 987Œ997. Also available as
hep-th/
9305002
.
Graeme Mitchison and Richard Jozsa, Counterfactual quantum computation,
Proc.
Roy. Soc. Lond.
A457
(2001) 1175Œ1194. Also available as
quant-ph/9907007
.
Jean-Yves Girard gave an overview of linear logic. Linear logic is a new version of
logic that he invented, which has some new operations besides the good old ones like
fiandfl, fiorfl, and finotfl. For example, there are things like fiparfl (written as an upside-
down ampersand), fi!fl (usually pronounced fibangfl) and fi?fl. Ever since I started going
to conferences on category theory and computer science I have been hearing a lot about
it, and I keep trying to get people to explain these weird new logical operations to me.
Unfortunately, I keep getting very different answers, so it has remained rather mysterious
to me, even though it seems like a lot of fun (see
 fiWeek 40fl
). Thus I was eager to hear
it from the horse's mouth.
Indeed, Girard gave a fascinating talk on it which almost made me feel I understood
it. I think the big thing I'd been missing was a good appreciation of topics in proof theory
like ficut eliminationfl. He noted that this subject usually appears to be all about the
precise manipulation of formulas according to purely syntactic rules: fiVery bureaucraticfl
he joked, fione parenthesis missing and you've had it!fl (For full effect, one must imagine
this being said in a French accent by someone stylishly dressed entirely in black.) He
wanted to get a more
geometrical
way to think about proofs, but to do this it turned
out to be important to rene ordinary logic in certain ways. . . . leading to linear logic.
However, I still don't feel up to explaining it, so let me turn you to:
3)
 Jean-Yves Girard, fiLinear logicfl,
Theoretical Computer Science
50
, 1Œ102, 1987.
Jean-Yves Girard, Y. Lafont and P. Taylor,
Proofs and Types
, Cambridge U. Press,
Cambridge, 1989. Also available at
http://www.paultaylor.eu/stable/Proofs+Types.
html
.
Eric Goubault and Vaughan Pratt talked, in somewhat different ways, about a for-
malism for treating concurrency using fihigher-dimensional automatafl. The basic idea is
simple: say we have two jobs to do, one of which gets us from some starting-point
A
to
some result
B
, and the other of which gets us from
A
0
to
B
0
. We can represent each task
by an arrow, as follows:
A
!
B
A
0
!
B
0
We can think of this arrow as a fimorphismfl, that is, a completely abstract sort of opera-
tion taking
A
to
B
. Or, we can think of it more concretely as an interval of time, where
our computer is doing something at each moment. Alternatively, we can think of it more
discretely as a sequence of steps, starting with
A
and winding up with
B
.
If we now consider doing both these tasks concurrently, we can represent the situa-
tion by a square:
AA
0
B A
0
AB
0
B B
0
107
 WEEK 70 NOVEMBER 26, 1995
Going rst across and then down corresponds to completing one task before starting
the other, while going rst down and then across corresponds to doing the other one
rst. However, we can also imagine various roughly diagonal paths through the square,
corresponding to doing both tasks at the same time. We might go horizontally for a
while, then vertically, then diagonally, and so on. Of course, if the two tasks were not
completely independent Š for example, if some steps of one could only occur after some
steps of the other were nished Š we would have some constraints on what paths from
AA
0
to
B B
0
were allowed. The idea is then to model these constaints as fiholesfl in
the square, forbidden regions where the path cannot go. There may then be several
fiessentially distinctfl ways of getting from
AA
0
to
B B
0
, that is, classes of path s that
cannot be deformed into each other.
To anyone who knows homotopy theory, this will seem very familiar, homotopy the-
ory being all about spaces with holes in them, and how those holes prevent you from
continuously deforming one path into another. Goubault's title, fiScheduling problems
and homotopy theoryfl, emphasized the relationships. But there are also some big differ-
ences. Unlike homotopy theory, here the paths are typically required to be fimonotonicfl:
they can't double back and go backwards in time. And, as I mentioned, the tasks can be
thought of more abstractly than as paths in some space. So we are really talking about
2
-categories here: they give a general framework for studying situations with fidotsfl or
fiobjectsfl, fiarrows between dotsfl or fimorphismsfl, and fiarrows between arrows between
dotsfl or fi2-morphismsfl. Similarly, when we study concurrency with more than 2 tasks
at a time we can think of it in terms of
n
-categories.
By the way, since I don't know much about parallel processing, I'm not sure how
much the above formalism actually helps the fiworking manfl. Probably not much, yet.
I get the impression, however, that parallel processing is a complicated problem, and
that people are busily dreaming up new formalisms for talking about it, hoping they will
eventually be useful for inventing and analyzing parallel programming languages.
Some references for this are:
4)
 Eric Goubault, fiSchedulers as abstract interpretations of higher-dimensional au-
tomatafl, in
Proc. PEPM '95 (La Jolla)
, ACM Press, 1995. Also available at
https:/
/dl.acm.org/doi/abs/10.1145/215465.215577
.
Eric Goubault and Thomas Jensen, fiHomology of higher-dimensional automatafl,
in
Proc. CONCUR '92 (New York)
, Lecture Notes in Computer Science
630
, Springer,
1992. Also available at
http://www.lix.polytechnique.fr/
˘
goubault/papers/
Homology.pdf
.
5)
 Vaughan Pratt, fiTime and information in sequential and concurrent computationfl,
in
Proc. Theory and Practice of Parallel Programming
, Sendai, Japan, 1994. Also
available at
http://boole.stanford.edu/pub/tppp.pdf
.
Yves Lafont also gave a talk with strong connections to
n
-category theory. Recall that
a monoid is a set with an associative product having a unit element. One way to describe
a monoid is by giving a presentation with figeneratorsfl, say
a; b; c; d;
and firelationsfl, say
ab
=
a; da
=
ac:
108
 WEEK 70 NOVEMBER 26, 1995
We get a monoid out of this in an obvious sort of way, namely by taking all strings built
from the generators
a
,
b
,
c
, and
d
, and then identifying two strings if you can get from one
to the other by repeated use of the relations. In math jargon, we form the free monoid
on the generators and then mod out by the relations.
Suppose our monoid is nitely presented, that is, there are nitely many generators
and nitely many relations. How can we tell whether two elements of it are equal? For
example, does
dacb
=
acc
in the above monoid? Well, if the two are equal, we will always eventually nd that out
by an exhaustive search, applying the relations mechanicallly in all possible ways. But if
they are not, we may never nd out! (For the above example, the answer appears at the
end of this article in case anyone wants to puzzle over it. Personally, I can't stand this
sort of puzzle.) In fact, there is no general algorithm for solving this fiword problem for
monoidsfl, and in fact one can even write down a
specic
nitely presented monoid for
which no algorithm works.
However, sometimes things are nice. Suppose you write the relations as firewrite
rulesfl, that go only one way:
ab
!
a
da
!
ac
Then if you have an equation you are trying to check, you can try to repeatedly apply
the rewrite rules to each side, reducing it to finormal formfl, and see if the normal forms
are equal. This will only work, however, if some good things happen! First of all, your
rewrite rules had better terminate: it had better be that you can only apply them nitely
many times to a given string. This happens to be true for the above pair of rewrite rules,
because both rules decrease the number of
b
's and
c
's. Second of all, your rewrite rules
had better be conuent: it had better be that if I use the rules one way until I can't go any
further, and you use them some other way, that we both wind up with the same thing! If
both these hold, then we can reduce any string to a unique normal form by applying the
rules until we can't do it any more.
Unfortunately, the rules above aren't conuent; if we start with the word
dab
, you
can apply the rules like this
dab
!
acb
while I apply them like this
dab
!
da
!
ac
and we both terminate, but at different answers. We could try to cure this by adding a
new rule to our list,
acb
!
ac:
This is certainly a valid rule, which cures the problem at hand... but if we foolishly keep
adding new rules to our list this way we may only succeed in getting conuence and
109
 WEEK 70 NOVEMBER 26, 1995
termination when we have an
innite
list of rules:
ab
!
a
da
!
ac
acb
!
ac
accb
!
acc
acccb
!
accc
accccb
!
acccc
.
.
.
.
.
.
and so on. I leave you to check that this is really terminating and conuent. Because
it is, and because it's a v ery predictable list of rules, we can use it to write a computer
program in this case to solve the word problem for the monoid at hand. But in fact, if
we had been cleverer, we could have invented a
nite
list of rules that was terminating
and conuent:
ab
!
a
ac
!
da
Lafont went on to describe some work by Squier:
6)
 Craig C. Squier, fiWord problems and a homological niteness condition for monoidsfl,
Jour. Pure Appl. Algebra
49
(1987), 201Œ217. Also available at
https://link.
springer.com/content/pdf/10.1007%2F3-540-17220-3
7.pdf
Craig C. Squier, fiA niteness condition for rewriting systemsfl, revision by F. Otto
and Y. Kobayashi,
Theoretical Computer Science
131
(1994), 271Œ294.
Craig C. Squier and F. Otto, fiThe word problem for nitely presented monoids
and nite canonical rewriting systemsfl, in
Rewriting Techniques and Applications
,
ed. J. P. Jouannuad, Lecture Notes in Computer Science
256
, Springer, Berlin,
1987, pp. 74Œ82. Also available at
https://link.springer.com/content/pdf/
10.1007%2F3-540-17220-3
7.pdf
which gave general conditions wh ich must hold for there to be a nite terminating and
conuent set of rewrite rules for a monoid. The nice thing is that this relies heavily on
ideas from
n
-category theory. Note: we started with a monoid in which the relations are
equations
, but we then started thinking of the relations as rewrite rules or
morphisms
,
so what we really have is a monoidal category. We then started worrying about ficonu-
encesfl, or equations between these morphisms. This is typical of ficategoricationfl, in
which equations are replaced by morphisms, which we then want to satisfy new equa-
tions (see
 fiWeek 38fl
).
For the experts, let me say exactly how it all goes. Given any monoid
M
, we can
cook up a topological space called its ficlassifying spacefl
K M
, as follows. We can think
of
K M
as a simplicial complex. We start by sticking in one 0-simplex, which we can
visualize as a dot like this:

110
 WEEK 70 NOVEMBER 26, 1995
Then we stick in one
1
-simplex for each element of the monoid, which we can visualize
as an arrow going from the dot to itself. Unrolled a bit, it looks like this:

a

Really we should draw an arrow going from left to right, but soon things will get too
messy if I do that, so I won't. Then, whenever we have
ab
=
c
in the monoid, we stick in
a
2
-simplex, which we can visualize as a triangle like this:

c

b

a
Then, whenever we have
abc
=
d
in the monoid, we stick in a
3
-simplex, which we can
visualize as a tetrahedron like this

d

bc

a
ab

b
c
And so on.... This is a wonderful space whose homology groups depend only on the
monoid, so we can call them
H
k
(
M
)
. If we have a presentation of
M
with only nitely
many generators, we can build
K M
using
1
-simplices only for those generators, and it
follows that
H
1
(
M
)
is nitely generated. (More precisely, we can build a space with the
same homotopy type as
K M
using only the generators in our presentation.) Similarly, if
we have a presentation with only nitely many relations, we can build
K M
using only
nitely many
2
-simplices, so
H
2
(
M
)
is nitely generated. What Squier showed is that if
we can nd a nite list of rewrite rules for M which is terminating and conuent, then
we can build
K M
using only nitely many
3
-simplices, so
H
3
(
M
)
is nitely generated!
What's nice about this is that homological algebra gives an easy way to compute
H
k
(
M
)
given a presentation of
M
, so in some cases we can
prove
that a monoid has no nite list
of rewrite rules for
M
which is terminating and conuent, just by showing that
H
3
(
M
)
is too big. Examples of this, and many further details, appear in Lafont's work:
7)
 Yves Lafont and Alain Proute, fiChurch-Rosser property and homology of monoidsfl,
Mathematical Structures in Computer Science
1
(1991), 297Œ326. Also available at
http://iml.univ-mrs.fr/
˘
lafont/publications.html
Yves Lafont, fiA new niteness condition for monoids presented by complete rewrit-
ing systems (after Craig C. Squier)fl,
Journal of Pure and Applied Algebra
98
(1995),
229Œ244. Also available at
http://iml.univ-mrs.fr/
˘
lafont/publications.
html
111
 WEEK 70 NOVEMBER 26, 1995
There were many other interesting talks, but I think I will quit here. Next time I want
to talk a bit about topological quantum eld theory. (Of course, folks who read
 fiWeek
38fl
 will know that Lafont's work is deeply related to topological qu antum eld theory...
but I won't go into that now.)
(Answer:
dacb
=
ddab
=
dda
=
dac
=
acc
.)
112
 WEEK 71 DECEMBER 3, 1995
Week 71
December 3, 1995
This week I will get back to mathematical physics... but before I do, I can't resist adding
that in my talk in that conference I announced that James Dolan and I had come up
with a denition of weak
n
-categories. (For what these are supposed to be, and what
they have to do with physics, see
 fiWeek 38fl
,
 fiWeek 49fl
, and
 fiWeek 53fl
.) John Power
was at the talk, and before long his collaborator Ross Street sent me some email from
Australia asking about the denition. Gordon, Power, and Street have done a lot of work
on
n
-categories Š see
 fiWeek 29fl
. Now, Dolan and I have been struggling for several
months to put this denition onto paper in a reasonably elegant and comprehensible
form, so Street's request was a good excuse to get something done quickly... sacricing
comprehensibility for terseness. The result can be found in
1)
 John Baez and James Dolan, fi
n
-Categories, sketch of a denitionfl, available at
http://math.ucr.edu/home/baez/ncat.def.html
A more readable version will appear as a paper fairly soon. I should add that this will
eventually be part of Dolan's thesis, and he has done most of the hard work on it; my
role has largely been to push him along and get him to explain everything to me.
On to some physics....
First, it's amusing to note that Maxwell's equations are back in fashion! In the follow-
ing papers you will see how the duality symmetry of Maxwell's equations (the symmetry
between electric and magnetic elds) plays a new role in modern work on
4
-dimensional
gauge theory. Also, there is some good stuff in Thompson's review article about the
SeibergŒWitten theory, which is basically just a
U(1)
gauge theory like Maxwell's equa-
tions... but with some important extra twists!
2)
 Erik Verlinde, fiGlobal aspects of electric-magnetic dualityfl,
Nucl. Phys. B
455
(1995), 211Œ225. Also available as
hep-th/9506011
.
George Thompson, fiNew results in topological eld theory and abelian gauge the-
oryfl, available as
hep-th/9511038
.
Next, it's nice to see that work on the loop representation of quantum gravity contin-
ues apace:
3)
 Thomas Thiemann, fiAn account of transforms on
A
=
G
fl,
Acta Cosmologica
21
(1996),
145Œ167. Also available as
gr-qc/9511049
.
Thomas Thiemann, fiReality conditions inducing transforms for quantum gauge
eld theory and quantum gravityfl,
Class. Quant. Grav.
13
(1996) 1383-1404. Also
available as
gr-qc/9511057
.
Abhay Ashtekar, fiA generalized Wick transform for gravityfl,
Phys. Rev. D
53
(1996)
2865-2869. Also available as
gr-qc/9511083
.
Renate Loll, fiMaking quantum gravity calculablefl,
Acta Cosmologica
21
(1995),
131Œ144. Also available as
gr-qc/9511080
.
Rodolfo Gambini and Jorge Pullin, fiA rigorous solution of the quantum Einstein
equationsfl,
Phys. Rev. D
54
(1996), 5935Œ5938. Also available as
gr-qc/9511042
.
113
 WEEK 71 DECEMBER 3, 1995
The rst three papers here discuss some new work tackling the fireality conditionsfl
and fiHamiltonian constraintfl, two of the toughest issues in the loop representation of
quantum gravity. First, the Hamiltonian constraint is another name for the WheelerŒ
DeWitt equation
H  
= 0
that every physical state of quantum gravity must satisfy (see
 fiWeek 11fl
 for why). The
fireality conditionsfl have to do with the fact that this constraint looks different depend-
ing on whether we are working with Riemannian or Lorentzian quantum gravity. The
constraint is simpler when we work with Riemannian quantum gravity. Classically, in
Riemannian
gravity the metric on spacetime looks like
dt
2
+
dx
2
+
dy
2
+
dz
2
at any point, if we use suitable local coordinates. In this Riemannian world, time is no
different from space! In the real world, the world of
Lorentzian
gravity, the metric looks
like

dt
2
+
dx
2
+
dy
2
+
dz
2
at any point, in suitable coordinates. Folks often call the Riemannian world the world
of fiimaginary timefl, since in some vague sense we can get from the Lorentzian world to
the Riemannian world by making the transformation
t
7!
it;
called a fiWick transformfl. It looks simple the way I have just written it, in local coordi-
nates. But a priori it's far from clear that this Wick transform makes any sense globally.
Apparently, however, there is something we can do along these lines, which transforms
the Hamiltonian for Lorentzian quantum gravity to the better-understood one of Rie-
mannian quantum gravity! Alas, I have been too distracted by
n
-categories to keep up
with the latest work on this, but I'll catch up in a bit. Maybe over Christmas I can relax
a bit, lounge in front of a nice warm re, and read these papers.
The goal of all these machinations, of course, is to nd some equations that make
mathematical sense, have a good right to be called a fiquantized version of Einstein's
equationfl, and let one compute answers to some physics problems. We don't expect that
quantum gravity is enough to describe what's really going on in interesting problems...
there are lots of other forces and particles out there. Indeed, string theory is founded on
the premise that quantum gravity is completely inseparable from the quantum theories
of everything else. But here we are taking a different tack, treating quantum gravity
by itself in as simple a way as possible, expecting that the predictions of theory will be
qualitatively
of great interest even if they are quantitatively inaccurate.
As described in earlier Finds (
fiWeek 55fl
,
 fiWeek 68fl
), Loll has been working to make
quantum gravity ficalculablefl, by working on a discretized version of the theory called
lattice quantum gravity. If one does it carefully, it's not too bad to treat space as a lattice
in the loop representation of quantum gravity, because even in the continuum the theory
is discrete in a certain sense, since the states are described by fispin networksfl, certain
graphs embedded in space. (See
 fiWeek 43fl
 for more on these.) Her latest paper is an
introduction to some of these issues.
114
 WEEK 71 DECEMBER 3, 1995
In a somewhat different vein, Gambini and Pullin have been working on relating the
loop representation to knot theory. One of their most intriguing results is that the second
coefcient of the AlexanderŒConway knot polynomial is a solution of the Hamiltonian
constraint. Here they argue for this result using a lattice regularization of the theory.
Now let me turn to a variety of other matters...
4)
 Matt Greenwood and Xiao-Song Lin, fiOn Vassiliev knot invariants induced from
nite typefl, available as
q-alg/9506001
.
Lev Rozansky, fiOn nite type invariants of links and rational homology spheres
derived from the Jones polynomial and WittenŒReshetikhinŒTuraev invariantfl, in
Geometry and Physics
, CRC Press, Boca Raton, 2021, pp. 379Œ397. Also available
as
q-alg/9511025
.
Scott Axelrod, fiOverview and warmup example for perturbation theory with in-
stantonsfl, in
Geometry and Physics
, CRC Press, Boca Raton, 2021, pp. 321Œ338.
Also available as
hep-th/9511196
.
These papers all deal with perturbative ChernŒSimons theory and its spinoffs. The rst
two consider homology 3-spheres. In ChernŒSimons theory, this makes the moduli space
of at
SU(2)
connections trivial, thus eliminating some subtleties in the perturbation
theory. A homology 3-sphere is a 3-manifold whose homology is the same as that of the
3-sphere... the rst one was discovered by Poincar
´
e when he was studying his conjecture
that every 3-manifold with the homology of a 3-sphere is a 3-sphere. It turns out that
you can get a counterexample if you just take an ordinary 3-sphere, cut out a solid torus
embedded in the shape of a trefoil knot, and stick it back in with the meridian and
longitude (the short way around, and the long way around) switched Š making sure
they wind up pointing in the correct directions. This is called fidoing Dehn surgery on
the trefoilfl. It gives something with the homology of a 3-sphere that's not a 3-sphere.
So Poincar
´
e had to revise his conjecture to say that every 3-manifold
homotopic
to a 3-
sphere is (homeomorphic to) a 3-sphere. This improved fiPoincar
´
e conjecturefl remains
unsolved... its analog is known to be true in every dimension other than 3! Since every
possible counterexample to the Poincar
´
e conjecture is a homology 3-sphere, it makes
some sense to ponder these manifolds carefully.
Now, just as perturbative ChernŒSimons theory gives certain special invariants of
links, said to be of finite typefl, the same is true for homology 3-spheres. When we say a
link invariants is of nite type, all we mean is that it satises a simple property described
in
 fiWeek 3fl
. There is a similar but subtler denition for an invariant of homology 3-
spheres to be of nite type; they need to transform in a nice way under Dehn surgery.
(See
 fiWeek 60fl
 for more references.)
The second paper concentrates precisely on those subtleties due to the moduli space
of at connections, developing perturbation theory in the presence of fiinstantonsfl (here,
nontrivial at connections).
5)
 Alan Carey, Jouko Mickelsson, and Michael Murray, fiIndex theory, gerbes, and
Hamiltonian quantizationfl, available as
hep-th/9511151
.
Alan Carey, M. K. Murray and B. L. Wang, fiHigher bundle gerbes and cohomology
classes in gauge theoriesfl, available as
hep-th/9511169
115
 WEEK 71 DECEMBER 3, 1995
Higher-dimensional algebra is sneaking into physics in yet another way: gerbes!
What's a gerbe? Roughly speaking, it's a sheaf of groupoids, but there are some other
ways of thinking of them that come in handy in physics. See
 fiWeek 25fl
 for a review of
Brylinski's excellent book on gerbes, and also:
6)
 Jean-Luc Brylinski, fiHolomorphic gerbes and the Beilinson regulatorfl,
Ast
´
erisque
226
(1994), 145Œ174. Also available at
http://www.numdam.org/item/AST_1994_
_226__145_0/
Jean-Luc Brylinski, fiThe geometry of degree-four characteristic classes and of line
bundles on loop spaces Ifl, Duke Math. Jour. 75 (1994), 603Œ638.
Jean-Luc Brylinski and D. A. McLaughlin, fi

Cech cocycles for characteristic classesfl,
Commun. Math. Phys.
178
(1996), 225Œ236.
7)
 Joe Polchinski, fiRecent results in string dualityfl,
Prog. Theor. Phys. Suppl.
123
(1996), 9Œ18. Also available as
hep-th/9511157
.
This should help folks keep up with the ongoing burst of work on dualities relating
supercially different string theories.
8)
 Leonard Susskind and John Uglum, fiString physics and black holesfl,
Nucl. Phys.
Proc. Suppl.
45
(1996), 115Œ134. Also available as
hep-th/9511227
.
Among other things, this review discusses the fiholographic hypothesisfl mentioned in
fiWeek 57fl
:
9)
 Boguslaw Broda, fiA gauge-eld approach to 3- and 4-manifold invariantsfl, avail-
able as
q-alg/9511010
.
This summarizes the ReshetikhinŒTuraev construction of 3d topological quantum eld
theories from quantum groups, and Broda's own closely related approach to 4d topolog-
ical quantum eld theories.
10)
 John Baez and Martin Neuchl, fiHigher-dimensional algebra I: braided monoidal
2
-categoriesfl,
Adv. Math.
121
(1996), 196Œ244. Also available as
q-alg/9511013
.
In this paper, we begin with a brief sketch of what is known and conjectured concerning
braided monoidal
2
-categories and their applications to 4d topological quantum eld
theories and 2-tangles (surfaces embedded in
4
-dimensional space). Then we give con-
cise denitions of semistrict monoidal
2
-categories and braided monoidal
2
-categories,
and show how these may be unpacked to give long explicit denitions similar to, but
not quite the same as, those given by Kapranov and Voevodsky. Finally, we describe how
to construct a semistrict braided monoidal
2
-category
Z
(
C
)
as the `center' of a semistrict
monoidal category
C
. This is analogous to the construction of a braided monoidal cat-
egory as the center, or `quantum double', of a monoidal category. The idea is to de-
velop algebra that will do for 4-dimensional topology what quantum groups and braided
monoidal categories did for 3d topology. As a corollary of the center construction, we
prove a strictication theorem for braided monoidal
2
-categories.
116
 WEEK 72 FEBRUARY 1, 1996
Week 72
February 1, 1996
It's been a while since I've written an issue of This Week's Finds... due to holiday distrac-
tions and a bunch of papers that need writing up. But tonight I just can't seem to get any
work done, so let me do a bit of catching up.
I'm no string theorist, but I still can't help hearing all the rumbling noises over in that
direction: rst about all the dualities relating seemingly different string theories, and
then about the mysterious fiM-theoryfl in 11 dimensions which seems to underlie all these
developments. Let me try to explain a bit of this stuff... in the hopes that I prompt some
string theorists to correct me and explain it better! I will simplify everything a lot to keep
people from getting scared of the math involved. But I may also make some mistakes, so
the experts should be kind to me and try to distinguish between the simplications and
the mistakes.
Recall that it's hard to get a consistent string theory Š one that's not plagued by
innite answers to interesting questions. But this difculty is generally regarded as a
good thing, because it drastically limits the number of different versions of string theory
one needs to think about. It's often said that there are only 5 consistent string theories:
the type I theory, the type IIA and IIB theory, and the two kinds of heterotic string
theory. I'm not sure exactly what this statement means, but certainly it's only meant to
cover supersymmetric string theories, which can handle fermions (like the electron and
neutrino) in addition to bosons (like the photon).
Type I strings are fiopen stringsfl Š not closed loops Š and they live in 10 dimen-
sional spacetime, meaning that you need the dimension to be 10 to make certain nasty
innities cancel out. Type II strings also live in 10 dimensions, but they are ficlosed
stringsfl. That means that they look like a circle, so there are vibrational modes that
march around clockwise and other modes that march arou nd counterclockwise, and
these are supposed to correspond to different particles that we see. We can think of
these vibrational modes as moving around the circle at the speed of light; they are called
fileft-moversfl and firight-moversfl. Now fermions which move at the speed of light are
able to be rather asymmetric and only spin one way (when viewed head-on). We say
they have a fichiralityfl or handedness. Ordinary neutrinos, for example, are left-handed.
This asymmetry of nature shocked everyone when rst discovered, but it appears to be a
fact of life, and it's certainly a fact of mathematics. In the type IIA string theory, the left-
moving and right-moving fermionic vibrational modes have opposite chiralities, while in
the IIB theory, they have the same chirality. When I last checked, the type IIA theory
seemed to t our universe a bit better than the IIB theory.
But lots of people say the heterotic theory matches our universe even better. The
name fiheteroticfl refers to the fact that this theory is supposed to have fihybrid vigorfl.
It's quite bizarre: the left-movers are purely bosonic Š no fermions Š and live in
26
-dimensional spacetime, the way non-supersymmetric string theories do. The right-
movers, on the other hand, are supersymmetric and live in
10
-dimensional spacetime. It
sounds not merely heterotic, but downright schizophrenic! But in fact, the
26
-dimensional
spacetime can also be thought of as being
10
-dimensional, with
16
extra ficurled-up di-
mensionsfl in the shape of a torus. This torus has two possible shapes:
R
16
modulo the
117
 WEEK 72 FEBRUARY 1, 1996
E
8

E
8
lattice or the
D

16
lattice. (For some of the wonders of
E
8
and other lattices, check
out
 fiWeek 64fl
 and
 fiWeek 65fl
. The
D

16
lattice is related to the
D
16
lattice described in
those Weeks, but not quite the same.)
Now there is still lots of room for toying with these theories depending on how you
ficompactifyfl: how you think of
10
-dimensional spacetime as 4-dimensional spacetime
plus 6 curled-up dimensions. That's because there are lots of
6
-dimensional manifolds
that will do the job (the so-called fiCalabi-Yaufl manifolds). Different choices give differ-
ent physics, and there is a lot of work to be done to pick the right one.
However, recently it's beginning to seem that all ve of the basic sorts of string theory
are beginning to look like different manifestations of the same theory in 11 dimensions...
some monstrous thing called M-theory! Let me quote the following paper:
1)
 Kelly Jay Davis, fiM-Theory and string-string dualityfl, available as
hep-th/9601102
.
The idea seems to be roughly that depending on how one compacties the 11th
dimension, one gets different
10
-dimensional theories from M-theory:
fiIn the past year much has happened in the eld of string theory. Old results
relating the two Type II string theories and the two Heterotic string theories have
been combined with newer results relating the Type II theory and the Heterotic
theory, as well as the Type I theory and the Heterotic theory, to obtain a single
fiString Theory.fl In addition, there has been much recent progress in interpreting
some, if not all, properties of String Theory in terms of an eleven-dimensional
M-Theory. In this paper we will perform a self-consistency check on the various
relations between M-Theory and String Theory. In particular, we will examine
the relation between String Theory and M-Theory by examining its consistency
with the string-string duality conjecture of six-dimensional String Theory. So, let
us now take a quick look at the relations between M-Theory and String Theory
some of which we will be employing in this article.
In Witten's paper he established that the strong coupling limit of Type IIA string
theory in ten dimensions is equivalent to eleven-dimensional supergravity on a
filargefl
S
1
. [Note:
S
1
just means the circle Š jb.] As the low energy limit of
M-theory is eleven-dimensional supergravity, this relation states that the strong
coupling limit of Type IIA string theory in ten-dimensions is equivalent to the
low -energy limit of M-Theory on a filargefl
S
1
. In the paper of Witten and Ho-
rava, they establish that the strong coupling limit of the ten-dimensional
E
8

E
8
Heterotic string theory is equivalent to M-Theory on a filargefl
S
1
=
Z
2
.
Recently, Witten, motivated by Dasgupta and Mukhi, examined M-Theory on
a
Z
2
orbifold of the ve-torus and established a relation between M-Theory on
this orbifold and Type IIB string theory on
K3
. [Note: most of these undened
terms refer to various spaces; for example, the ve-torus is the
5
-dimensional
version of a doughnut, while
K3
is a certain
4
-dimensional manifold Š jb.]
Also, Schwarz very recently looked at M-Theory and its relation to T-Duality.
As stated above, M-Theory on a filargefl
S
1
is equivalent to a strongly coupled
Type IIA string theory in ten-dimensions. Also, M-theory on a filargefl
S
1
=
Z
2
is equivalent to a strongly coupled
E
8

E
8
Heterotic string theory in ten di-
mensions. However, the string-string duality conjecture in six dimensions states
118
 WEEK 72 FEBRUARY 1, 1996
that the strongly coupled limit of a Heterotic string theory in six dimensions
on a four-torus is equivalent to a weakly coupled Type II string theory in six
dimensions on
K3
. Similarly, it states that the strongly coupled limit of a Type
II theory in six dimensions on
K3
is equivalent to a weakly coupled Heterotic
string theory in six-dimensions on a four-torus. Now, as a strongly coupled Type
IIA string theory in ten-dimensions is equivalent to the low energy limit of M-
Theory on a filargefl
S
1
, the low energy limit of M-Theory on
S
1

K3
should be
equivalent to a weakly coupled Heterotic string theory on a four-torus by way of
six-dimensional string-string duality. Similarly, as a strongly coupled
E
8

E
8
Heterotic string theory in ten-dimensions is equivalent to the low energy limit of
M-Theory on a filargefl
S
1
=
Z
2
, the low energy limit of M-Theory on
S
1
=
Z
2

T
4
should be equivalent to a weakly coupled Type II string theory on
K3
. The rst of
the above two consistency checks on the relation between M-Theory and String
Theory will be the subject of this article. However, we will comment on the
second consistency check in our conclusion.fl
So, as you can see, there is a veritable jungle of relationships out there. But you must
be wondering by now:
what's M-theory?
According to
2)
 Edward Witten, fiFive-branes and M-theory on an orbifoldfl, available as
hep-th/
9512219
.
the M stands for fimagicfl, fimysteryfl, or fimembranefl, according to taste. From a math-
ematical viewpoint a better term might be fimurkyfl, since apparently everything known
about M-theory is indirect and circumstantial, except for the classical limit, in which it
seems to act as a theory of
2
-branes and
5
-branes, where an fi
p
-branefl is a
p
-dimensional
analog of a membrane or surface.
Well, here I must leave off, for reasons of ignorance. I don't really understand the
evidence for the existence of the M-theory... I can only await the day when the murk
clears and it becomes possible to learn about this stuff a bit more easily. It has been
suggested that string theory is a bit of 21st-century mathematics that accidentally fell
into the 20th century. I think this is right, and that eventually much of this stuff will be
seen as much simpler than it seems now.
Now let me briey describe some papers I actually sort of understand.
3)
 Abhay Ashtekar, fiPolymer geometry at Planck scale and quantum Einstein equa-
tionsfl, available as
hep-th/9601054
.
Roumen Borissov, Seth Major and Lee Smolin, fiThe geometry of quantum spin
networksfl, available as
gr-qc/9512043
,
Bernd Br
¨
ugmann, fiOn the constraint algebra of quantum gravity in the loop repre-
sentationfl, available as
gr-qc/9512036
.
Kiyoshi Ezawa, fiNonperturbative solutions for canonical quantum gravity: an overviewfl,
available as
gr-qc/9601050
Kiyoshi Ezawa, fiA semiclassical interpretation of the topological solutions for canon-
ical quantum gravityfl, available as
gr-qc/9512017
.
Jorge Griego, fiExtended knots and the space of states of quantum gravityfl, avail-
able as
gr-qc/9601007
.
119
 WEEK 72 FEBRUARY 1, 1996
Seth Major and Lee Smolin, fiQuantum deformation of quantum gravityfl, available
as
gr-qc/9512020
.
Work on the loop representation of quantum gravity proceeds apace. The paper by
Ashtekar and the rst one by Ezawa review various recent developments and might be
good to look at if one is just getting interested in this subject. Smolin has been pushing
the idea of combining ideas about the quantum group
S U
q
(2)
with the loop representa-
tion, and his papers with Borissov and Major are about that. This seems rather interesting
but still a bit mysterious to me. I suspect that what it amounts to is thinking of loops as
excitations not of the AshtekarŒLewandowksi vacuum state but the ChernŒSimons state.
I'd love to see this claried, since these two states are two very important exact solutions
of quantum gravity, and the latter has the former as a limit as the cosmological constant
goes to zero. In the second paper listed, Ezawa gives semiclassical interpretations of
these and other exact solutions of quantum gravity.
4)
 Thomas Kerler, fiGenealogy of nonperturbative quantum-invariants of 3-Manifolds:
the surgical familyfl, available as
q-alg/9601021
.
Kerler brings a bit more order to the study of quantum invariants of 3-manifolds, in
particular, the ReshetikhinŒTuraev, Hennings-Kauffman-Radford, and Lyubashenko in-
variants. All of these are constructed using certain braided monoidal categories, like the
category of (nice) representations of a quantum group. He describes how Lyubashenko's
invariant specializes to the ReshetikhinŒTuraev invariant for semisimple categories and
to the Hennings-Kauffman-Radford invariant for Tannakian categories. People interested
in extended TQFTs and
2
-categories will nd his work especially interesting, because he
works with these invariants using these techniques. James Dolan and I have argued that
it's only this way that one will really understand these TQFTs (see
 fiWeek 49fl
).
In future editions of This Week's Finds I will say more about
n
-categories and topo-
logical quantum eld theory. I have a feeling that while I've discussed these a lot, I have
never really explained the basic ideas very well. As I gradually understand the basic ideas
better, they seem simpler and simpler to me, so I think I should try to explain them.
120
 WEEK 73 FEBRUARY 24, 1996
Week 73
February 24, 1996
In this and future issues of This Week's Finds, I'd like to talk a bit more about higher-
dimensional algebra, and how it should lead to many exciting developments in mathe-
matics and physics in the 21st century. I've talked quite a bit about this already, but I
hear from some people that the fibig picturefl remained rather obscure. The main reason,
I suppose, is that I was just barely beginning to see the big picture myself! As Louis
Crane noted, in this subject it often feels that we are unearthing the fossilized remains
of some enormous prehistoric beast, still unsure of its extent or how it all ts together.
Of course that's what makes it so exciting, but I'll try to make sense what we've found
so far, and where it may lead. In the Weeks to come, I'll start out describing some basic
stuff, and work my way up to some very new ideas.
However, before I get into that, I'd like to say a bit about something completely
different: biology.
1)
Biological Asymmetry and Handedness
, Ciba Foundation Symposium
162
, John Wi-
ley and Sons, 1991.
D. K. Kondepudi and D. K. Nelson, fiWeak neutral currents and the origins of molec-
ular chiralityfl,
Nature
314
, pp. 438Œ441.
It's always puzzled me how humans and other animals could be consistently asym-
metric. A 50-50 mix of two mirror-image forms could easily be explained by fisponta-
neously broken symmetryfl, but in fact there are many instances of populations with a
uniform handedness. Many examples appear in Weyl's book fiSymmetryfl (see
 fiWeek
63fl
). To take an example close to home, the human brain appears to be lateralized in
a fairly consistent manner; for example, most people have the speech functions concen-
trated in the left hemisphere of their cerebrum Š even most, though not all, left-handers.
One might nd this unsurprising: it just means that the asymmetry is encoded in the
genes. But think about it: how are the genes supposed to tell the embryo to develop in
an asymmetric way? How do they explain the difference between right and left? That's
what intrigues me.
Of course, genes code for proteins, and most proteins are themselves asymmetric.
Presumably the answer lurks somewhere around here. Indeed, even the amino acids of
which the proteins are composed are asymmetric, as are many sugars and for that matter,
the DNA itself, which is composed of two spirals, each of which has an intrinsic direc-
tionality and hence a handedness. The handedness of many of these basic biomolecules
is uniform for all life on the globe, as far as I know.
In the conference proceedings on biological asymmetry, there is an interesting article
on the development of asymmetry in
C. elegans
. Ever since the 1960s, this little nema-
tode has been a favorite among biologists because of its simplicity, and because of the
advantages understanding one organism thoroughly rather than many organisms in a
sketchy way. I'm sure most of you know about the fondness geneticists have for the fruit
y, but Caenorhabditis elegans is a far simpler critter: it only has 959 cells, all of which
have been individually named and studied! There are over 1000 people studying it by
now, there is a journal devoted to it Š The Worm Breeder's Gazette Š and it has its own
121
 WEEK 73 FEBRUARY 24, 1996
world-wide web server. Moreover, folks are busily sequencing not only the complete
human genome but also all 100 million bases of the DNA of
C. elegans
.
But I digress! The point here is that
C. elegans
is asymmetric, and exhibits a consistent
handedness. And the cool thing is that in the conference proceedings, Wood and Kevshan
report on experiments where they articially changed the handedness of
C. elegans
em-
bryos when they consisted of only 6 cells! The embryos look symmetric when they have
4 cells; by the time they have 8 cells the asymmetry is marked. By moving some cells
around at the 6-cell stage, Wood and Kevshan were able to create fully functional
C.
elegans
having opposite the usual handedness.
The question of exactly how the embryo's asymmetry originates from some asymme-
try at the molecular still seems shrouded in mystery. And there is another puzzle: how
did the biomolecules choose their handedness in the rst place? Here spontaneous sym-
metry breaking Š an essentially random choice later amplied by selection Š seems a
natural hypothesis. But physicists should be interested to note that another alternative
has been seriously proposed. Weak interactions violate parity and thus endow the laws
of nature with an intrinsic handedness. This means there is a slight difference in energies
between any biomolecule and its enantiomer, or mirror-image version. According to S. F.
Mason's article in the conference proceedings, this difference indeed favors the observed
forms of amino acids and sugars Š the left-handed or fiLfl amino acids and the right-
handed or fiDfl sugars. But the difference is is incredibly puny Š typically it amounts to
10

14
joules per mole! How could such a small difference matter? Well, Kondepudi and
Nelson have done calculations suggesting that in certain situations where there is both
autocatalysis of both L and D forms of these molecules, and also competition between
them, random uctuations can be averaged out, while small energy level differences can
make a big difference.
That would be rather satisfying to me: knowing that my heart is where it is for the
same reason that neutrinos are left-handed. But in fact this theory is very controver-
sial. . . . I mention it only because of its charm.
If we think of the universe as passing through the course of history from simplicity
to complexity, from neutrinos to nematodes to humans, it's natural to wonder what's
at the bottom, where things get very simple, where physics blurs into pure logic. . . . far
from the fispires of formfl. Ironically, even the simplest things may be hard to understand,
because they are so abstract. But let's give it a try Š here comes the Tale of
n
-Categories.
Let's begin with the world of sets. In a certain sense, there is nothing much to a set
except its cardinality, the number of elements it has. Of course, set theorists work hard
to build up the universe of sets from the empty set, each set being a set of sets, with its
own distinctive personality:
fg
;
ffgg
;
fffggg
;
ffg
;
ffggg
;
ffg
;
fffgggg
;
ffg
;
ffgg
;
ffg
;
ffgggg
and the like. But for many purposes, a one-to-one and onto function between two sets
allows us to treat them as the same. So if necessary, we could actually get by with just
one set of each cardinality. For example
fg
;
ffgg
;
ffg
;
ffggg
;
ffg
;
ffgg
;
ffg
;
ffgggg
and so on. For short, people like to call these
0
;
1
;
2
;
3
122
 WEEK 73 FEBRUARY 24, 1996
and so on. We could wonder what comes after all these nite cardinals, and what comes
after that, and so on, but let's not. Instead, let's ponder what we've done so far. We
started with the universe of sets Š not exactly the set of all sets, but pretty close Š but
very soon we started playing with functions between sets. This is what allowed us to
speak of two sets with the same cardinality as being isomorphic.
In short, we are really working with the
category
of sets. A category is something just
as abstract as a set, but a bit more structured. It's not a mere collection of objects; there
are also morphisms between objects, in this case the functions between sets.
Some of you might not know the precise denition of a category; let me state it
just for completeness. A category consists of a collection of fiobjectsfl and a collection
of fimorphismsfl. Every morphism
f
has a fisourcefl object and a fitargetfl object. If the
source of
f
is
X
and its target is
Y
, we write
f
:
X
!
Y
. In addition, we have:
1)
 Given a morphism
f
:
X
!
Y
and a morphism
g
:
Y
!
Z
, there is a morphism
f g
:
X
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
X
there is a morphism
1
X
:
X
!
X
, called the fiidentityfl of
X
. For
any
f
:
X
!
Y
we have
1
X
f
=
f
1
Y
=
f
.
That's it.
(Note that we are writing the composite of
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
Z
as
f g
, which is
backwards from the usual order. This will make life easier in the long run, though, since
f g
will mean first do
f
, then
g
fl.)
Now, there are lots of things one can do with sets, which lead to all sorts of interesting
examples of categories, but in a sense the primordial category is
Set
, the category of sets
and functions. (One might try to make this precise, by trying to prove that every category
is a subcategory of
Set
, or something like that. Actually the right way to say how
Set
is
primordial is called the fiYoneda lemmafl. But to understand this lemma, one needs to
understand categories a little bit.)
When we get to thinking about categories a lot, it's natural to think about the ficate-
gory of all categoriesfl. Now just as it's a bit bad to speak of the set of all sets, it's bad to
speak of the category of all categories. This is true, not only because Russell's paradox
tends to ruin attempts at a consistent theory of the fithing of all thingsfl, but because, just
as what really counts is the
category
of all sets, what really counts is the
2
-category
of all
categories.
To understand this, note that there is a very sensible notion of a morphism between
categories. It's called a fifunctorfl, and a functor
F
:
C ! D
from a category
C
to a
category
D
is just something that assigns to each object
x
of
C
an object
F
(
x
)
of
D
, and
to each morphism
f
of
C
a morphism
F
(
f
)
of
D
, in such a way that fiall structure in sight
is preservedfl. More precisely, we want:
1)
 If
f
:
x
!
y
, then
F
(
f
) :
F
(
x
)
!
F
(
y
)
.
2)
 If
f g
=
h
, then
F
(
f
)
F
(
g
) =
F
(
h
)
.
3)
 If
1
x
is the identity morphism of
x
, then
F
(1
x
)
is the identity morphism of
F
(
x
)
.
123
 WEEK 73 FEBRUARY 24, 1996
It's good to think of a category as a bunch of dots Š objects Š and arrows going
between them Š morphisms. I would draw one for you if I could here. Category theorists
love drawing these pictures. In these terms, we can think of the functor
F
:
C ! D
as
putting a little picture of the category
C
inside the category
D
. Each dot of
C
gets drawn
as a particular dot in
D
, and each arrow in
C
gets drawn as a particular arrow in
D
. (Two
dots or arrows in
C
can get drawn as the same dot or arrow in
D
, though.)
In addition, however, there is a very sensible notion of a fi2-morphismfl, that is, a
morphism between morphisms between categories! It's called a finatural transforma-
tionfl. The idea is this. Suppose we have two functors
F
:
C ! D
and
G
:
C ! D
. We can
think of these as giving two pictures of
C
inside
D
. So for example, if we have any object
x
in
C
, we get two objects in
D
,
F
(
x
)
and
G
(
x
)
. A finatural transformationfl is then a
gadget that draws an arrow from each dot like
F
(
x
)
to the dot like
G
(
x
)
. In other words,
for each
x
, the natural transformation
T
gives a morphism
T
x
:
F
(
x
)
!
G
(
x
)
. But we
want a kind of compatibility to occur: if we have a morphism
f
:
x
!
y
in
C
, we want
F
(
x
)
F
(
y
)
G
(
x
)
G
(
y
)
F
(
f
)
T
x
T
y
G
(
f
)
to commute; in other words, we want
T
x
G
(
f
) =
F
(
f
)
T
y
.
This must seem very boring to the people who understand it and very mystifying
to those who don't. I'll need to explain it more later. For now, let me just say a bit
about what's going on. Sets are fizero-dimensionalfl in that they only consist of objects,
or fidotsfl. There is no way to figo from one dot to anotherfl within a set. Nonetheless,
we can go from one set to another using a function. So the category of all sets is fione-
dimensionalfl: it has both objects or fidotsfl and morphisms or fiarrows between dotsfl. In
general, categories are fione-dimensionalfl in this sense. But this in turn makes the col-
lection of all categories into a fitwo-dimensionalfl structure, a
2
-category having objects,
morphisms between objects, and
2
-morphisms between morphisms.
This process never stops. The collection of all
n
-categories is an
(
n
+ 1)
-category, a
thing with objects, morphisms,
2
-morphisms, and so on all the way up to
n
-morphisms.
To study sets carefully we need categories, to study categories well we need
2
-categories,
to study
2
-categories well we need
3
-categories, and so on... so fihigher- dimensional al-
gebrafl, as this subject is called, is automatically generated in a recursive process starting
with a careful study of set theory.
If you want to show off, you can call the
2
-category of all categories
Cat
, and more
generally, you can call the
(
n
+ 1)
-category of all
n
-categories
n
Cat
.
n
Cat
is the primordial
example of an
(
n
+ 1)
-category!
Now, just as you might wonder what comes after
0
;
1
;
2
;
3
; : : :
, you might wonder
what comes after all these
n
-categories. The answer is fi
!
-categoriesfl.
What comes after these? Well, let us leave that for another time. I'd rather conclude
by mentioning the part that's the most fascinating to me as a mathematical physicist.
Namely, the various dimensions of category turn out to correspond in a very beautiful
Š but still incompletely understood Š way to the various dimensions of spacetime.
In other words, the study of physics in imaginary
2
-dimensional spacetimes uses lots
124
 WEEK 73 FEBRUARY 24, 1996
of
2
-categories, the study of physics in a 3d spacetimes uses 3-categories, the study of
physics in 4d spacetimes appears to use 4-categories, and so on. It's very surprising
at rst that something so simple and abstract as the process of starting with sets and
recursively being led to study the
(
n
+ 1)
-category of all
n
-categories could be related
to the dimensionality of spacetime. In particular, what could possibly be special about 4
dimensions?
Well, it turns out that there
are
some special things about 4 dimensions. But more on
that later. To continue reading the fiTale of
n
-Categoriesfl, see
 fiWeek 74fl
.
Addendum
: Long after writing the above, I just saw an interesting article on chirality
in biology:
2)
 N. Hirokawa, Y. Tanaka, Y. Okada and S. Takeda, fiNodal ow and the generation
of left-right asymmetryfl,
Cell
125
1 (2006), 33Œ45.
It reports on detailed studies of how left-right asymmetry rst shows in the development
of animal embryos. It turns out this asymmetry is linked to certain genes with names like
Lefty -1
,
Lefty -2
,
Nodal
and
Pitx2
. About half of the people with a genetic disorder called
Kartagener's Syndrome have their organs in the reversed orientation. These people also
have immotile sperm and defective cilia in their airway. This suggests that the genes
controlling left-right asymmetry also affect the development of cilia! And the link has
recently been understood....
The rst visible sign of left-right asymm etry in mammal embryos is the formation of a
structure called the fiventral nodefl after the front-back (dorsal-ventral) and top-bottom
(anterior-posterior) symmetries have been broken. This node is a small bump on the
front of the embryo.
It has recently been found that cilia on this bump wiggle in a way that makes the
uid the embryo is oating in ow towards the
left
. It seems to be this leftward ow that
generates many of the more fancy left-right asymmetries that come later.
How do these cilia generate a leftward ow? It seems they spin around
clockwise
,
and are tilted in such a way that they make a leftward swing when they are near the
surface of the embryo, and a rightward swing when they are far away. This manages to
do the job... the article discusses the hydrodynamics involved.
I guess now the question becomes: why do these cilia spin clockwise?
125
 WEEK 74 MARCH 5, 1996
Week 74
March 5, 1996
Before continuing my story about higher-dimensional algebra, let me say a bit about
gravity. Probably far fewer people study general relativity than quantum mechanics,
which is partially because quantum mechanics is more practical, but also because general
relativity is mathematically more sophisticated. This is a pity, because general relativity
is so beautiful!
Recently, I have been spending time on
sci.physics
leading an informal (nay, chaotic)
figeneral relativity tutorialfl. The goal is to explain the subject with a minimum of compli-
cated equations, while still getting to the mathematical heart of the subject. For example,
what does Einstein's equation REALLY MEAN? It's been a lot of fun and I've learned a
lot! Now I've gathered up some of the posts and put them on a web site:
1)
 John Baez
et al
, fiGeneral relativity tutorialfl,
gr/gr.html
I hope to improve this as time goes by, but it should already be fun to look at.
Let me also list a couple new papers on the loop representation of quantum gravity,
dealing with ways to make volume and area into observables in quantum gravity:
2)
 Abhay Ashtekar and Jerzy Lewandowski, fiQuantum theory of geometry I: area op-
eratorsfl, to appear in Classical and Quantum Gravity, available as
gr-qc/9602046
.
Jerzy Lewandowski, fiVolume and quantizationsfl, available as
gr-qc/9602035
.
Roberto De Pietri and Carlo Rovelli, fiGeometry eigenvalues and scalar product
from recoupling theory in loop quantum gravityfl, available as
gr-qc/9602023
.
I won't say anything about these now, but see
 fiWeek 55fl
 for some information on
area operators.
Okay, where were we? We had started messing around with sets, and we noted
that sets and functions between sets form a category, called Set. Then we started mess-
ing around with categories, and we noted that not only are there fifunctorsfl between
categories, there are things that ply their trade between functors, called finatural trans-
formationsfl. I then said that categories, functors, and natural transformations form a
2
-category. I didn't really say what a
2
-category is, except to say that it has objects, mor-
phisms between objects, and
2
-morphisms between morphisms. Finally, I said that this
pattern continues:
n
Cat
forms an
(
n
+ 1)
-category.
By the way, I said last time that
Set
was fithe primordial categoryfl. Keith Ramsay
reminded me by email that this can be misleading. There are other categories that act
a whole lot like
Set
and can serve equally well as fithe primordial categoryfl. These are
called topoi. Poetically speaking, we can think of these as alternate universes in which
to do mathematics. For more on topoi, see
 fiWeek 68fl
. All I meant by saying that
Set
was
fithe primordial categoryfl is that, if we start from
Set
and various categories of structures
built using sets Š groups, rings, vector spaces, topological spaces, manifolds, and so on
126
 WEEK 74 MARCH 5, 1996
Š we can then abstract the notion of ficategoryfl, and thus obtain
Cat
. In the same sense,
Cat
is the primordial
2
-category, and so on.
I mention this because it is part of a very important broad pattern in higher-dimensional
algebra. For example, we will see that the complex numbers are the primordial Hilbert
space, and that the category of Hilbert spaces is the primordial fi2-Hilbert spacefl, and
that the
2
-category of 2-Hilbert spaces is the primordial fi3-Hilbert spacefl, and so on.
This leads to a quantum-theoretic analog of the hierarchy of
n
-categories, which plays
an important role in mathematical physics. But I'm getting ahead of myself!
Let's start by considering a few examples of categories. I want to pick some examples
that will lead us naturally to the main themes of higher-dimensional algebra. Beware:
it will take us a while to get rolling. For a while Š maybe a few issues of This Week's
Finds Š everything may seem somewhat dry, pointless and abstract, except for those
of you who are already clued in. It has the avor of fifoundations of mathematics,fl but
eventually we'll see these new foundations reveal topology, representation theory, logic,
and quantum theory to be much more tightly interknit than we might have thought. So
hang in there.
For starters, let's keep the idea of fisymmetryfl in mind. The typical way to think about
symmetry is with the concept of a figroupfl. But to get a concept of symmetry that's really
up to the demands put on it by modern mathematics and physics, we need Š at the very
least Š to work with a
category
of symmetries, rather than a group of symmetries.
To see this, rst ask: what is a category with one object? It is a fimonoidfl. The
usual
denition of a monoid is this: a set
M
with an associative binary product and a unit
element
1
such that
a
1 = 1
a
=
a
for all
a
in
M
. Monoids abound in mathematics; they
are in a sense the most primitive interesting algebraic structures.
To check that a category with one object is fiessentially just a monoidfl, note that if our
category
C
has one object
x
, the set
Hom(
x; x
)
of all morphisms from
x
to
x
is indeed a
set with an associative binary product, namely composition, and a unit element, namely
1
x
. (Actually, in an arbitrary category
Hom(
x; y
)
could be a class rather than a set. But
let's not worry about such nuances.) Conversely, if you hand me a monoid
M
in the
traditional sense, I can easily cook up a category with one object
x
and
Hom(
x; x
) =
M
.
How about categories in which every morphism is invertible? We say a morphism
f
:
x
!
y
in a category has inverse
g
:
y
!
x
if
f g
= 1
x
and
g f
= 1
y
. Well, a category in
which every morphism is invertible is called a figroupoidfl.
Finally, a group is a category with one object in which every morphism is invertible.
It's both a monoid and a groupoid!
When we use groups in physics to describe symmetry, we think of each element
g
of
the group
G
as a fiprocessfl. The element
1
corresponds to the fiprocess of doing nothing
at allfl. We can compose processes
g
and
h
Š do
h
and then
g
Š and get the product
g h
.
Crucially, every process
g
can be fiundonefl using its inverse
g

1
.
We tend to think of this ability to fiundofl any process as a key aspect of symmetry. I.e.,
if we rotate a beer bottle, we can rotate it back so it was just as it was before. We don't
tend to think of
smashing
the beer bottle as a symmetry, because it can't be undone. But
while processes that can be undone are especially interesting, it's also nice to consider
other ones... so for a full understanding of symmetry we should really study monoids as
well as groups.
But we also should be interested in fipartially denedfl processes, processes that can
be done only if the initial conditions are right. This is where categories come in! Suppose
127
 WEEK 74 MARCH 5, 1996
that we have a bunch of boxes, and a bunch of processes we can do to a bottle in one
box to turn it into a bottle in another box: for example, fitake the bottle out of box
x
,
rotate it 90 degrees clockwise, and put it in box
y
fl. We can then think of the boxes as
objects and the processes as morphisms: a process that turns a bottle in box
x
to a bottle
in box
y
is a morphism
f
:
x
!
y
. We can only do a morphism
f
:
x
!
y
to a bottle in
box
x
, not to a bottle in any other box, so
f
is a fipartially denedfl process. This implies
we can only compose
f
:
x
!
y
and
g
:
u
!
v
to get
f g
:
x
!
v
if
y
=
u
.
So: a monoid is like a group, but the fisymmetriesfl no longer need be invertible; a
category is like a monoid, but the fisymmetriesfl no longer need to be composable!
Note for physicists: the operation of fievolving initial data from one spacelike slice
to anotherfl is a good example of a fipartially denedfl process: it only applies to initial
data on that particular spacelike slice. So dynamics in special relativity is most naturally
described using groupoids. Only after pretending that all the spacelike slices are the
same can we pretend we are using a group. It is very common to pretend that groupoids
are groups, since groups are more familiar, but often insight is lost in the process. Also,
one can only pretend a groupoid is a group if all its objects are isomorphic. Groupoids
really are more general.
Physicists wanting to learn more about groupoids might try:
3)
 Alan Weinstein, fiGroupoids: unifying internal and external symmetryfl, available
at
http://www.ams.org/notices/199607/weinstein.pdf
So: in contrast to a set, which consists of a static collection of fithingsfl, a category
consists not only of objects or fithingsfl but also morphisms which can viewed as fipro-
cessesfl transforming one thing into another. Similarly, in a
2
-category, the
2
-morphisms
can be regarded as fiprocesses between processesfl, and so on. The eventual goal of
basing mathematics upon
!
-categories is thus to allow us the freedom to think of any
process as the sort of thing higher-level processes can go between. By the way, it should
also be very interesting to consider fi
Z
-categoriesfl (where
Z
denotes the integers), hav-
ing
j
-morphisms not only for
j
= 0
;
1
;
2
; : : :
but also for negative
j
. Then we may also
think of any thing as a kind of process.
How do the above remarks about groups, monoids, groupoids and categories gener-
alize to the
n
-categorical context? Well, all we did was start with the notion of category
and consider two sorts of requirement: that the category have just one object, or that all
morphisms be invertible.
A category with just one object Š a monoid Š could also be seen as a set with extra
algebraic structure, namely a product and unit. Suppose we look at an
n
-category with
just one object? Well, it's very similar: then we get a special sort of
(
n

2)
-categoryfl, and so on.
This game must seem very abstract and mysterious when one rst hears of it. But it turns
out to yield a remarkable set of concepts, some already very familiar in mathematics,
and it turns out to greatly deepen our notion of ficommutativityfl. For now, let me simply
display a chart of fi
k
-tuply monoidal
n
-categoriesfl for certain low values of
n
and
k
:
128
 WEEK 74 MARCH 5, 1996
Table 1:
k
-tuply monoidal
n
-categories
n
= 0
n
= 1
n
= 2
k
= 0
sets categories
2
-categories
k
= 1
monoids monoidal
categories
monoidal
2
-categories
k
= 2
commutative
monoids
braided monoidal
categories
braided monoidal
2
-categories
k
= 3
fl fl symmetric
monoidal
categories
weakly involutory
monoidal
2
-categories
k
= 4
fl fl fl fl strongly
involutory
monoidal
2
-categories
k
= 5
fl fl fl fl fl fl
The quotes indicate that each column fistabilizesfl past a certain point. If you can't
wait to read more about this, you might try
 fiWeek 49fl
 for more, but I will explain it all
in more detail in future issues.
What if we take an
n
-category and demand that all
j
-morphisms (
j >
0
) be in-
vertible? Well, then we get something we could call an fi
n
-groupoidfl. However, there
are some important subtle issues about the precise sense in which we might want all
j
-morphisms to be invertible. I will have to explain that, too.
Let me conclude, though, by mentioning something the experts should enjoy. If we
dene
n
-groupoids correctly, and then gure out how to dene
!
-groupoids correctly, the
homotopy category of
!
-groupoids turns out to be equivalent to the homotopy category
of topological spaces. The latter category is something algebraic topologists have spent
decades studying. This is one of the main ways
n
-categories are important in topology.
Using this correspondence between
n
-groupoid theory and homotopy theory, the fistabi-
lizationfl property described above is then related to a subject called fistable homotopy
theoryfl, and fi
Z
-groupoidsfl are a way of talking about fispectrafl Š another important
tool in homotopy theory.
The above paragraph is overly erudite and obscure, so let me explain the gist: there is
a way to think of a topological space as giving us an
!
-groupoid, and the
!
-groupoid then
captures all the information about its topology that homotopy theorists nd interesting.
(I will explain in more detail how this works later.) If this is
all
n
-category theory did, it
would simply be an interesting language for doing topology. But as we shall see, it does a
lot more. One reason is that, not only can we use
n
-categories to think about spaces, we
can also use them to think about symmetries, as described above. Of course, physicists
are very interested in space and also symmetry. So from the viewpoint of a mathematical
129
 WEEK 74 MARCH 5, 1996
physicist, one interesting thing about
n
-categories is that they
unify
the study of space
(or spacetime) with the study of symmetry.
I will continue along these lines next time and try to ll in some of the big gaping
holes.
To continue reading the fiTale of
n
-Categoriesfl, see
 fiWeek 75fl
.
130
 WEEK 75 MARCH 6, 1996
Week 75
March 6, 1996
If you've been following my recent introduction to
n
-categories, you'll note that I haven't
actually given the denition of
n
-categories! I've only dened categories, and
hinted
at
the denition of
2
-categories by giving an example, namely
Cat
. This is the
2
-category
whose objects are categories, whose morphisms are functors, and whose
2
-morphisms
are natural transformations.
The denition of
n
-categories Š or maybe I should say the problem of dening
n
-
categories Š is actually surprisingly subtle. Since I want to proceed at a gentle pace here,
I think I should rst get everyone used to the
2
-category
Cat
, then dene
2
-categories in
general, then play around with those a bit, and then move on to
n
-categories for higher
n
.
So recall what the objects, morphisms and
2
-morphisms in
Cat
are: they are cate-
gories, functors and natural transformations. A functor
F
:
C ! D
assigns to each object
x
of
C
an object
F
(
x
)
of
D
, and to each morphism
f
of
C
a morphism
F
(
f
)
of
D
, and has
1.
 If
f
:
x
!
y
, then
F
(
f
) :
F
(
x
)
!
F
(
y
)
.
2.
 If
f g
=
h
, then
F
(
f
)
F
(
g
) =
F
(
h
)
.
3.
 If
1
x
is the identity morphism of
x
, then
F
(1
x
)
is the identity morphism of
F
(
x
)
.
Given two functors
F
:
C ! D
and
G
:
C ! D
, a finatural transformationfl
T
:
F
)
G
assigns to each object
x
of
C
a morphism
T
x
:
F
(
x
)
!
G
(
x
)
, such that for any morphism
f
:
x
!
y
in
C
, the diagram
F
(
x
)
F
(
y
)
G
(
x
)
G
(
y
)
F
(
f
)
T
x
T
y
G
(
f
)
commutes.
Let me give a nice example. Let
Top
be the category with topological spaces and con-
tinuous functions between them as morphisms. Let
Gp d
be the category with groupoids
as objects and functors between them as morphisms. (Remember from
 fiWeek 74fl
 that a
groupoid is a category with all morphisms invertible.) Then there is a functor

1
:
Top
!
Gp d
called the fifundamental groupoidfl functor, which plays a very basic role in algebraic
topology.
Here's how we get from any space
X
its fifundamental groupoidfl

1
(
X
)
. (If per-
chance you already know about the fifundamental groupfl, fear not, what we're doing
now is very similar.) To say what the groupoid

1
(
X
)
is, we need to say what its objects
and morphisms are. The objects in

1
(
X
)
are just the
points
of
X
and the morphisms
are just certain equivalence classes of
paths
in
X
. More precisely, a morphism
f
:
x
!
y
in

1
(
X
)
is just an equivalence class of continuous paths from
x
to
y
, where two paths
131
 WEEK 75 MARCH 6, 1996
from
x
to
y
are decreed equivalent if one can be continuously deformed to the other
while not moving the endpoints. (If this equivalence relation holds we say the two paths
are fihomotopicfl, and we call the equivalence classes fihomotopy classes of paths.fl)
This is a truly wonderful thing! Recall the idea behind categories. A morphism
f
:
x
!
y
is supposed to be some abstract sort of fiprocess going from
x
to
y
.fl The
human mind often works by visual metaphors, and our visual image of a fiprocessfl from
x
to
y
is some sort of fiarrowfl from
x
to
y
:
x
f
!
y :
That's why we write
f
:
x
!
y
, of course. But now what we are doing is taking this
visual metaphor literally! We have a space
X
, like the piece of the computer screen on
which you are actually reading this text. The objects in

1
(
X
)
are then points in
X
, and
a morphism is basically just a path from
x
to
y
:
x
f
!
y :
Well, not quite; it's a homotopy class of paths. But still, something very interesting
is going on here: we are turning something ficoncretefl, namely the space
X
, into a
corresponding fiabstractfl thing, namely the groupoid

1
(
X
)
, by thinking of ficoncretefl
paths as fiabstractfl morphisms. Here I am thinking of geometrical concepts as ficoncretefl,
and algebraic ones as fiabstractfl.
You may wonder why we use homotopy classes of paths, rather than paths. One
reason is that topologists want to use

1
to distill a very abstract fiessencefl of the topo-
logical space
X
, an essence that conveys only information that's invariant under fihomo-
topy equivalencefl. Another reason is that we can easily get homotopy classes of paths to
compose associatively, as they must if they are to be morphisms in a category. We simply
glom them end to end:
x
f
!
y
g
!
z
and there is no problem with associativity, since we can easily reparametrize the paths to
make
(
f g
)
h
=
f
(
g h
)
. (If you haven't thought about this, please do!) If we do not work
with homotopy classes, it's a pain to dene composition in such a way that
(
f g
)
h
=
f
(
g h
)
. Unless you are sneaky, you only get that
(
f g
)
h
is
homotopic
to
f
(
g h
)
; there are
ways to get composition to come out associative, but they are all somewhat immoral.
As we shall see, if we want to preserve the ficoncretenessfl of
X
as much as possible,
and work with morphisms that are actual paths in
X
rather than homotopy equivalence
classes, the best thing is to work with
n
-categories. More on that later.
Let's see; I claimed there is a functor

1
:
Top
!
Gp d
, but so far I have only dened

1
on the objects of
Top
; we also need to dene it for morphisms. That's easy. A
morphism
F
:
X
!
Y
in
Top
is a continuous map from the space
X
to the space
Y
; this
is just what we need to take points in
X
to points in
Y
, and homotopy classes of paths
in
X
to homotopy classes of paths in
Y
. So it gives us a morphism in
Gp d
from the
fundamental groupoid

1
(
X
)
to the fundamental groupoid

1
(
Y
)
. There are various
things to check here, but it's not hard. We call this morphism

1
(
F
) : 
1
(
X
)
!

1
(
Y
)
.
With a little extra work, we can check that

1
:
Top
!
Gp d
, dened this way, is really a
functor.
132
 WEEK 75 MARCH 6, 1996
Perhaps you are nding this confusing. If so, it could easily be because there are
several levels of categories and such going on here. For example,

1
(
X
)
is a groupoid,
and thus a category, so there are morphisms like
f
:
x
!
y
in it; but on the other hand
Gp d
itself is a category, and there are morphisms like

1
(
F
) : 
1
(
X
)
!

1
(
Y
)
in it,
which are functors! If you nd this confusing, take heart. Getting confused this way
is crucial to learning
n
-category theory! After all,
n
-category theory is all about how
every fiprocessfl is also a fithingfl which can undergo higher-level fiprocessesfl. Complex,
interesting structures emerge from very simple ones by the interplay of these different
levels. It takes work to mentally hop up and down these levels, and to weather the
inevitable filevel slipsfl one makes when one screws up. If you expect it to be easy and
are annoyed when you mess up, you will hate this subject. When approached in the right
spirit, it is very fun; it teaches one a special sort of agility. (We are, by the way, nowhere
near the really tricky stuff yet.)
Okay, so we have seen an interesting example of a functor

1
:
Top
!
Gp d
:
As I said, we can think of this as going from the concrete world of spaces to the abstract
world of groupoids, turning concrete paths into abstract fimorphismsfl. Wonderfully,
there is a kind of fireversefl functor,
K
:
Gp d
!
Top
sending any groupoid
G
into a topological space
K G
called the ficlassifying spacefl of
G
.
This turns the abstract into the concrete, by making abstract morphisms into concrete
paths! Basically, it goes like this. Say we have a groupoid
G
. We will build the space
K
(
G
)
out of simplices as follows. Start with one 0-simplex for each object in
G
. A
0-simplex is simply a point. We can draw the 0-simplex for the object
x
as follows:
x
Then put in one
1
-simplex for each morphism in
G
. A
1
-simplex is just a line segment.
We can draw the
1
-simplex for the morphism
f
:
x
!
y
as follows:
x
y
f
Really we should draw an arrow going from left to right, but soon things will get too
messy if I do that, so I won't. Then, whenever we have
f g
=
h
in the groupoid, we stick
in a
2
-simplex. A
2
-simplex is just a triangle and we visualize it as follows:
x
y
z
f
h
g
f
:
x
!
y
g
:
x
!
z
h
:
y
!
z
Then, whenever we have
f g h
=
k
in the groupoid, we stick in a
3
-simplex, which we can
133
 WEEK 75 MARCH 6, 1996
visualize as a tetrahedron like this
x
x
y
z
f
g
h
k
f g
g h
f
:
w
!
x
g
:
x
!
y
h
:
y
!
z
k
:
w
!
z
And so on... we do this forever and get a big fisimplicial set,fl which we can think of as
the topological space
K G
. The reader might want to compare
 fiWeek 70fl
, where we do
the same thing for a monoid instead of a groupoid. Really, one can do it for any category.
That's how we dene
K
on objects; it's not hard to dene
K
on morphisms too, so
we get
K
:
Gp d
!
Top
In case you study this in more detail at some point, I should add that folks often think
of simplicial set as somewhat abstract combinatorial objects in their own right, and then
they break down
K
into two steps: rst they take the finervefl of a groupoid and get a
simplicial set, and then they take the figeometrical realizationfl of the simplicial set to get
a topological space. For more on simplicial sets and the like, try:
1)
 J. P. May,
Simplicial Objects in Algebraic Topology
, Van Nostrand, Princeton, 1968.
Now, in what sense is the functor
K
:
Gp d
!
Top
the fireversefl of the functor

1
:
Top
!
Gp d
? Is it just the fiinversefl in the traditional sense? No! It's something more subtle. As
we shall see, the fact that
Cat
is a
2
-category means that a functor can have a more subtle
and interesting sorts of fireversefl than one might expect if one were used to the simple
fiinversefl of a function. This is something I alluded to in
 fiWeek 74fl
: inverses become
subtler as we march up the
n
-categorical hierarchy.
I'll talk about this more later. But let me just drop a teaser... Quantum mechanics
is all about Hilbert spaces and linear operators between them. Given any (bounded)
linear operator
F
:
H
!
H
0
from one Hilbert space to another, there is a subtle kind of
fireversefl operator, called the fiadjointfl of
F
and written
F

:
H
0
!
H
, dened by
h
x; F

y
i
=
h
F x; y
i
for all
x
in
H
and
y
in
H
0
. This is not the same as the fiinversefl of
F
; indeed, it exists even
if
F
is not invertible. This sort of fireversefl operator is deeply related to the fireversefl
functors I am hinting at above, and for this reason those fireversefl functors are also called
fiadjointsfl. This is part of a profound and somewhat mysterious relationship between
quantum theory and category theory... which I eventually need to describe.
To continue reading the fiTale of
n
-Categoriesfl, see
 fiWeek 76fl
.
134
 WEEK 76 MARCH 9, 1996
Week 76
March 9, 1996
Yesterday I went to the oral exam of Hong Xiang, a student of Richard Seto who is looking
for evidence of quark-gluon plasma at Brookhaven. The basic particles interacting via
the strong force are quarks and gluons; these have an associated kind of fichargefl known
as color. Under normal conditions, quarks and gluons are conned to lie within particles
with zero total color, such as protons and neutrons, and more generally the baryons and
mesons seen in particle acccelerators Š and possibly glueballs, as well. (See
 fiWeek 68fl
for more on glueballs.)
However, the current theory of the strong force Š quantum chromodynamics Š pre-
dicts that at sufciently high densities and/or pressures, a plasma of protons and neu-
trons should undergo a phase transition called fideconnementfl, past which the quarks
and gluons will roam freely. At low densities, this is expected to happen at a temperature
corresponding to about 200 MeV per nucleon (i.e., proton or neutron). If my calculation
is right, this is about 2 trillion Kelvin! At low temperatures, it's expected to happen at
about 5 to 20 times the density of an atomic nucleus. (Normal nuclear matter has about
0.16 nucleons per femtometer cubed.) For more on this, check out these
1)
 Wikipedia, Quark-gluon plasma,
https://en.wikipedia.org/wiki/Quark-gluon
plasma
.
Relativistic Heavy Ion Collider homepage,
http://www.bnl.gov/RHIC/
.
The folks at Brookhaven are attempting to get high densities
and
temperatures by
slamming two gold nuclei together. They are getting densities of about 9 times that of
a nucleus... and I forget what sort of temperature, but there is reason to hope that the
combined high density and pressure might be enough to cause deconnement and create
a fiquark-gluon plasmafl. Colliding gold on gold at high energies produces a enormous
spray of particles, but amidst this they are looking for a particular signal of deconne-
ment. They are looking for
'
-mesons and looking to see if their lifetime is modied. A
'
-meson is a spin-
1
particle made of a strange quark / strange antiquark pair; strange
quarks and antiquarks are supposed to be common in the quark-gluon plasma formed
by the collision. Folks think the lifetime of a
'
-meson will be affected by the medium it
nds itself in, and that this should serve as a signature of deconnement. In fact, they
may have already seen this!
People might also enjoy looking at this review article:
2)
 Adriano Di Giacomo, fiMechanisms of colour connementfl, available as
hep-th/
9603029
.
Okay, let me continue the fiTale of
n
-Categoriesfl. I want to lead up to their role in
physics, but to do it well, there are quite a few things I need to explain rst. One of the
important things about
n
-category theory is that they allow a much more ne-grained
approach to the notion of fisamenessfl than we would otherwise be able to achieve.
In a bare set, two elements
x
and
y
are either equal or not equal; there is nothing
much more to say.
135
 WEEK 76 MARCH 9, 1996
In a category, two objects
x
and
y
can be equal or not equal, but more interestingly,
they can be
isomorphic
or not, and if they are, they can be isomorphic in many different
ways. An isomorphism between
x
and
y
is simply a morphism
f
:
x
!
y
which has an
inverse
g
:
y
!
x
. (For a discussion of inverse morphisms, see
 fiWeek 74fl
.)
For example, in the category Set an isomorphism is just a one-to-one and onto func-
tion. If we know two sets
x
and
y
are isomorphic we know that they are fithe same in
a wayfl, even if they are not equal. But specifying an isomorphism
f
:
x
!
y
does more
than say
x
and
y
are the same in a way; it species a
particular way
to regard
x
and
y
as
the same.
In short, while equality is a yes-or-no matter, a mere
property
, an isomorphism is a
structure
. It is quite typical, as we climb the categorical ladder (here from elements of a
set to objects of a category) for properties to be reinterpreted as structures, or sometimes
vice-versa.
What about in a
2
-category? Here the notion of equality sprouts still further nuances.
Since I haven't dened
2
-categories in general, let me work with an example, Cat. This
has categories as its objects, functors as its morphisms, and natural transformations as
its 2-morphisms.
So... we can certainly speak, as before, of the
equality
of categories. We can also
speak of the
isomorphism
of categories: an isomorphism between
C
and
D
is a functor
F
:
C ! D
for which there is an inverse functor
G
:
D ! C
. I.e.,
F G
is the identity
functor on
C
and
GF
is the identity on
D
, where we dene the composition of functors
in the obvious way. But because we also have natural transformations, we can also dene
a subtler notion, the
equivalence
of categories. An equivalence is a functor
F
:
C ! D
together with a functor
G
:
D ! C
and natural isomorphisms
a
:
F G
!
1
C
and
b
:
GF
!
1
D
. A finatural isomorphismfl is a natural transformation which has an inverse.
Abstractly, I hope you can see the pattern here: just as we can firelaxfl the notion
of equality to the notion of isomorphism when we pass from sets to categories, we can
relax the condition that
F G
and
GF
equal identity functors to the condition that they be
isomorphic to identity functors when we pass from categories to the
2
-category
Cat
. We
need to have the natural transformations to be able to speak of functors being isomor-
phic, just as we needed functions to be able to speak of sets being isomorphic. In fact,
with each extra level in the theory of
n
-categories, we will be able to come up with a
still more rened notion of fi
n
-equivalencefl in this way. That's what fiprocesses between
processes between processes...fl allow us to do.
But let me attem pt to bring this notion of equivalence of categories down to earth
with some examples. Consider rst a little category
C
with only one object
x
and one
morphism, the identity morphism
1
x
:
x
!
x
. We can draw
C
as follows:
x
where we don't bother drawing the identity morphism
1
x
. This category, by the way, is
called the fiterminal categoryfl. Next consider a little category
D
with two objects
y
and
z
and only four morphisms: the identities
1
y
and
1
z
, and two morphisms
f
:
y
!
z
and
g
:
z
!
y
which are inverse to each other. We can draw
D
as follows:
y
z
f
g
136
 WEEK 76 MARCH 9, 1996
where again we don't draw identities.
So:
C
is a little world with only one object, while D is a little world with only two
isomorphic objects... that are isomorphic in precisely one way!
C
and
D
are clearly
not isomorphic, because for a functor
F
:
C ! D
to be invertible it would need to be
one-to-one and onto on objects, and also on morphisms.
However,
C
and
D
are equivalent. For example, we can let
F
:
C ! D
be the unique
functor with
F
(
x
) =
y
, and let
G
:
D ! C
be the unique functor from
D
to
C
. (There is
only one functor from any category to
C
, since
C
has only one object and one morphism;
this is why we call
C
the terminal category.) Now, if we look at the functor
F G
:
C ! C
,
it's not hard to see that this is the identity functor on
C
. But the composite
GF
:
D ! D
is not the identity functor on
D
. Instead, it sends both
y
and
z
to
y
, and sends all the
morphisms in
D
to
1
y
. But while not
equal
to the identity functor on
D
, the functor
GF
is
naturally isomorphic
to it. We can dene a natural transformation
b
:
GF
!
1
D
by
setting
b
y
= 1
y
and
b
z
=
f
. Here some folks may want to refresh themselves on the
denition of natural transformation, given in
 fiWeek 75fl
, and check that
b
is really one
of these, and that
b
is a natural isomorphism because it has an inverse.
The point is, basically, that having two uniquely isomorphic things with no morphisms
other than the isomorphisms between them and the identity morphisms isn't really all
that different from having one thing with only the identity morphism. Category theorists
generally regard equivalent categories as fithe same for all practical purposesfl. For exam-
ple, given any category we can nd an equivalent category in which any two isomorphic
objects are equal. We call these fiskeletalfl categories because all the fat is gone and just
the essential bones are left. For example, the category
FinSet
of nite sets, with functions
between them as morphisms, is equivalent to the category with just the sets
0 =
fg
1 =
f
0
g
2 =
f
0
;
1
g
3 =
f
0
;
1
;
2
g
etc., and functions between them as morphisms (see
 fiWeek 73fl
). Essentially all the
mathematics that can be done in
FinSet
can be done in this skeletal category. This
may seem shocking, but it's true. . . . Similarly, the category
Set
is equivalent to the
category
Card
having one set of each cardinality. Also, the category
Vect
of complex
niteŒdimensional vector spaces, with linear functions between them as morphisms, is
equivalent to a skeletal category where the only objects are those of the form
C
n
.
This
example should not seem shocking; it's this fact which allows unsophisticated people to
do linear algebra under the impression that all nite-dimensional vector spaces are of the
form
C
n
, and still manage to do all the practical computations that more sophisticated
people can do, who know the abstract denition of vector space and thus know of lots
more nite-dimensional vector spaces.
However, there is another thing we can do in
Cat
, another renement of the notion
of isomorphism, which I alluded to in
 fiWeek 75fl
. This is the notion of fiadjoint functorfl.
Let me mention a few examples (in addition to the example given in
 fiWeek 75fl
) and
let the reader ponder them before giving the denition. Let
Grp
denote the category
with groups as objects and homomorphisms as morphisms, a homomorphism
f
:
G
!
H
between groups being a function with
f
(1) = 1
and
f
(
g h
) =
f
(
g
)
f
(
h
)
for all
g ; h
in
G
.
137
 WEEK 76 MARCH 9, 1996
Then there is a nice functor
L
:
Set
!
Grp
which takes any set
S
to the free group on
S
: this is the group
L
(
S
)
formed by all formal
products of elements in
S
and inverses thereof, with no relations other than those in the
denition of a group. For example, a typical element of the free group on
f
x; y ; z
g
is
xy z y

1)
-morphism to be an equivalence if it's invertible up to an equivalence. This
downwards induction leaves off when we dene equivalence for fi
0
-morphismsfl, mean-
ing objects.)
We have also begun talking about a curious situation where the categories
C
and
D
are not at all fithe same,fl but there are fiadjointfl functors
L
:
C ! D
and
R
:
D !
C
. Let
me list some examples before dening the concept of adjoint functor and talking about
it:
1.
 First for the one we discussed in
 fiWeek 76fl
. Let
Set
be the category of sets, and
Grp
the category of groups. Let
L
:
Set
!
Grp
be the functor taking each set
S
to
the free group on
S
, and doing the obvious thing to morphisms. Let
R
:
Grp
!
Set
be the functor taking each group to its underlying set.
2.
 Let
Ab
be the category of abelian (i.e., commutative) groups. Let
L
:
Set
!
Ab
be
the functor taking each set
S
to the free abelian group on
S
. The fifree abelian
groupfl on
S
is what we get by taking the free group on
S
and imposing commu-
tativity relations like
xy
=
y x
for all elements
x; y
in
S
. Let
R
:
Ab
!
Set
be the
functor taking each abelian group to its underlying set.
3.
 Let
L
:
Grp
!
Ab
be the functor taking each group
G
to its fiabelianizationfl. The
abelianization of
G
is what we get when we impose the extra relations
xy
=
y x
for
all elements
x; y
in
G
. Let
R
:
Ab
!
Grp
be the functor taking each abelian group
to its underlying group.
4.
 Let
Mon
be the category of monoids, where the objects are monoids and the mor-
phisms are monoid homomorphisms. (Remember that a monoid is a set with an
associative product and a unit; a monoid morphism
f
:
M
!
N
is a function be-
tween monoids such that
f
(
xy
) =
f
(
x
)
f
(
y
)
and
f
(1) = 1
.) Let
L
:
Set
!
Mon
be
the functor taking each set
S
to the free monoid on
S
. This is simply the set of
words whose letters are elements of
S
, with the product given by concatenation
of words, and the unit being the empty word. Let
R
:
Mon
!
Set
be the functor
taking each monoid to its underlying set.
5.
 Let
L
:
Mon
!
Grp
be the functor taking each monoid
M
to the group obtained
by throwing in formal inverses for every element of
M
. The famous example of
this is when
N
=
f
0
;
1
;
2
; :::
g
, which is a monoid whose fiproductfl is addition.
Then
L
(
N
) =
Z
, the integers, since we have thrown in the negative integers. Let
R
:
Grp
!
Mon
be the functor taking each group to its underlying monoid. I.e.,
R
simply forgets that our group has inverses and thinks of it as a monoid.
Note the common aspects of these examples! In most of them,
L
:
C ! D
gives us a
fifreefl object of
D
for every object of
C
, while
R
:
D ! C
gives us an fiunderlyingfl object
of
C
for every object of
D
. This is an especially good way to think about it when the
141
 WEEK 77 MARCH 23, 1996
objects of
D
are objects of
C
equipped with extra structure, as in examples 1, 2, 4, and 5.
For example, a group is a set equipped with some extra structure, the group operations.
In this case, the functor
L
:
C ! D
turns an object of
C
into an object of
D
by fifreely
throwing in whatever extra stuff is necessary, without putting in any relations other than
those needed to get an object of
D
fl.
It's not quite the same when the objects of
D
are objects of
C
with extra
properties
,
as in example 3. In this case, the functor
L
:
C ! D
forces an object of
C
to have the
properties needed to be an object of
D
. It does so in as nonviolent a manner as possible.
In either of these situations,
R
:
D ! C
has the avor of what we call a fiforgetfulfl
functor. This is not a precisely dened term, but folks use it whenever we can simply
fiforgetfl something about an object of
D
and think of it as an object of
C
. For example,
we can take a group, and forget about the group operations, thinking of it as merely a
set. Here we are forgetting extra structure; we can also forget extra properties.
The crucial thing here is that unlike in an equivalence, there is a built-in asymmetry
here:
L
and
R
have very different avors, and serve different mathematical purposes.
We call
L
the fileft adjointfl of
R
, and we call
R
the firight adjointfl of
L
.
There are situations where adjoint functors
L
and
R
aren't so immediately reminis-
cent of the concepts fifreefl and fiunderlyingfl. But it's good to keep these ideas in mind
when learning about adjoint functors. I used to have trouble remembering which was
supposed to be the left adjoint and which was the right. The honest way to do this is to
remember the denition (coming up soon), but for a cheap mnemonic, you can think of
the L in a left adjoint as standing for filibertyfl Š that is, freedom!
So what's the denition of fiadjointfl? Roughly speaking, it's that for any object
c
of
C
and any object
d
of
D
, we have
Hom(
Lc; d
) = Hom (
c; R d
)
:
Actually this is a slight exaggeration: we don't want these to be equal. The guy on the
left is the set of morphisms from
Lc
to
d
in the category
D
. The guy on the right is the
set of morphisms from
c
to
R d
in the category
C
. So it's evil to want them to be
equal
.
As you might guess, it's enough for them to be naturally isomorphic in some sense. Let's
not worry about that too much yet, though. Let's get the basic idea here!
Consider example 1. Say
S
is a set and
G
is a group. Why is
Hom(
LS ; G
)
naturally isomorphic to
Hom(
S ; R G
)
?
In other words, why is the set of homomorphisms from the free group on
S
to
G
naturally isomorphic to the set of functions from
S
to the underlying set of
G
?
Well, say we have a homomorphism
f
:
LS
!
G
. Since
LS
is a free group, we know
f
if we know what it does to each element of
S
... and it can do whatever it wants to
these elements! So we can think of it as just a function from
S
to the underlying set of
G
.
In other words, we can think of it as a function
f
0
:
S
!
R G
. Conversely, any function
f
0
:
S
!
R G
gives us a homomorphism
f
:
LS
!
G
.
So this is the idea. Say we have an object
c
of
C
and an object
d
of
D
. Then:
fiThe set of morphisms from the free
D
-object on
c
to
d
is natu rally isomorphic
to the set of morphisms from
c
to the underlying
C
-object of
d
.fl
142
 WEEK 77 MARCH 23, 1996
Next time I will nish off the denition of adjoint functors, by making this finaturally
isomorphicfl stuff precise. I will also begin to explain what adjoint functors have to
do with adjoint operators in quantum mechanics. Remember that an fiobservablefl in
quantum theory is an operator on a Hilbert space which is its own adjoint, while a
fisymmetryfl in quantum theory is an operator whose adjoint is its inverse. I eventually
hope to show that this, and many other shocking aspects of quantum theory, become less
shocking when we think of the world in terms of categories (or
n
-categories) rather than
sets. The way I think of it these days, the mysterious way quantum theory slammed into
physics in the early 20th century was just nature's way of telling us we'd better learn
n
-category theory.
I'll also explain what adjoint functors have to do with the following topological equa-
tions:
=
=
To continue reading the fiTale of
n
-Categoriesfl, see
 fiWeek 78fl
.
143
 WEEK 78 MARCH 28, 1996
Week 78
March 28, 1996
Last Week I began explaining the concept of fiadjoint functorfl. This Week I want to nish
explaining it Š or at least nish one round of explanation! Then we'll begin to be able to
see the unity of category theory, topology, and quantum theory. These may seem rather
distinct subjects, but they have an interesting tendency to blur together when one is
doing topological quantum eld theory. Part of the point of higher-dimensional algebra
is to explain this.
So, remember the idea of adjoint functors. Say we have categories
C
and
D
and
functors
L
:
C ! D
and
R
:
D ! C
. Then we say
L
is the fileft adjointfl of
R
, or that
R
is the firight adjointfl of
L
, if for any object
c
of
C
and object
d
of
D
, there is a natural
one-to-one correspondence between
Hom(
Lc; d
)
and
Hom(
c; R d
)
. An example to keep
in mind is when
C
is the category of sets and
D
is the category of groups. Then
L
turns
any set into the free group on that set, while
R
turns any group into the underlying set
of that group. All sorts of other fifreefl and fiunderlyingfl constructions are also left and
right adjoints, respectively.
Now the only thing I didn't make very precise is what I mean by finaturalfl in the
above paragraph. Informally, the idea of a finaturalfl one-to-one correspondence is that
doesn't depend on any arbitrary choices. The famous example is that if we have a nite-
dimensional vector space
V
, it's always isomorphic to its dual
V

, but not naturally so:
to set up an isomorphism we need to pick a basis
e
i
of
V
, and this gives a dual basis
f
i
of
V

, and then we get an isomorphism sending
e
i
to
f
i
, but this isomorphism depends
on our choice of basis. But
V
is
naturally
isomorphic to its double dual
(
V

)

.
Now, it's hard to formalize the idea of finot depending on any arbitrary choicesfl
directly, so one needs to reect on why it's bad for an isomorphism to depend on arbitrary
choices. The main reason is that the arbitrariness may break a useful symmetry. In
fact, Eilenberg and Mac Lane invented category theory in order to formalize this idea
of finaturality as absence of symmetry-breakingfl. Of course, they needed the notion of
category to get a sufciently general concept of fisymm etryfl. They realized that a nice
way to turn things in the category
C
into things in the category
D
is typically a functor
F
:
C ! D
. And then, if we have two functors
F ; G
:
C ! D
, they dened a finatural
transformationfl from
F
to
G
to be a bunch of morphisms
T
c
:
F
(
c
)
!
G
(
c
)
;
one for each object
c
of
C
, such that the following diagram commutes for every morphism
f
:
c
!
c
0
in
C
:
F
(
c
)
F
(
c
0
)
G
(
c
)
G
(
c
0
)
F
(
f
)
T
c
T
c
0
G
(
f
)
This condition says that the transformation
T
gets along with all the fisymmetriesfl, or
more precisely morphisms
f
, in the category
D
. We can do it either before or after
applying one of these symmetries, and we get the same result. For example, a vector
144
 WEEK 78 MARCH 28, 1996
space construction which depends crucially on a choice of basis will fail this condition if
we take
f
to be a linear transformation corresponding to a change of basis.
A finatural isomorphismfl is then just a natural transformation that's invertible, or in
other words, one for which all the morphisms T
c
are isomorphisms.
Okay. Hopefully that explains the idea of finaturalityfl a bit better. But right now we
are trying to gure out what we mean by saying that
Hom(
Lc; d
)
and
Hom(
c; R d
)
are
naturally isomorphic. To do this, we need to introduce a couple more ideas: the product
of categories, and the opposite of a category.
First, just as you can take the cartesian product of two sets, you can take the cartesian
product of two categories, say
C
and
D
. It's not hard. An object of
C  D
is just a pair of
objects, one from
C
and one from
D
. A morphism in
C  D
is just a pair of morphisms,
one from
C
and one from
D
. And everything works sort of the way you'd expect.
Second, if you have a category
C
, you can form a new category
C
