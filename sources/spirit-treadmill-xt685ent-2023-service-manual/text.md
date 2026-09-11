<!-- Source: XT685ENT Service Manual.pdf. Text is pdftotext -layout; pages a 300 dpi render knows more about than the text layer are appended below under '=== OCR SUPPLEMENT, PDF PAGE n ===' headers. -->

                    1 of 52




SERVICE MANUAL
        XT685(ENT)(2023)
           XT816-NT052
           ENT Treadmill
                                                                                                                                                                 2 of 52



                                                                          -Contents-
1 . O u t l i n e s ....................................................................................................................................................... 3
2 . E l e c t r o n i c                P a r t s ............................................................................................................................. 4
3 . E l e c t r i c a l               C o n f i g u r a t i o n s .............................................................................................. 5
4 . P r o d u c t              O p e r a t i o n ...................................................................................................................... 6
5 . U n i t          B l o c k          D i a g r a m s .............................................................................................................. 10
6 . B a s i c           C o n n e c t i o n s                    a n d        W i r i n g .............................................................................. 11
       6 . 1 D i s p l a y B o a r d w i r e C o n n e c t i o n s .................................................................................. 11
       6 . 2 D i s p l a y B o a r d P C B C o m p o n e n t L o c a t i o n s ............................................................ 12
       6 . 3 D r i v e r B o a r d W i r e C o n n e c t i o n s .................................................................................... 14
       6 . 4 D r i v e r B o a r d P C B C o m p o n e n t L o c a t i o n s ............................................................... 15
       6 . 5 D r i v e r B o a r d f u n c t i o n ............................................................................................................ 15
       6 . 6 D r i v e r B o a r d L E D I n d i c a t o r L o c a t i o n s ................................................................... 17
       6 . 7 C o n t r o l l e r I n d i c a t o r L E D d e b u g g i n g ........................................................................ 17
7 . P r o d u c t              S a f e t y           I n s t r u c t i o n s .................................................................................... 18
8 . E r r o r           M e s s a g e s               /       T r o u b l e s h o o t i n g ................................................................ 19
       8 . 1 E r r o r M e s s a g e : E 0 ...................................................................................................................... 20
       8 . 2 E r r o r M e s s a g e : E 1 ...................................................................................................................... 22
       8 . 3 E r r o r M e s s a g e : E 2 / O V E R C U R R E N T ............................................................................. 28
       8 . 4 E r r o r M e s s a g e : E 3 ...................................................................................................................... 28
       8 . 5 E r r o r M e s s a g e : E 4 ...................................................................................................................... 34
       8 . 6 E r r o r M e s s a g e : E 5 ...................................................................................................................... 35
       8 . 7 E r r o r M e s s a g e : E 6 ...................................................................................................................... 36
       8 . 8 C i r c u i t D i a g r a m ............................................................................................................................ 37
       8 . 9 C a l i b r a t i o n P r o c e d u r e ............................................................................................................ 39
9 . P a r t s           R e p l a c i n g                 G u i d e ........................................................................................................ 43
       9 . 1 R e p l a c i n g t h e C o n t r o l l e r .................................................................................................... 43
       9 . 2 R e p l a c i n g t h e C o n s o l e A s s e m b l y ................................................................................. 44
       9 . 3 R e p l a c i n g t h e D r i v e M o t o r ................................................................................................ 45
       9 . 4 R e p l a c i n g t h e B r e a k e r ........................................................................................................... 46
       9 . 5 R e p l a c i n g t h e A C P o w e r S w i t c h .................................................................................... 46
       9 . 6 R e p l a c i n g t h e F r o n t a n d R e a r R o l l e r ...................................................................... 47
       9 . 7 R e p l a c i n g t h e R u n n i n g D e c k , R u n n i n g b e l t , a n d C u s h i o n s ................ 49
       9 . 8 R e p l a c i n g t h e S p e e d S e n s o r ............................................................................................. 51
       9 . 9 R e p l a c i n g t h e I n c l i n e M o t o r ........................................................................................... 51
             3 of 52


1.Outlines
                                          4 of 52


2.Electronic Parts
CONSOLE




C O N TRO L L ER AN D D R I V ER PAR TS
                                                                                                                      5 of 52


3.Electrical Configurations
SAFETY KEY      Th e s afety key f it s i nto t h e Con so l e to a cti vate a ll fu n cti on s an d tread m i ll. Wi th ou t
                s afety key, con sol e can n ot b e con trol l ed , an d tread m ill wil l n ot b e a ct ivated .
Console         Interfac e t h at control s a ll fu n cti on s o f th e tread mi ll .
Main            Th e circu i t b oa rd con s is ts of th e DC p ow er su p p ly for con so le 、 in c li n e d riv er an d
Controller      DC m oto r d riv er, li n k th e con so l e to ou t p u t ap p rop ri ate v oltage s for mo tor th at
                co ntro l th e t re ad mi ll fu n cti on s.
Drive Motor     Th is i s a D C mo tor with var iab le sp eed .         Con trol th e 0 –9 0 ( or 0 - 18 0) vol ta ge s
                fro m t h e m ain controll e r to in crea s e o r d ecre as e sp e ed o f t h e ru n n in g b el t.
Incline Motor   Th is i s a n AC motor. U s e r can co ntro l var iab l e e l evati on by con so l e wit h i n ma in
                co ntro ll er.


G E NE R AL IN FO RMAT IO N
Console         Th e con s ol e co mp ri s ed of keys control a n d 1 5. 6 -in ch s cre en d is p l ay.
                Main control le r In cl u d e p ow er su p p ly 、 motor d riv er control circu it an d in c lin e
                co ntro l c ircu it .
Drive Motor     It ’s a var iab l e sp eed on 0 - 9 0 vo lt DC motor. (0 - 1 80 vol ts D C mo tor on 22 0 Vac
                el e ctron ic p ow er syste m )
                Hav e th re e wire s red , b l ack a n d g reen .
                If th e re i s D C vo lta ge o n th e Re d ( wh ite ) wire ( M +) th e t re ad mi ll mo tor wi ll tu rn
                clo ck wi s e .
                If th e re i s D C vo lta ge o n th e B lac k wi re ( M -) th e tre ad mi ll mo tor wil l tu r n co u nter -
                clo ck wi s e .
                Wh e n th e h igh er vo lta ge s, th e sp e ed i s fas ter.
                Th e gree n wire i s grou n d in g .
Incline Motor   Th is i s a 1 20 vol t AC mo tor. (2 2 0 vo lt s AC mo tor on 2 20 Vac e l ectron i c p ow er
                syste m)
                Hav e fou r w ire s, red , b l ack, wh ite, an d gree n .
                Has on e 3 p in s cab l e of p os it ion s en sor.
                If th e re i s AC v oltage on th e red wi re ( UP ) th e in cli n e m oto r wi ll in crea s e th e
                in c lin e.
                If th e re i s AC v oltage on th e B lac k wi re ( DOWN ) th e in c li n e m oto r wi ll d ec re a se th e
                in c lin e.
                Th e Wh ite w ire (CO M) i s n eu t ra l.
                Th e gree n wire i s grou n d .
                                                                                                                   6 of 52


4.Product Operation
15.6” TOUCH SCREEN




WINDOW DISPLAY MODE
OFF Mode     Wh e n u s er d oe sn ’ t in s e r t th e SA FE T Y KE Y on th e con s ol e, t h e tread m il l en ters th e
             OF F Mod e, an d th e wi n d ow wi ll ap p ear “P LEA SE RE PL ACE TH E SA FE T Y KE Y ”.
READY        Wh e n th e t re ad mi ll i s O N an d S AFE T Y KE Y is in s er ted in con sol e, th e wi n d ow w il l
Mode         sh ow p rog ra m s n a m e fo r ch oo sin g an d q u i ck s ta rt fo r tap to b e gin wor kou t. Pre s s
             STA RT b u tton to start tread m ill on Man u al Mod e.
SLEEP Mode   In S LE E P Mod e, i f a nyon e b u tton i s p re s s ed th en th e tread m il l e nters RE A DY M od e .
RUN Mode     In R UN Mod e, p re ss in g t h e “S TO P ” b u tton an d re m ovin g th e S AFE T Y KE Y w ill cau s e
             th e tread mi ll stop in sta ntly an d ente r O F F M od e.
                                                                                                                   7 of 52


FUNCTION
SPEED      Di sp lay th e c u rren t sp ee d in mi l e p er h ou r (k ilo me te r p er h ou r ).
           DI SPL AY ran ge i s 0. 0 to 99 .9.
           WO RK ra n ge i s 0.5 ~ 12 .0 mp h ( 1.0 ~ 2 .0 km p h )
           Pre s s “ FAS T ” or ”S LOW ” to ad ju st sp e ed , ea ch in cre me nt a n d d ec re m en t is 0 .1
           km /h ( mp h ).
INCLINE    Di sp lay th e in cl in e p o s it ion fro m 0 to 1 5.
           DI SPL AY ran ge i s 0 to 99 9.
           WO RK ra n ge i s 0.0 to 1 5 .0.
           IN C LIN E p re s et va lu e i s 0. 0.
           Pre s s “ UP ” or ” D OWN ” to ad ju st in cl in e, ea ch in cre me nt o r d ec rem e nt i s 0. 5.
TIME       TI ME is e ith er CO UN T U P or C O UN T DOWN. Sys te m p re se t i s C O UN T UP ; if u se r se ts
           th e ti m e, th en ti m er i s COUN T D OWN .
           DI SPL AY ran ge i s 0 :0 0 to 99 9 :9 9.
           COUN T D OWN setu p ra n ge i s 1 0: 00 to 9 9: 00 .
           Wh e n TI ME i s s et, t h e cou nt w ill go to zero .
           In R UN Mod e, p re ss “S TOP ” b u tton to s av e va lu e o f t i m e an d e nter “R U N Mod e”
           again th at valu e wi ll con tin u e cou nt t i me .
PACE       It me an s: H ow l on g w il l take s to wa lk (or ru n ) p er ea ch Km or M il e at cu rre nt sp e ed ?
           Th e u n it i s min /Km o r m in / Mi .
           DI SPL AY ran ge i s 0 0 ： 0 0 to 99 ： 99 .
           WO RK ra n ge i s 00 ： 00 to 9 9 ： 9 9.
DISTANCE   Di sp lay th e c u rren t d is tan c e i n ki lo me ter o r Mil e.
           DI SPL AY ran ge i s 0. 00 to 99 .9 9.
           WO RK ra n ge i s 0.0 0 to 9 9. 99.
CALORIES   Di sp lays th e cu mu l ati ve ca lor i es b u rn ed at any g ive n ti m e d u ri n g you r w orkou t.
           DI SPL AY ran ge i s 0 to 99 9.
           WO RK ra n ge i s 0 to 9 99 .
PULSE      Di sp lays th e h ea rt rate b eat by u sin g h an d p u l s e o r rec e iv er. Wh en u s e re ce iv er, a
           ch es t b el t mu st b e w orn .
           DI SPL AY ran ge i s 0 to 99 9.
           WO RK ra n ge i s 50 to 20 0 B PM .
           In R UN Mod e, i f th e t re ad m il l d o e sn ’t h av e a s i gn al for 8 s e con d s, th en d i sp l ay va lu e
           wi ll b e com e “0 ”.
                                                                                                                     8 of 52


FU N CT ION BU T TO N LO CAT IO N




BUTTON FUNCTION IN EACH MODE

Ready Mode
Safety Key           Set s afety key in ri ght p os iti on to p ow er on th e co mp u ter. W h e n safe ty key
                     is p u l l ed away from it s p os it ion , t h e w in d ow w i ll ap p e ar “ PLE AS E RE PL ACE
                     THE S A FE T Y KE Y ”.
Stop Key             N on -f u n ct ion al.
Start Key            Pre s s in g “STA RT ” b u tton to start tread mi ll, wh e n p res s in g “STA RT ” b u tton ,
                     th ere w il l b e 3 se con d fi n al cou nt d own on win d ow d i sp l ay, th e n mac h in e
                     start s ru n n i n g. In MA N UAL , tre ad mil l start s at M IN S PE E D an d t re ad mi ll
                     start s at p rog ra m p re s et va lu e in P RO G R A M.
Speed Fast Key       If u s e r d o e sn ’t e nter a s ettin g , th en th i s b u tto n is n on - fu n cti on a l.
Speed Slow Key       If u s e r d o e sn ’t e nter a s ettin g , th en th i s b u tto n is n on - fu n cti on a l.
Incline Up Key       If u s e r d o e sn ’t e nter a s ettin g , th en th i s b u tto n is n on - fu n cti on a l.
Incline Down Key     If u s e r d o e sn ’t e nter a s ettin g , th en th i s b u tto n is n on - fu n cti on a l.
Speed quick Keys     N on -f u n ct ion al.
Incline quick Keys   N on -f u n ct ion al.
Fan Switch           It can co ntro l O N / OF F fo r th e fan .
Child Lock Key       Wh e n th is in E N G INE E RI NG MO DE settin g loc k key ON th at al l keyb oa rd
                     b u tton n o wo rki n g , th e n MW w il l sh ow th e “HO L D CHI LD LO C K BUT TON 3
                     SECON D S TO UN LO CK ”. ( On th e I DLE M ODE d o e s n ot wo rk after 5 mi n u te s o f
                     d etect ion , th e l oc ked wi ll ON. ) i f lo ck key of f at E NGI NE E R IN G M ODE
                     settin g , th at u n it keyb o ard can w ork in g .
DISABLE Key          To co ntro l ON /O F F fo r t h e h a n d rai l sp ee d /i n c lin e s w itch .
                                                                                                                   9 of 52


Run Mode
Safety Key           Wh e n safe ty key i s p u l le d away fro m it s p o s iti on , th e co mp u te r wi ll b e
                     au to mati ca lly s h u t d ow n .
Stop Key             p re s s “ STOP ” b u tton to stop t re ad mi ll.
Start Key            N on -f u n ct ion al.
Speed Fast Key       Pre s s th e b u tton to in c rea s e you r sp e ed an d e ac h in c rea s e i s
                     0. 1kp h (0 .1 mp h ). I f b u tton i s p re s s ed co nt in u ou sly th en sp e ed i n cre as e s to
                     MA X SPE E D q u i ck ly.
Speed Slow Key       Pre s s th e b u tton to d e crea s e you r sp e ed an d e ac h d e crea s e i s
                     0. 1kp h (0 .1 mp h ). I f b u tton i s p re s s ed co nt in u ou sly th en sp e ed d e crea s e s to
                     MIN SPE E D q u ic kl y.
Incline Up Key       Pre s s th e b u tton to rai s e p o s iti on an d each in crea s e i s 0. 5, th e maxi mu m
                     in c lin e p o sit ion i s 1 5.
Incline Down Key     Pre s s th e b u tton to low er p o sit ion an d ea ch d e crea s e i s 0. 5, t h e m in im u m
                     in c lin e p o sit ion i s 0 .
Speed quick Keys     Sp eed wil l se t to 1 ， 2 ， 3 ， 4 ， 5 ， 6 ， 7 ， 8 ， 10 ， 12 s p e ed q u i ckly .
                     (N ote : O n 2 0. 0kp h s p e c is 2, 4, 6, 8, 10, 1 2, 14, 16, 1 8, 2 0 )
Incline quick Keys   In cl in e wi ll s et to 0 ， 1 ， 2 ， 4 ， 5 ， 6 ， 8 ， 1 0 ， 12 ， 15 p o si tion q u i ck ly.
Fan Switch           It can co ntro l O N / OF F fo r th e fan .
Child Lock Key       N on -f u n ct ion al.
DISABLE Key          To co ntro l ON /O F F fo r t h e h a n d rai l sp ee d /i n c lin e s w itch .
                        10 of 52


5.Unit Block Diagrams
                                     11 of 52


6.Basic Connections and Wiring

6.1 Display Board wire Connections
                                            12 of 52


6.2 Display Board PCB Component Locations

PCB BOARD TOP VIEW




PCB BOARD BOTTOM VIEW
13 of 52
                                    14 of 52


6.3 Driver Board Wire Connections
                                           15 of 52


6.4 Driver Board PCB Component Locations




6.5 Driver Board function
16 of 52
                                                                                                                    17 of 52


6.6 Driver Board LED Indicator Locations




6.7 Controller Indicator LED debugging

Indicator
          Function         Condition                          Reason                         Solve
LED
POWE R    Con t ro ll er   If D C v o lta ge is n or ma l, it Vol tag e is n o t c orr e ct. Ch eck th e s u p p ly v o lta g e is
                                                              Fu s e is b lo wn .               12 0V ac .
          p ow e r         wou ld b e a l way s ON.                                            (on  22 0 Vac e l ect ron ic p ow er
                                                              Tr an s f or m er is n o go od .
                           If of f, fa u lt con d it ion                                        s ys te m n e ed 22 0V ac )
                                                                                               Re p la c e F u s e .
                           ex is ts .
                                                                                               Re p la c e c on tr ol le r.
                                                                                                                                    18 of 52


7.Product Safety Instructions
Important Safety Instructions
- To red u c e th e ri sk of e le ctr i c sh o ck, d i s con n ec t you r tread m ill fro m th e el e ctr i cal ou t let p ri or to
cl ean in g an d /o r s er vi c e work.
- To red u c e th e ri sk of b u rn s, fire, e l ect ri c sh o ck , or in ju ry to p erson s, in stall th e tre ad mil l on a f lat
lev el su rfa c e wit h a cc e s s to a 2 20 -v olt , 1 0 -a mp grou n d ed ou tl et w ith o n ly th e t re ad mi ll p lu g ged into
th e ci rcu it. 【 1 20 VAC e le ctro n i c p ow er syste m i s 11 0 -vo lt, 1 5 - a mp 】
- Do n o t u s e an exten si o n co rd u n l es s it i s a 1 6 AWG o r b etter wi th on ly on e ou t let on th e en d . Do n o t
atte mp t to d i sa b l e th e g rou n d e d p lu g by u s in g i mp rop e r ad a p ters or in any way mod if y t h e cord ou tl et.

Important Electrical Instructions
- N ev er u s e a gro u n d fa u lt circu i t i nter ru p t ( G FCI ) wa ll o u tl et wi th th i s tre ad mi ll. A s w ith a ny a p p lia n c e
wi th a large mo tor, th e G FCI wi ll tr ip o ften . Rou te th e p ow er co rd away fro m a ny m ovi n g p art o f th e
tre ad mi ll in c lu d i n g th e el evat ion m ec h an i s m an d t ra n sp or t wh ee l s.
- C i rcu it B reake rs : S o me circu it b rea kers u s ed i n h om e s are n o t rated for h igh in ru sh c u rren t s th at can
occ u r wh en a tread m il l i s firs t tu r n e d on or eve n d u rin g u s e. I f you r trea d mi ll i s t rip p in g th e h ou s e
circu i t b rea ker (ev en th ou gh it i s th e p rop e r cu r ren t rat in g ) b u t th e circ u it b rea ker on th e tread mi ll
it se l f d o e s n ot t rip , you wi ll n e ed to re p la c e th e h om e b re aker with a h ig h in ru sh typ e. Th i s i s n o t a
wa rranty d efe ct. Th i s is a con d i tion w e a s a m an u factu re h av e n o ab i lity to con trol . Th is p ar t i s
avai lab le th rou gh mos t el e ctr i cal s u p p ly s tore s . E xa mp l e s: G ra in ger p a r t # 1 D2 37, or ava il ab l e on lin e at
w w w. sq u ared . com p ar t # Q O 12 0H M.


Important Grounding Instructions
- Th i s p rod u ct m u st b e g ro u n d ed . If th e trea d m ill s h ou l d mal fu n ct ion o r b rea kd own , grou n d in g
p rov id e s a p ath o f l east re sis tan ce for e l ect ri c c u rrent, red u c in g th e r i s k of e l ec tri c sh o ck . Th i s p rod u c t
is eq u ip p ed w ith a cord h avi n g an eq u ip m e nt - grou n d in g p lu g . Th e p l u g mu st b e p lu g ged in to a n
ap p rop r iate ou t let th at is p rop er ly i n sta ll ed an d grou n d ed in ac co rd an c e wi th a ll lo ca l cod e s an d
ord in a n c e s.
- DANG E R - I m p rop er co n n ect io n o f th e eq u ip m ent -g rou n d in g con d u cto r can res u l t in a r i sk o f ele ctr ic
sh o ck . Ch eck w ith a q u a l if ied e lectr ic i an o r se r v icem an if you ar e in d ou bt as to wh eth er th e p rod u c t
is p ro p er l y g rou n d ed . D o n o t m o d if y th e p lu g p rovid ed w ith th e p rod u ct i f it w i ll n ot f it th e o u tl et;
h ave a p rop er ou t l et in sta ll ed by a q u a li f ied e le ctr ic i an . T h i s p rod u c t i s for u s e on a n o m in a l 2 2 0 -vo lt
(on 12 0 VAC e l ectron i c p ow er sys te m n e ed 1 10 VAC) c ircu it an d h a s a gro u n d in g p lu g th at loo ks l i ke th e
p lu g il lu st rate d b el ow. A te mp orary ad a pte r th at loo ks l ike t h e ad a pter i l lu st rated b e l ow may b e u s ed
to con n e ct th i s p lu g to a 2 -p o l e rec e pta cl e a s s h own b e l ow i f a p rop er l y grou n d ed ou t let i s n o t
avai lab le . Th e te mp o ra r y ad a pter sh ou ld b e u se d on ly u nt il a p rop er ly g rou n d e d ou t let , ( sh own b el ow )
can b e in stal led by a q u ali fi ed e l ect ri ci an . Th e g re en co lored ri gid e arp l u g s, o r th e li ke, exten d i n g fro m
th e ad a pter, mu s t b e c o n n e cted to a p e r man ent grou n d su ch a s a p rop e rly grou n d ed ou t let b ox cov er.
Wh e n ev er th e ad a p te r i s u s ed , it mu s t b e h eld i n p la c e by a me tal s crew.
                                                                                                           19 of 52


8.Error Messages / Troubleshooting
ERROR CODE LIST

            Code      Description
                 E0   Th e d i sp l ay ap p e ars PL E ASE RE P L ACE THE S AFE T Y KE Y. It m ean s safe ty
                      key i s re m ove d .
                 E1   Di sp lay b oard C P U d i d n ot rec e iv e th e RP M si gn al. (on ly ca lib ration )
                 E2   Tread m il l motor i s ov er cu rre nt .
                 E3   Th e con s ol e b o ard i s n o t d ete ctin g t h e V R vo lta ge valu e, or th e
                      volta ge va lu e h a s exc e e d ed t h e ra n ge .
                 E4   Tread m il l motor w ire s o r vo lt p o s s ib l e a b n or m al .
                 E5   Co m mu n icat ion s in g l e i s ab n or m al.
                 E6   Lowe r Con trol b oard p o s sib l e b ro ken .


TOOLS REQUIRED

A multi-meter.
                                                                                                                 20 of 52


8.1 Error Message: E0




DEFINITION:
C o n s o l e i s n o t i n s e r t e d s a f e t y, o r s a f e t y m o d u l e m a y b e b r o k e n . O r e l s e
component of upper control board or lower controller is broken.

CONFIGURATION:
                                                                                                                     21 of 52




CAUSE:
T h e c o n s o l e i s n o t i n s e r t e d t h e s a f e t y k e y, c a u s e t o c o n s o l e i s n o t f o r m a
+ 1 2 V ’s l o o p ( s a f e t y s w i t c h l o o p ) . S o , d i s p l a y w i l l b e a p p e a r e d “ E 0 ”.
But possibly main control wires or component of lower controller is broken.
(Because lower controller sent (+12V) signal via S/W of main control wire to
upper control board to form a safety switch loop.)

TROUBLESHOOTING:
Part                    Troubleshooting
                        Insert the safety key, and then use multi-meter transform into short circuit gear position to check safety
Safety module           module wires whether short or not.
                        Reinsert Main control wire.
Main control wires      Replace main control wire.

Note: Before check hardware, first check software setting.
R e m o v e s a f e t y k e y, p r e s s S T O P & S TA R T & E N T E R k e y s , a n d a t t h e s a m e t i m e
i n s e r t t h e s a f e t y k e y . T h e d i s p l a y i n t o “ E N G I N E E R I N G M O D E ”, P r e s s
F A S T / S L O W o r U P / D O W N k e y s , t o f i n d “ f u n c t i o n s ”, a n d p r e s s E n t e r k e y i n t o
“ D I S P L A Y M O D E ”, a n d t h e n p r e s s E n t e r k e y i n t o c h o o s i n g o n o r o f f .         When
c h o o s e “ o f f ”, t h i s i s m e a n d i s p l a y o f f a f t e r r e m o v e d s a f e t y k e y . W h e n
c h o o s e “o n ” w h i c h i s d i s p l a y o n a n d a p p e a r E 0 a f t e r r e m o v e d s a f e t y ke y.
                                                                                                                   22 of 52


8.2 Error Message: E1

DEFINITION:
Display board CPU did not receive the RPM signal. (Only happen in the
C a l i b r a t i o n . I n g e n e r a l l y, i t d o e s n o t n e c e s s a r y s p e e d R P M s e n s o r, b u t w h e n
t h e C a l i b r a t i o n w h i c h i t i s a n e c e s s a r y. )

CONFIGURATION:




CAUSE:
The motor doesn’t turn then E1 appears.
T h e d r i v e b o a r d d i d n o t s e n t v o l t a g e t o t h e m o t o r, s o t h e m o t o r d i d n o t
operate. And the display board did not receive the RPM sensor signal.
                            23 of 52

E1 SOLUTION FOLLOW CHART:
                                               24 of 52

E1 SOLUTION FOLLOW CHART – CHECK RPM SENSOR DEVICE
PROCEDURE:
25 of 52
                                                                                                                   26 of 52




CHECKING THE SPEED SENSOR:
1. Remove the motor cover hood.
2. The speed sensor is located on the left side of the frame, right next to
the front roller pulley (the pulley will have a belt around it that also goes
to the motor). The speed sensor is small and black with a wire connected to
it.
3. Make sure the sensor is as close as possible to the pulley without
t o u c h i n g i t . Yo u w i l l s e e a m a g n e t o n t h e f a c e o f t h e p u l l e y ; m a k e s u r e t h e
sensor is aligned with the magnet. There is a screw that holds the sensor in
p l a c e t h a t n e e d s t o b e l o o s e n e d t o a d j u s t t h e s e n s o r. R e - t i g h t e n t h e s c r e w
when finished.

TROUBLESHOOTING:
   E1      Possible cause                                            Things to check                         Solution
                  The upper console board hasn’t          check the speed sensor cable is in good   Make sure the good
                  received any speed signal for 8 seconds connection                                connection for cables
The motor         The speed sensor didn't detect signal   Check the gap between speed sensor and To keep the gap-distance less
cannot move       completely.                             magnet.                                than 3 mm.
                  Defective sensor or bad cable           Check if the sensor and cables are circuit Change the sensor or cables.
                  connection.                             short damaged.
27 of 52
                                                                                                                 28 of 52


8.3 Error Message: E2/OVER CURRENT

DEFINITION:
When the controller detects that the operating current for the drive motor
is above standard, the display will light up and show the message "E2." This
indicates that the controller needs to protect itself and the drive motor in
o r d e r t o p r e v e n t d a m a g e . T y p i c a l l y, t h i s i s d u e t o t h e r u n n i n g b e l t n e e d i n g
lubricate or its bottom fiber being worn seriously and requiring
replacement. A dried or worn running belt generates more friction between
itself and the running deck. The resulting high friction causes the controller
requires to provide more current for the drive motor to maintain speed.

TROUBLESHOOTING:
First, we recommend that users lubricate the bottom of the running belt
according to the instructions provided in the owner's manual. If this does
not resolve the issue, it may be due to excessive wear and tear on the
r u n n i n g b e l t , i n w h i c h c a s e r e p l a c e m e n t i s n e c e s s a r y. B y r e p l a c i n g t h e
running belt, the operating current for the drive motor will return to normal
levels.
If the E2 error still occurs after replacing the running belt, then either the
controller or the drive motor may be defective. Since the drive motor is a
p a ss i ve co mp o n ent , i t i s l e ss l i ke l y t o b e th e cau se o f t h e i s su e . T h erefo re ,
r e p l a c i n g t h e c o n t r o l l e r s h o u l d b e t h e f i r s t o p t i o n t o c o n s i d e r.




8.4 Error Message: E3
DEFINITION:
The console board is not detecting the VR voltage value, or the voltage
v a l u e h a s e x c e e d e d t h e r a n g e .” E 3 ” a p p e a r s o n t h e d i s p l a y .

CONFIGURATION:
                                                                                                                  29 of 52




CAUSE:
I n c l i n e V R r e s i s t o r v a l u e e x c e e d s t h e r a n g e . E 3 a p p e a r o n t h e d i s p l a y.
-The incline motor isn't operating up or down, causing the VR value to
exceed the range.
-After turning on the unit, the display board detects that the incline VR
voltage exceeds the range, and E3 appears.
-Action Flow Chart:




TROUBLESHOOTING:
Part      Troubleshooting
                           Press incline keys, see the display weather appear value or not.
Display board              If no values, please check keys weather keys stuck or not, or replace display board.
                                                                             30 of 52

                      -Inspect the wire connections.
Incline power cable
                      -Inspect whether wires are broken or crimped.
& incline VR cable    -Replace the wires and test again.

                      -Inspect whether the 5-PIN cable is connected well.
5-pin cable           -Test by replacing the cable with a good one.

Controller            Replace the controller.

                      -Inspect whether the incline motor is stuck.
                      -Inspect whether the incline gears are cracked.
Incline Motor         -Test whether the incline motor has a broke circuit.
                      -Recalibrate the incline set.
                                                             31 of 52

TEST CONFIGURATION:
The console to driver board connector pin define function.




Incline motor control function relate parts location.
                                                                                                                           32 of 52




TEST PROCEDURE:
1.Run calibration again.
2.Does the incline motor move at all?
3.If not, do the Up/down lights on the controller light?
4.If they light, do the relays click on?
◆If the relay clicks on but the motor does not move: with the incline light and relay activated check the voltage between the
neutral (white) wire and the Up (red) or down (black) wire, depending on which direction the motor is supposed to travel
according to Up/Down lights on the board. It should be about the same as the mains voltage ~ 110VAC (230VAC). If the voltage is
present but the motor doesn’t move, then the motor is bad.
◆If the light is on, but the relay does not click on then the controller needs to be replaced (Bad relay most likely).
5.If the motor moves, is there a sensor reading on console?
◆The INCLINE window will display the computer incline setting (after speed cal. ends); 15 for max incline, 0 for lowest incline.
The Incline window is a counter that is showing the actual position sensor output. If the motor is moving and there is no count
occurring in the Incline window, then there is a problem in the position sensor wiring or circuitry.
◆If there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings
(should not be able to rotate).
Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws
holding it to the motor casting.
If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the
potentiometer could be bad.
◆If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black and red wire and
                                                                                                                         33 of 52

there should be a voltage between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the
lowest position (the number isn’t too critical, as long as it’s somewhere in this neighborhood). If there is a voltage at the white
wire, and the voltage changes as the motor moves, but the counter still does not register then there may be a bad wire
connection between the potentiometer and the console.
6.Check the voltage from the potentiometer at the 3-pin connector on the controller. If there is no voltage, then the wire from
the motor to the connector is faulty.
7.If there is a voltage, check at the output connector to the console at the bottom of the controller. If no voltage present, then
there is a problem on the controller.
There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer
connector to the console connector.
The only problems that are possible are a bad solder joint or broken circuit on the board.
◆Console connector wiring, these connections are the same on the controller and at the console.
■Pin 1 = ground
■Pin 2 = position signal 0~5vdc
■Pin 3= 5vdc
8.If there is a voltage at the output connector to the console, then check the voltage at the console. If there is no voltage at
the console but there is a voltage at the controller, then check the entire cable from the controller to the console for cuts or
bad connections at the input wire connectors.
9.If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a problem
with the console.
                                                                                           34 of 52


8.5 Error Message: E4

DEFINITION:
M o t o r p o w e r w i r e e r r o r.

CONFIGURATION:




CAUSE:
P o w e r w i r e o f M o t o r d o e s n o t i n s e r t l o w e r c o n t r o l l e r.

TROUBLESHOOTING:
Part       Troubleshooting
Controller Insert power wire of motor.
Drive Motor             Replace Motor.
Display board           Replace upper control board.
                                                                                                                35 of 52


8.6 Error Message: E5

DEFINITION:
T h e c o m m u n i c a t i o n b e t w e e n t h e c o n s o l e a n d t h e c o n t r o l l e r i s p o o r. I t m a y
be due to a faulty main control wire, but it's also possible that either the
display board or the controller is malfunctioning.

CONFIGURATION:




CAUSE:
The main control wire is possibly broken. But E5 maybe has another
problem, like a component of the controller or console.

TROUBLESHOOTING:
Part                   Troubleshooting
Lower controller board Replace main control wire.
Main control wires            Reinsert or replace Main control wire.
Display board                 Replace display board.
                                                                                                                 36 of 52


8.7 Error Message: E6

DEFINITION:
The lower controller component is fault.

CONFIGURATION:




CAUSE:
T h e c o n t r o l l e r c o m p o n e n t i s f a u l t , L i ke Tra n s i s t o r 、 I G BT 、 c o n t r o l m o d u l e …
etc.

TROUBLESHOOTING:
Part         Troubleshooting
Controller                      Insert power wire of motor.
Display board                   Only Replace upper control board.
                      37 of 52


8.8 Circuit Diagram
38 of 52
                                                                                                           39 of 52


8.9 Calibration Procedure
STEP 1: After power on, the display shows the main screen as follows, touch
            the icon “          ” and enter the Settings page.




S T E P 2 : I n S E T T I N G S p a g e , t h e f i g u r e i s s h o w n a s b e l o w. C l i c k t h e w o r d o f
            “ S e t t i n g s ” m o r e t h a n 5 t i m e s i n a r o w t o e n t e r D E V I C E I N F O R M AT I O N
            page.
40 of 52
                                                                                                                 41 of 52



S T E P 3 : I n t h e D E V I C E I N F O R M AT I O N p a g e . C l i c k “                      ” to enter the
            p a g e o f C O N T R O L L E R I N F O R M AT I O N .




S T E P 4 : I n t h e C O N T R O L L E R I N F O R M AT I O N p a g e , y o u w i l l n o w b e a b l e t o s e t
            the display to show Metric or Imperial settings (Miles vs.
            K i l o m e t e r s ) . To d o t h i s , t o u c h t h e m e t r i c o r i m p e r i a l t o s h o w w h i c h

             y o u w a n t . To c l i c k a n d m a r k o n t h e i t e m “ ”, t h e n
             set the wheel diameter is 75 and set the maximum speed (if needed)
             to 12.0 mph and max incline to 30…etc.
                                                                                                                    42 of 52




STEP 5: Click “Check speed” button to start calibration. The process is
        automatic; the speed will start up without warning, so do not stand
        on the belt.

S T E P 6 : To c o m p l e t e t h e s p e e d a n d i n c l i n e c a l i b r a t i o n , c l i c k “ R e b o o t ” b u t t o n
            t o r e b o o t t h e d i s p l a y.
                                                                   43 of 52


9.Parts Replacing Guide
9.1 Replacing the Controller
Remove Motor cover and unplug all the controller wires. Then replace
Controller and plug all wires back.
                                                                                                                    44 of 52


9.2 Replacing the Console Assembly
STEP 1: Use Phillips head screwdriver to loosen the 8 Sheet Metal Screw
t h e n r e m o v e t h e U p r i g h t c o v e r.




STEP 2: Using an M6 L-Allen wrench to remove 4 bolts which securing the
console on the uprights.




S T E P 3 : D i s c o n n e c t a l l t h e c o n t r o l w i r e s t h e n r e p l a c e t h e c o n s o l e a s s e m b l y.
                                                                                                         45 of 52


9.3 Replacing the Drive Motor
S T E P 1 : L o o s e 5 M o t o r c o v e r l o c k i n g s c r e w s w i t h a s c r e w d r i v e r.




STEP 2: Unmount Drive motor ground wire and 2 input wires (black and red
wire.).




S T E P 3 : R e m o v e 4 D r i v e m o t o r L o c k i n g b o l t s w i t h a 1 4 m m T- t y p e s o c k e t
spanner and loose Drive belt.
Then do the reverse move to mount Drive motor back and 4 locking bolts but
do not secure.
                                                                                                                46 of 52

STEP 4: Adjust Drive belt tension with a 14mm open -end wrench. Measure
b e l t t e n s i o n w i t h a t e n s i o n m e t e r. T h e t e n s i o n n e e d s t o b e a b o u t 7 0 ~ 7 5 L B S .




STEP 5: Plug Drive motor 2 input wires to Controller (Red to M+ / Black to
M-) and mount ground wire.

9.4 Replacing the Breaker
Unplug Breaker wires to replace and plug wires back.




9.5 Replacing the AC Power Switch
Unplug AC Power switch wires to replace and plug wires back.
                                                                     47 of 52




9.6 Replacing the Front and Rear Roller
STEP 1: Remove both Adjustment base cover screws with a screwdriver then
take off them.




STEP 2: Remove 2 Rear Roller locking bolts with a M6 L -Allen wrench then
t a k e o f f R e a r R o l l e r.




STEP 3: Remove Drive motor cover then unmount Drive belt from Front
R o l l e r.
STEP 4: Remove Front Roller locking bolt with a 13mm wrench then take off
F r o n t R o l l e r.
STEP 5: Adjust Running belt to the center is necessary when installing Front
/ Rear Roller back.
48 of 52
                                                                                                           49 of 52


9.7 Replacing the Running Deck, Running belt, and
Cushions
STEP 1: Follow the 9.6 section to remove the front and rear rollers. Using a
screwdriver to remove the foot rail fixing screws on both sides. Then follow
the direction to side both foot rails out.




STEP 2: Remove 8 Running Deck locking screws then take off Running Deck.
N o w y o u c a n r e p l a c e R u n n i n g D e c k , R u n n i n g B e l t , a n d C u s h i o n s . To d o t h e
reverse steps to install them back.
STEP 3: Adjust Running belt tension and center it.
50 of 52
                                                                                             51 of 52


9.8 Replacing the Speed Sensor
Remove Motor cover then unplug Speed Sensor wire from Controller and
replace it.




9.9 Replacing the Incline Motor
S T E P 1 : Ta k e o f f M o t o r c o v e r.




STEP 2: Unplug Incline motor wires and unmount Incline motor from
treadmill.
S T E P 3 : To a d j u s t s p a r e I n c l i n e m o t o r t o l o w e r ( 2 2 5 m m ) .
                                                                                 52 of 52

STEP 4: Install Incline motor back with a 14mm open-end wrench and a M8
L-Allen wrench.




S T E P 5 : P l u g I n c l i n e m o t o r w i r e s t o C o n t r o l l e r.


=== OCR SUPPLEMENT, PDF PAGE 2 ===
<!-- render-vs-extraction: 156 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
2 of 52

-Contents-
DL. OU CI EM CS eee ceeeeeeeeeeeaaeeeeaeeceaeeecaaeeseaaeseaeecsaeeeeaaeceeaeeseaeeeesaeeeeaaeceeeeecsaeeseaaeeseaeeseseeeesaeeseaaeseeeeeeeas 3
ZL EPO CHE OME C PALES Le ccceeeeesteceesaeeeeaeeceeeeesaeceeaaeceeeeecsaeceeaaeceeaeeceaeeeesaeeeeaaeseeeeeseaeeseaaeeeeaeeseeeeees 4
ZB. Electrical CONF FUL ati ONS ci ccccccccssseecsesneeeceeseeeeceesseeecseseeeecseseeeeeseseeeeseseeeeeees 5
A PrOM UCHR O PEF ALL OM Liccccccccsssneecssseneeceesececeseeeeecseseeeecseeeeeecssseesecseseasecsseeeaecssseaaecseseeaeceseenaees 6
SB. Unt BLOCK Dia GLa MS  Liiccccccccssssecesssnecesseeecsseeeecesseeecseceeeeceeseesecsesessecssseaecseseaeesseeaaees 10
6. Basic CONNE|S CRI ONS ANNA|} WETS M G wiiccccccccsssceceeseccecesseececesseeeecssseeeecseseeeesseeeees 11
6.1 Display Board Wire CONN ES CLIONS Liiccccccccsssssccecessesessnaeeececsssesecseseeeeeeessesscseaeeeeseesees 11
6.2 Display Board PCB COMPONE| Nt LOCATIONS wicccccccccccssccccccessesesteceeeeecsssesscseeeeesessees 12
6.3 Driver Board Wire CONNECTIONS wiiecceseeesneceeseceeeeceeeeeeaeeeeaaeceeeeeceaeeeeaaeseeeeeneeeees 14
6.4 Driver Board PCB COMPONE| Nt LOCATIONS wiiccccccccssscccceceseesecseceeeeecsssesscseeeeeseesees 15
6.5 Driver Board FUNCTION wiiceeseceseeeesteeeesaeeeeaeeceeeeeeaeeeeaaecseaeeceaeeeeaaeceeaeeseeeeeseaeeeeaaeseeaeeseeeeees 15
6.6 Driver Board LED Indicator LOCATIONS wi ieececeseeesseeeeeeeceeeeeeeeeeeaeeeeaeeeeeeees 17
6.7 Controller Indicator LED AO DUG BING ecceccccccccccccssssssseeececeseesscsceeeeecessessesseeeeseesees 17
7. Product Safety LMSC UCT ONS wicccccccccsrcccssseneeceesenecesseneceseececssseeecsseeeessseaees 18
8.-Error Messages f/ Trou DIG SHO ODM G ccccccccccsccssscstscstscetsseesssesssesssessesees 19
Bi. L Error Me SSAGe|!E EO Lessscccececensseeseeeeeeeeeaeeeeeeeeeeeeeeeeeeeeeeeeeeeeeaeeeeeeeeeeeeeeeaaaeeeeeeeeeeaeaaaaeseeeeeeneea 20
Bi. 2 ErrOr MESS AGE|!?E ETL Lcsssssscscececensseesseeeeeeeeaeeeeseeeeeeeeaeeeeeeeeeeeeeeaeeeeeeeeeeeeaeaeeeeeeeeeeeeaeaaaeeeeeeeeeneaa 22
8.3 Error Message: E2Z/OVER CURRENT Qoiiiiccccscccsssceessecssssecsseeecsececsecesseecseeeesseeeeseceseeees 28
B.4 ErrOr MSS AGe|!E EB ciccccccccsssssscscececenesesseeeeeeeeeaeeeeeeeeeeeeeaeeeeeeeeeeeeeeeaeeeeeeeeeeeeeeeeeeeeeeeeeeeeeaeaaaaeeeeeeeeneea 28
B.5 ErrOr Me SSAaGe|!E EAS Licssssscscececeesseeeseeeeeeeeaeeseeeeeeeeeeeeeeeeeeeeeeeeeeaeeeeeeeeeeeeeeeaeaeeeeeeeeeeeaeaaaaeseeeeeeneaa 34
B. G6 ErrOr MSS AZ|? ED Licccccccsssssscscececeeesseeseeeeeeeeeaeeeeeeeeeeeeeaeeeeeeeeeeeeeeeaeeeeeeeeeeeeeseseaeaeeeeeeeeaaaaaaeeeeeeeeneaa 35
Bi. 7 ErrOr MSS AGe|S!E EG Liceecccccssssscscececeeeseeseeeceeeeeaeeeeeeeeeeeeeaeeeeeeeeeeeeeee ase eeeeeeeeeeeeeeeeseeeeeeeeeaaaaaaeeeeeeeeaeea 36
B.8 CIP CUIit Dia SPAM wicccccccccscscsceeeeeeeeeeeeeeeeeeeeeeeeececeeeceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeseseseeeeeseseeeeeseeeeeees 37
B.9 CalibratiON PrOCCAIULE Liieeccceeeesteceeseceeaeeceeeeeesaeeeeaaeceeaeeceaeeesaaeceeaaeseeeeeseaeeeesaeeseaeeeeeeeees 39
9. Parts Re pla cin F GUM COS i cccccsessceesenteeecseneececeeneceseeaeeeeseaeceeseaeeeeseaeeeeseaeeseseaas 43
9.1 Replacing the CONtolle ls ci cccccsssscccccessssessseeeeeecessesesseaeeeeecesseseeaeseesesessseseeaeaeseeseesees 43
9.2 Replacing the CONnsoOle ASSEMBLY wicccccccssssscccccecsssessseeececeseesesseseeeeeesssesseseseeeeseesees 44
9.3 Replacing the Drive MOt OP wiiccccccccsssscccccessssessnceceeececsescsseaeeeeecsseeseeseesesesssessaeaeseeseesees 45
9.4 Replacing the Break el wcccccccccsccsccccccsssessnsececccecccsessneeseeccssseseseeaeeesecsseeseeeseesesesssessesaeeeeseesees 46
9.5 Replacing the AC POWEr SWITCH wccccccccccsessssceeecessesesseeececsseeseeseseeeesesssesseeeseeeeseesees 46
9.6 Replacing the Front and Raf ROLIE|A ccccccccccccccccsesssssceececessesscsseeeeeesssesseseeeeeseesees 47
9.7 Replacing the Running Deck, Running belt, and Cushions.............. 49
9.8 Replacing the SPE SENS OL wrccccccccccsssssccecececeessnaeeecccsscesessaeeeeecesseseeseseeeeeessseseeeaeeeeseesees 51
9.9 Replacing the INCLINE MOCO cccccccccccccsccccccccsssessnseceeecsccesesnaeeececssseseeseaeeeeeesssesseaeaeseeseesees 51


=== OCR SUPPLEMENT, PDF PAGE 3 ===
<!-- render-vs-extraction: 58 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
J8P|OH Ped = 0Z (uy) 1y8udy

1243004 6T ()ausudn 6
Aay seqajpuey paeds = gt awesyauljou; 8
Aay Jeqajpuey auljou| = ZT (yu) 42pjOH eOG yUUQ «LZ
awelj ule) = 9T (1) 42P|OH eFM0G YUUG «9
(y) 4an0D JuUaWysNipyseay = ST Jayeadg =
(1) 42009 uaujsnipyseey PT uej,
(1) 429009 JOJOW=ys ET Josuas ajyesyesy SE
yeg Suluuny = ZT pegjooy 2
42A0} JOJO s«oTT gjosuoy—sdiT

eweN ‘ON sweN ‘ON

S9UI]INO'L

CS JOE


=== OCR SUPPLEMENT, PDF PAGE 4 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
4 of 52

2.Electronic Parts

CONSOLE

= Cooling Fan K)) Speaker

CONTROLLER AND DRIVER PARTS

Controller


=== OCR SUPPLEMENT, PDF PAGE 5 ===
<!-- render-vs-extraction: 80 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
5 of 52

3.Electrical Configurations

SAFETY KEY The safety key fits into the Console to activate all functions and treadmill. Without

safety key, console cannot be controlled, and treadmill will not be activated.

Console Interface that controls all functions of the treadmill.
Main The circuit board consists of the DC power supply for console ~ incline driver and
Controller DC motor driver, link the console to output appropriate voltages for motor that

control the treadmill functions.

Drive Motor This is a DC motor with variable speed. Control the 0 —90 (or 0-180) voltages

from the main controller to increase or decrease speed of the running belt.

Incline Motor This is an AC motor. User can control variable elevation by console within main

controller.

GENERAL INFORMATION

Console The console comprised of keys control and 15.6-inch screen display.
Main controller Include power supply + motor driver control circuit and incline

control circuit.

Drive Motor It’s a variable speed on 0-90 volt DC motor. (0-180 volts DC motor on 220Vac
electronic power system)
Have three wires red, black and green.
If there is DC voltage on the Red (white) wire (M+) the treadmill motor will turn
clockwise.
If there is DC voltage on the Black wire (M-) the treadmill motor will turn counter-
clockwise.
When the higher voltages, the speed is faster.

The green wire is grounding.

Incline Motor This is a 120 volt AC motor. (220 volts AC motor on 220Vac electronic power
system)
Have four wires, red, black, white, and green.
Has one 3 pins cable of position sensor.
If there is AC voltage on the red wire (UP) the incline motor will increase the
incline.
If there is AC voltage on the Black wire (DOWN) the incline motor will decrease the
incline.
The White wire (COM) is neutral.

The green wire is ground.


=== OCR SUPPLEMENT, PDF PAGE 6 ===
<!-- render-vs-extraction: 59 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
6 of 52

4.Product Operation

15.6” TOUCH SCREEN
GE b> DB fF © — & Annajohnson €] 10:23AM =

G 6 total workouts
1,275 mi total distance
12,356 calories
7:32

™ per mi avg pace this montigg

Set Timer
$ Training G) Media

WINDOW DISPLAY MODE

OFF Mode When user doesn’t insert the SAFETY KEY on the console, the treadmill enters the

OFF Mode, and the window will appear “PLEASE REPLACE THE SAFETY KEY”.

READY When the treadmill is ON and SAFETY KEY is inserted in console, the window will
Mode show programs name for choosing and quick start for tap to begin workout. Press

START button to start treadmill on Manual Mode.

SLEEP Mode In SLEEP Mode, if anyone button is pressed then the treadmill enters READY Mode.

RUN Mode In RUN Mode, pressing the “STOP” button and removing the SAFETY KEY will cause

the treadmill stop instantly and enter OFF Mode.


=== OCR SUPPLEMENT, PDF PAGE 7 ===
<!-- render-vs-extraction: 77 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
7 of 52

FUNCTION

SPEED Display the current speed in mile per hour (kilometer per hour).
DISPLAY range is 0.0 to 99.9.
WORK range is 0.5%12.0 mph (1.0 ~ 2.0 kmph)
Press “FAST” or “SLOW” to adjust speed, each increment and decrement is 0.1

km/h(mph).

INCLINE Display the incline position from 0 to 15.
DISPLAY range is 0 to 999.
WORK range is 0.0 to 15.0.
INCLINE preset value is 0.0.

Press “UP” or ”"DOWN” to adjust incline, each increment or decrement is 0.5.

TIME TIME is either COUNT UP or COUNT DOWN. System preset is COUNT UP; if user sets
the time, then timer is COUNT DOWN.
DISPLAY range is 0:00 to 999:99.
COUNT DOWN setup range is 10:00 to 99:00.
When TIME is set, the count will go to zero.
In RUN Mode, press “STOP” button to save value of time and enter “RUN Mode”

again that value will continue count time.

PACE It means: How long will takes to walk (or run) per each Km or Mile at current speed?
The unit is min/Km or min/Mi.
DISPLAY range is 00 : 00 to 99: 99.
WORK range is 00 : 00 to 99: 99,

DISTANCE Display the current distance in kilometer or Mile.
DISPLAY range is 0.00 to 99.99.
WORK range is 0.00 to 99.99.

CALORIES Displays the cumulative calories burned at any given time during your workout.
DISPLAY range is 0 to 999.
WORK range is 0 to 999.

PULSE Displays the heart rate beat by using hand pulse or receiver. When use receiver, a
chest belt must be worn.
DISPLAY range is 0 to 999.
WORK range is 50 to 200 BPM.
In RUN Mode, if the treadmill doesn’t have a signal for 8 seconds, then display value

will become “O ”.


=== OCR SUPPLEMENT, PDF PAGE 8 ===
<!-- render-vs-extraction: 61 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
8 of 52

FUNCTION BUTTON LOCATION

SPIRIT

Fan Key e_

Child Lock Key ®

Incline Quick Keys * : : __e Speed Quick Keys

Incline Up Key ®—__
__—® Speed Fast Key

Incline Down Key ® —® Speed Slow key

- STOP Key
START key® ~~ Safety Key
BUTTON FUNCTION IN EACH MODE
Ready Mode

Safety Key Set safety key in right position to power on the computer. When safety key
is pulled away from its position, the window will appear “PLEASE REPLACE
THE SAFETY KEY”.

Stop Key Non-functional.

Start Key Pressing “START” button to start treadmill, when pressing “START” button,
there will be 3 second final count down on window display, then machine
starts running. In MANUAL, treadmill starts at MIN SPEED and treadmill
starts at program preset value in PROGRAM.

Speed Fast Key If user doesn’t enter a setting, then this button is non-functional.

Speed Slow Key If user doesn’t enter a setting, then this button is non-functional.

Incline Up Key If user doesn’t enter a setting, then this button is non-functional.

Incline Down Key If user doesn’t enter a setting, then this button is non-functional.

Speed quick Keys Non-functional.

Incline quick Keys Non-functional.

Fan Switch It can control ON/OFF for the fan.

Child Lock Key When this in ENGINEERING MODE setting lock key ON that all keyboard
button no working, then MW will show the “HOLD CHILD LOCK BUTTON 3
SECONDS TO UNLOCK”. (On the IDLE MODE does not work after 5 minutes of
detection, the locked will ON.) if lock key off at ENGINEERING MODE

setting, that unit keyboard can working.

DISABLE Key To control ON/OFF for the handrail speed/incline switch.


=== OCR SUPPLEMENT, PDF PAGE 9 ===
<!-- render-vs-extraction: 45 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
9 of 52

Run Mode

Safety Key When safety key is pulled away from its position, the computer will be
automatically shut down.

Stop Key press “STOP” button to stop treadmill.

Start Key Non-functional.

Speed Fast Key Press the button to increase your speed and each increase is
0.1kph(0.1mph). If button is pressed continuously then speed increases to
MAX SPEED quickly.

Speed Slow Key Press the button to decrease your speed and each decrease is
0.1kph(0.1mph). If button is pressed continuously then speed decreases to
MIN SPEED quickly.

Incline Up Key Press the button to raise position and each increase is 0.5, the maximum
incline position is 15.

Incline Down Key Press the button to lower position and each decrease is 0.5, the minimum
incline position is 0.

Speed quick Keys Speed willsetto1°>2°3°4°5°6°7°8» 10> 12 speed quickly .
(Note: On 20.0kph spec is 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

Incline quick Keys Incline willsetto0°>1°2°4°>5°*6°8 10° 12> 15 position quickly.

Fan Switch It can control ON/OFF for the fan.

Child Lock Key Non-functional.

DISABLE Key To control ON/OFF for the handrail speed/incline switch.


=== OCR SUPPLEMENT, PDF PAGE 10 ===
<!-- render-vs-extraction: 28 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
10 of 52

5.Unit Block Diagrams

| , BLE /
ie ailaa ma 4 WIRELESS HR
RECEIVER
ret DISPLAY BOARD
2 SAFETY KEY

HR a %
HANDLEBAR
P| /|__ SPEAKER
| LR

4s

LINE IN CHARGING

INCLINE

CURRENT \ DRIVER BOARD MOTOR
BRAKER | ,

K VR SET

POWER
POWER =) SWITCH


=== OCR SUPPLEMENT, PDF PAGE 11 ===
<!-- render-vs-extraction: 25 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
Tl of 52

6.Basic Connections and Wiring

6.1 Display Board wire Connections

SPEED HANDRAIL WIRE

USB BOARD SOCKET

SPEAKER
SOCKET

KEYBOARD WIRE 5 ;

SOCKET tec
IF

SSL GEE

GROUNDING

HAND PULSE
WIRES SOCKET

COMPUTER CABLE SOCKET AUDIO OUTPUT
DC FAN SOCKET

SAFETY KEY WIRE SOCKET HR WIRELESS BOARD


=== OCR SUPPLEMENT, PDF PAGE 12 ===
<!-- render-vs-extraction: 23 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
; = —

. — Pio> Aen) SUG Sa ES tal
Ps00g3s03-S9EEXN ON Mt
SIEERIMG GI

M§AIA dOl GUYVOd dd

SUOIJEDO7] JUaUOdWOD godd pseog Aejdsigq z'9

cS $0 CL


=== OCR SUPPLEMENT, PDF PAGE 16 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
16 of 52

‘\
M— (To DC Motor)
WHITE or BLACK WIRE
POWER INPUT J
~
M+ (To DC Motor)
RED WIRE
Zz
( *)
WHITE WIRE (COM) OF THE VR SENSOR OF
INCLINE MOTOR POWER
L INCLINE
J
r
RED WIRE (UP) OF ‘
INCLINE MOTOR POWER SPEED SENSOR
. (RESERVE)
( y

BLACK WIRE (DOWN) OF

INCLINE MOTOR POWER
\

CONNECT TO CONSOLE


=== OCR SUPPLEMENT, PDF PAGE 17 ===
<!-- render-vs-extraction: 35 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
17 of 52

6.6 Driver Board LED Indicator Locations

POWER LED «

IT MUST BE CONNECT
CONSOLE AND SET SAFETY
KEY TO CHECK#

6.7 Controller Indicator LED debugging

Indicator . _
Function Condition Reason Solve
LED
POWER Controller If DC voltage is normal, it Voltage is not correct. Check the supply voltage is
Fuse is blown. 120Vac.
power would be always ON. Transformer is no good.(0n 220Vac electronic power
If off, fault condition system need 220Vac)

; Replace Fuse.
exists.
Replace controller.


=== OCR SUPPLEMENT, PDF PAGE 18 ===
<!-- render-vs-extraction: 187 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
18 of 52

7.Product Safety Instructions

Important Safety Instructions

- To reduce the risk of electric shock, disconnect your treadmill from the electrical outlet prior to
cleaning and/or service work.

- To reduce the risk of burns, fire, electric shock, or injury to persons, install the treadmill on a flat
level surface with access to a 220-volt, 10-amp grounded outlet with only the treadmill plugged into
the circuit. [120VAC electronic power system is 110-volt, 15-amp J

- Do not use an extension cord unless it is a 16 AWG or better with only one outlet on the end. Do not
attempt to disable the grounded plug by using improper adapters or in any way modify the cord outlet.

Important Electrical Instructions

- Never use a ground fault circuit interrupt (GFCI) wall outlet with this treadmill. As with any appliance
with a large motor, the GFCI will trip often. Route the power cord away from any moving part of the
treadmill including the elevation mechanism and transport wheels.

- Circuit Breakers: Some circuit breakers used in homes are not rated for high inrush currents that can
occur when a treadmill is first turned on or even during use. If your treadmill is tripping the house
circuit breaker (even though it is the proper current rating) but the circuit breaker on the treadmill
itself does not trip, you will need to replace the home breaker with a high inrush type. This is not a
warranty defect. This is a condition we as a manufacture have no ability to control. This part is
available through most electrical supply stores. Examples: Grainger part # 1D237, or available online at
www.squared.com part # QO120HM.

Important Grounding Instructions

- This product must be grounded. If the treadmill should malfunction or breakdown, grounding
provides a path of least resistance for electric current, reducing the risk of electric shock. This product
is equipped with a cord having an equipment-grounding plug. The plug must be plugged into an
appropriate outlet that is properly installed and grounded in accordance with all local codes and
ordinances.

L DANGER -| Improper connection of the equipment-grounding conductor can result in a risk of electric
shock. Check with a qualified electrician or serviceman if you are in doubt as to whether the product
is properly grounded. Do not modify the plug provided with the product if it will not fit the outlet;
have a proper outlet installed by a qualified electrician. This product is for use on a nominal 220-volt
(on 120VAC electronic power system need 110VAC) circuit and has a grounding plug that looks like the
plug illustrated below. A temporary adapter that looks like the adapter illustrated below may be used
to connect this plug to a 2-pole receptacle as shown below if a properly grounded outlet is not
available. The temporary adapter should be used only until a properly grounded outlet, (shown below)
can be installed by a qualified electrician. The green colored rigid earplugs, or the like, extending from
the adapter, must be connected to a permanent ground such as a properly grounded outlet box cover.
Whenever the adapter is used, it must be held in place by a metal screw.

Adapter
Grounded Outlet

NN tab of

(10) “TA Metal Screw Grounding
Bh Screw

Grounding Pin \ rounded Outlet Box


=== OCR SUPPLEMENT, PDF PAGE 19 ===
<!-- render-vs-extraction: 38 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
19 of 52

8.Error Messages / Troubleshooting

ERROR CODE LIST

Code Description
EO The display appears PLEASE REPLACE THE SAFETY KEY. It means safety

key is removed.

E1 Display board CPU did not receive the RPM signal. (only calibration)
E2 Treadmill motor is over current.
E3 The console board is not detecting the VR voltage value, or the

voltage value has exceeded the range.

E4 Treadmill motor wires or volt possible abnormal.
E5 Communication single is abnormal.
E6 Lower Control board possible broken.

TOOLS REQUIRED

A multi-meter.


=== OCR SUPPLEMENT, PDF PAGE 20 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
20 of 52

8.1 Error Message: EO

PLEASE REPLACE THE SAFETY KEY

DEFINITION:
Console is not inserted safety, or safety module may be broken. Or else
component of upper control board or lower controller is broken.

CONFIGURATION:


=== OCR SUPPLEMENT, PDF PAGE 21 ===
<!-- render-vs-extraction: 57 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
21 of 52

Pre SSSSe 1
| |
|
SAFETY KEY
ice SGA |
. . f |
CONSOLE 74 ae - nen
DISPLAY BOARD Kp SAREIN REY | |

ras
4/™
JEAN

MOTOR SPEED
SIGNAL

y

MOTOR

VOLTAGE

\ VE 20N) 3S MOTOR
AC POWER | ) DRIVER BOARD ee

CAUSE:

The console is not inserted the safety key, cause to console is not form a
+12V’s loop (safety switch loop). So, display will be appeared “EO”.

But possibly main control wires or component of lower controller is broken.
(Because lower controller sent (+12V) signal via S/W of main control wire to
upper control board to form a safety switch loop.)

TROUBLESHOOTING:

Part Troubleshooting

Insert the safety key, and then use multi-meter transform into short circuit gear position to check safety

Safety module module wires whether short or not.

Reinsert Main control wire.

Main control wires ; .
Replace main control wire.

Note: Before check hardware, first check software setting.

Remove safety key, press STOP & START & ENTER keys, and at the same time
insert the safety key. The display into “ENGINEERING MODE”, Press
FAST/SLOW or UP/DOWN keys, to find “functions”, and press Enter key into
“DISPLAY MODE”, and then press Enter key into choosing on or off. When
choose “off”, this is mean display off after removed safety key. When
choose “on” which is display on and appear EO after removed safety key.


=== OCR SUPPLEMENT, PDF PAGE 22 ===
<!-- render-vs-extraction: 31 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
22 of 52
8.2 Error Message: El

DEFINITION:

Display board CPU did not receive the RPM signal. (Only happen in the
Calibration. In generally, it does not necessary speed RPM sensor, but when
the Calibration which it is a necessary.)

CONFIGURATION:

CONSOLE
DISPLAY BOARD

A: NX
Send and receive speed
a 2 RPM SENSOR MOTOR SPEED
signal via TX/RX of SIGNAL SIGNAL
5-pin Main wire. + v

NX
FR MOTOR
L7
AC POWER [= >) DRIVER BOARD
ae
A__ RPM
-—™=—| SENSOR

CAUSE:

The motor doesn’t turn then El appears.

The drive board did not sent voltage to the motor, so the motor did not
operate. And the display board did not receive the RPM sensor signal.


=== OCR SUPPLEMENT, PDF PAGE 23 ===
<!-- render-vs-extraction: 68 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
E1 SOLUTION FOLLOW CHART:

El showing up — Reset power L—»

Press start again

Replace upper console board or
update the program of upper
console board

Check display whether Countdown
or not after pressing start?

Did belt moves after
start?

‘ >| Replace lower control driver board

Check lower control
driver board weather
enough Power?
(AC: 2207)

Use multi-meter to
Check Wain control line
socket pin2 & pind is
DC12V)

Check power source from wall weather
stable AC220V or not?

Then, press start and
use multi-meter to
Check driver board

notor socket weather

voltage or not?

NO

Vv

Check main control line
whether split or not?

Check RPM sensor
whether well or not?

23 of 52

Adjust sensor gap distance to 2nm.

Did belt moves after
start?

YES

Replace Motor

>

Solve the problem

Replace main
control line
Replace RPM
sensor
Vv v


=== OCR SUPPLEMENT, PDF PAGE 25 ===
<!-- render-vs-extraction: 24 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
25 of 52

Check RPM sensor

YES

¥

Move the roller so
that meegent closest
to the scnsur

YES

com:down ts function ss rebtern feces

OK?

NO

Replace Consale


=== OCR SUPPLEMENT, PDF PAGE 26 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
26 of 52

Reed switch RPM
speed sensor device

CHECKING THE SPEED SENSOR:

1. Remove the motor cover hood.

2. The speed sensor is located on the left side of the frame, right next to
the front roller pulley (the pulley will have a belt around it that also goes
to the motor). The speed sensor is small and black with a wire connected to
it.

3. Make sure the sensor is as close as possible to the pulley without
touching it. You will see a magnet on the face of the pulley; make sure the
sensor is aligned with the magnet. There is a screw that holds the sensor in
place that needs to be loosened to adjust the sensor. Re-tighten the screw
when finished.

TROUBLESHOOTING:

E1 Possible cause Things to check Solution
The upper console board hasn’t check the speed sensor cable is in good |Make sure the good
received any speed signal for 8 seconds |connection connection for cables
The motor The speed sensor didn't detect signal |Check the gap between speed sensor and|To keep the gap-distance less;
cannot move = _ Completely. magnet. than 3 mm.
Defective sensor or bad cable Check if the sensor and cables are circuit |Change the sensor or cables.
connection. Short damaged.

Speed Sensor = ;

Motor (red
wire) M+

DRIVER MOTOR

! Motor (black wire) iy
M-


=== OCR SUPPLEMENT, PDF PAGE 28 ===
<!-- render-vs-extraction: 22 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
28 of 52

8.3 Error Message: E2/OVER CURRENT

DEFINITION:

When the controller detects that the operating current for the drive motor
is above standard, the display will light up and show the message "E2." This
indicates that the controller needs to protect itself and the drive motor in
order to prevent damage. Typically, this is due to the running belt needing
lubricate or its bottom fiber being worn seriously and requiring
replacement. A dried or worn running belt generates more friction between
itself and the running deck. The resulting high friction causes the controller
requires to provide more current for the drive motor to maintain speed.

TROUBLESHOOTING:

First, we recommend that users lubricate the bottom of the running belt
according to the instructions provided in the owner's manual. If this does
not resolve the issue, it may be due to excessive wear and tear on the
running belt, in which case replacement is necessary. By replacing the
running belt, the operating current for the drive motor will return to normal
levels.

If the E2 error still occurs after replacing the running belt, then either the
controller or the drive motor may be defective. Since the drive motor is a
passive component, it is less likely to be the cause of the issue. Therefore,
replacing the controller should be the first option to consider.

8.4 Error Message: E3

DEFINITION:
The console board is not detecting the VR voltage value, or the voltage
value has exceeded the range.” E3” appears on the display.

CONFIGURATION:


=== OCR SUPPLEMENT, PDF PAGE 29 ===
<!-- render-vs-extraction: 13 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
29 of 52

DISPLAY BOARD

. The incline VR
ape single via TX/RX of
VOLTAGE Main control wire
send and receive.

INCLINE
MOTOR

DRIVER BOARD == VR VOLTAGE | INCLINE VR SET

CAUSE:

Incline VR resistor value exceeds the range. E3 appear on the display.
-The incline motor isn't operating up or down, causing the VR value to
exceed the range.

-After turning on the unit, the display board detects that the incline VR
voltage exceeds the range, and E3 appears.

-Action Flow Chart:

TROUBLESHOOTING:

Part Troubleshooting

Press incline keys, see the display weather appear value or not.
If no values, please check keys weather keys stuck or not, or replace display board.

Display board


=== OCR SUPPLEMENT, PDF PAGE 32 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
32 of 52

The position sensor wires:
Black = Ground, +
White = Position signal,
Red = 5vdc, «

(0~5v depending on incline position)“

WHITE-NEUTRAL«

RED-UP«

BLACK-DOWN=

TEST PROCEDURE:

1.Run calibration again.

2.Does the incline motor move at all?

3.If not, do the Up/down lights on the controller light?

4.If they light, do the relays click on?

@ If the relay clicks on but the motor does not move: with the incline light and relay activated check the voltage between the
neutral (white) wire and the Up (red) or down (black) wire, depending on which direction the motor is supposed to travel
according to Up/Down lights on the board. It should be about the same as the mains voltage ~ 110VAC (230VAC). If the voltage is
present but the motor doesn’t move, then the motor is bad.

lf the light is on, but the relay does not click on then the controller needs to be replaced (Bad relay most likely).

5.If the motor moves, is there a sensor reading on console?

@The INCLINE window will display the computer incline setting (after speed cal. ends); 15 for max incline, O for lowest incline.
The Incline window is a counter that is showing the actual position sensor output. If the motor is moving and there is no count
occurring in the Incline window, then there is a problem in the position sensor wiring or circuitry.

@\f there is a count, but the calibration fails then the position sensor (Potentiometer) could be loose, creating false readings
(should not be able to rotate).

Remove the cover from the rear of the motor and grab the potentiometer and see if it is loose. Check the two Phillips screws
holding it to the motor casting.

If it still feels loose the nut holding the potentiometer to its black mounting bracket could be loose. If everything is tight then the
potentiometer could be bad.

@ If there is no count then check the voltage at the potentiometer. There should be 5vdc between the black and red wire and


=== OCR SUPPLEMENT, PDF PAGE 33 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
33 of 52

there should be a voltage between the red and white wire. This voltage will be about 4.5~4.7 Vdc when the motor is at the
lowest position (the number isn’t too critical, as long as it’s somewhere in this neighborhood). If there is a voltage at the white
wire, and the voltage changes as the motor moves, but the counter still does not register then there may be a bad wire
connection between the potentiometer and the console.

6.Check the voltage from the potentiometer at the 3-pin connector on the controller. If there is no voltage, then the wire from
the motor to the connector is faulty.

7.1f there is a voltage, check at the output connector to the console at the bottom of the controller. If no voltage present, then
there is a problem on the controller.

There are no electronic components on the board for this signal; there are just circuit connections from the potentiometer
connector to the console connector.

The only problems that are possible are a bad solder joint or broken circuit on the board.

@Console connector wiring, these connections are the same on the controller and at the console.

WiPin 1 = ground

BiPin 2 = position signal O~S5vdc

BBPin 3= 5vdc

8.If there is a voltage at the output connector to the console, then check the voltage at the console. If there is no voltage at
the console but there is a voltage at the controller, then check the entire cable from the controller to the console for cuts or
bad connections at the input wire connectors.

9.If there is voltage at the console connector, but no count in Incline window when motor is moving then there is a problem

with the console.


=== OCR SUPPLEMENT, PDF PAGE 34 ===
<!-- render-vs-extraction: 18 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
34 of 52

8.5 Error Message: E4

DEFINITION:
Motor power wire error.

CONFIGURATION:

DISPLAY BOARD

4

The signal
RPM or via TX/ RX Send
Motor of Main command of
signal control wire+ start or speed
return - signal _«

MOTOR

Power of Motor+-
DRIVER BOARD

VA

CAUSE:
Power wire of Motor does not insert lower controller.

TROUBLESHOOTING:

Part Troubleshooting
Controller Insert power wire of motor.
Drive Motor Replace Motor.

Display board Replace upper control board.


=== OCR SUPPLEMENT, PDF PAGE 35 ===
<!-- render-vs-extraction: 7 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
35 of 52

8.6 Error Message: E5

DEFINITION:

The communication between the console and the controller is poor. It may
be due to a faulty main control wire, but it's also possible that either the
display board or the controller is malfunctioning.

CONFIGURATION:

Console

Signal via main
control wire to
communication.

Lower controller

CAUSE:
The main control wire is possibly broken. But E5 maybe has another
problem, like a component of the controller or console.

TROUBLESHOOTING:
Part Troubleshooting
Lower controller board Replace main control wire.

Main control wires Reinsert or replace Main control wire.

Display board Replace display board.


=== OCR SUPPLEMENT, PDF PAGE 36 ===
<!-- render-vs-extraction: 10 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
36 of 52

8.7 Error Message: E6

DEFINITION:
The lower controller component is fault.

CONFIGURATION:

Console

Signal via main
control wire to
communication.

Lower controller

CAUSE:
The controller component is fault, Like Transistor +» IGBT + control module:::
etc.

TROUBLESHOOTING:
Part Troubleshooting

Controller Insert power wire of motor.

Display board Only Replace upper control board.


=== OCR SUPPLEMENT, PDF PAGE 37 ===
<!-- render-vs-extraction: 55 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
37 of 52

8.8 Circuit Diagram

#XT816-NT052 TREADMILL SCHEMATIC
CONSOLE

5 PIN COMPUTER CABLE

~\/

INPUT POWER

...

Q CONNECTOR “\/

BREAKER | | 5 PIN COMPUTER CABLE DEFINE
7
INLE Oo To ew

1 1 } 00 2—t— vop
BLACK WIRE 3——_ TXD

WHITE WIRE ,—— Be Wy

FILTER a.

oe INCLINE
= MOTOR

0 ACL NY

WHITE WIRE cine 3 PIN VR CABLE zZ w

BLACK WIRE a
o colle RED WIRE =
AC pack wire L |_ACN | CONTROLLER |com WHITE WIRE 3 5

wT oC ao
ACL a tu

0
M4) M-l  sEnsor | yk 44 = 5

FAN

pc . RED WIRE wo
MOTOR

WHITE WIRE

SPEED SENSOR SENSOR

orouno NG


=== OCR SUPPLEMENT, PDF PAGE 39 ===
<!-- render-vs-extraction: 59 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
39 of 52

8.9 Calibration Procedure

STEP 1: After power on, the display shows the main screen as follows, touch

the icon « @» and enter the Settings page.
Enh BG BR © @ Guest €] 02:36PM =

Hello, Guest!

Please provide your age and weight
to get a more accurate workout
summary.

we — 35 +

Weight |b — 1 55 a
Set Timer

All Programs >

& Training @) Media

STEP 2: In SETTINGS page, the figure is shown as below. Click the word of
“Settings” more than 5 times in a row to enter DEVICE INFORMATION

page.

Settings x

Units Child Lock Sleep Mode

Screen Brightness

Date & Time > WiFi > Language >
May 9, 2023, 02:37 PM Wifi-VIP_guest English
Software v2.0 Media Apps Passcode >


=== OCR SUPPLEMENT, PDF PAGE 41 ===
<!-- render-vs-extraction: 40 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
41 of 52

CONTROLLER
STEP 3: In the DEVICE INFORMATION page. Click “ ” to enter the
page of CONTROLLER INFORMATION.
€ Back
DEVICE INFO CONTROLLER
MIN SPEED MAX SPEED MIN INCLINE MAX INCLINE
0.5 mph 12.0 mph oO % 15 *%
Rom version: C5A28V12 Total distance: 0.0mi
Set reminder to refuel time: 90 hours

STEP 4: In the CONTROLLER INFORMATION page, you will now be able to set
the display to show Metric or Imperial settings (Miles vs.
Kilometers). To do this, touch the metric or imperial to show which

g Start calibrating speed?
you want. To click and mark on the item “ ”, then
set the wheel diameter is 75 and set the maximum speed (if needed)
to 12.0 mph and max incline to 30..etc.


=== OCR SUPPLEMENT, PDF PAGE 42 ===
<!-- render-vs-extraction: 37 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
42 of 52

€ Back
DEVICE INFO CONTROLLER
Units Metric ee
WHEEL DIAMETER 2? TORQUE VALUE 7? PWM START o PWM SEGMENTATION 7
60 50 1080 1007
MIN SPEED MAX SPEED o MAX INCLINE o
0.5 mph 12.0 mph 30 %

g Start calibrating speed? Check speed ROM Reset Factory

STEP 5: Click “Check speed” button to start calibration. The process is
automatic; the speed will start up without warning, so do not stand
on the belt.

STEP 6: To complete the speed and incline calibration, click “Reboot” button
to reboot the display.

W Speed calibration successfully!

Incline low point Incline high point

18 206


=== OCR SUPPLEMENT, PDF PAGE 45 ===
<!-- render-vs-extraction: 12 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
45 of 52

9.3 Replacing the Drive Motor

STEP 1: Loose 5 Motor cover locking screws with a screwdriver.

STEP 2: Unmount Drive motor ground wire and 2 input wires (black and red
wire.).

ITT I]
1 fj

= Oo ——

L__/

oy = -—}

STEP 3: Remove 4 Drive motor Locking bolts with a 14mm T-type socket
spanner and loose Drive belt.

Then do the reverse move to mount Drive motor back and 4 locking bolts but
do not secure.


=== OCR SUPPLEMENT, PDF PAGE 46 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
46 of 52

STEP 4: Adjust Drive belt tension with a 14mm open-end wrench. Measure
belt tension with a tension meter. The tension needs to be about 70~75LBS.

STEP 5: Plug Drive motor 2 input wires to Controller (Red to M+ / Black to
M-) and mount ground wire.

9.4 Replacing the Breaker

Unplug Breaker wires to replace and plug wires back.

9.5 Replacing the AC Power Switch

Unplug AC Power switch wires to replace and plug wires back.


=== OCR SUPPLEMENT, PDF PAGE 49 ===
<!-- render-vs-extraction: 5 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
49 of 52

9.7 Replacing the Running Deck, Running belt, and
Cushions

STEP 1: Follow the 9.6 section to remove the front and rear rollers. Using a
screwdriver to remove the foot rail fixing screws on both sides. Then follow
the direction to side both foot rails out.

STEP 2: Remove 8 Running Deck locking screws then take off Running Deck.
Now you can replace Running Deck, Running Belt, and Cushions. To do the
reverse steps to install them back.

STEP 3: Adjust Running belt tension and center it.


=== OCR SUPPLEMENT, PDF PAGE 51 ===
<!-- render-vs-extraction: 6 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
51 of 52

9.8 Replacing the Speed Sensor
Remove Motor cover then unplug Speed Sensor wire from Controller and
replace it.

9.9 Replacing the Incline Motor
STEP 1: Take off Motor cover.

STEP 2: Unplug Incline motor wires and unmount Incline motor from
treadmill.
STEP 3: To adjust spare Incline motor to lower (225mm).


=== OCR SUPPLEMENT, PDF PAGE 52 ===
<!-- render-vs-extraction: 14 words the text layer does not have; tesseract --psm 4 at 300 dpi -->
52 of 52

STEP 4: Install Incline motor back with a 14mm open-end wrench and a M8

L-Allen wrench.

sa

Red wire connects to UP port.< IY

NS _ “ S White wire connects to COM port.< G/ (oe

Black wire connects to Down port.<
