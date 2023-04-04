# 1. Jelenlegi Helyzet
Számos szoftver és megoldás érhető el jelenleg az online e-learning weboldalak területén, amelyek segíthetik az oktatási folyamatot, mint például a Moodle, a Blackboard, a Google Classroom és az Edmodo.
Azonban nincs olyan weboldal, amely az oktatási intézményünk specifikus igényeit és követelményeit figyelembe véve biztosítaná az oktatási anyagok, tesztek és kurzusok hatékony kezelését, valamint a diákok és tanárok közötti kommunikációt.

# 2. Képernyőtervek

# 3. Fogalomszótár
E-learning: Az az oktatási forma, amely digitális eszközöket alkalmaz a tananyag feldolgozásához, bemutatásához és a kommunikációhoz.
Weboldal: Egy olyan elektronikus dokumentum, amelyet a World Wide Web számára készítettek el, és amelyet a böngészők képesek megjeleníteni.
Platform: Az a számítástechnikai környezet, amely lehetővé teszi, hogy bizonyos programok futtathatók legyenek egy számítógépen.
Nyílt forráskódú: A számítógépes program, amelynek forráskódja nyilvánosan hozzáférhető, és szabadon használható, másolható, terjeszthető, tanulmányozható és módosítható.
Kurzus: Az a tanfolyam, amely keretet biztosít a hallgatók számára, hogy meghatározott rend szerint (pl. előadás, gyakorlat, házi feladat stb.) sajátítsák el a tudást, és arról számot is adnak.
Hallgató: Olyan személy, aki egyetemi vagy főiskolai tanulmányokat folytat egy bizonyos karokon, és meghatározott kurzusokat teljesít, hogy szakmai tudását bővítse.
Zárthelyi dolgozat: A zárthelyi dolgozat egy olyan írásbeli vizsga, amelyet általában az egyetemi félév végén vagy a tananyag egy adott részénél írnak a hallgatók. A dolgozat általában a tanult anyagot foglalja össze, és általában a tanár értékelése befolyásolja a hallgatók jegyét.


# 4. Forgatókönyvek
Regisztráció: Az e-learning felület megnyitása után a kezdőlapon található regisztráció gombra kattintva tudunk regisztrálni. Ez után megadhatjuk a szükséges adatokat, valamint kiválaszthatjuk, hogy oktatóként vagy tanulóként kívánunk regisztrálni. A regisztráció gombra kattintva a kezdőlap jelenik meg, amennyiben helyes adatokat adtunk meg.

Bejelentkezés: Az e-learning oldal megnyitása után a navigációs sávon a bejelentkezés gomb használatával tudunk a korábban már létrehozott fiókunkba belépni. A bejelentkezés gombra kattintva megadhatjuk felhasználónevünk, valamint jelszavunk. Helyes adatokat megadva és a Bejelentkezés gombra kattintva a fiókunkba lépünk be.

Tananyagok kezelése oktatóként: Tanár jogosultságú felhasználóval bejelentkezve, a tananyagok menüpontban lehetőségünk van új tananyagokat létrehozni és meglévő, általunk létrehozott tananyagokat átírni,szerkeszteni.

Tesztek kezelése tanulóként: tanuló felhasználóval bejelentkezve a tesztek menüpontban azon tananyagok tesztjeit/kérdéseit nézhetjük meg és oldhatjuk meg, amelyekhez korábban hozzáférést kaptunk.

Tesztek kezelése oktatóként: oktató fiókba bejelentkezve, az általunk létrehozott tananyagokhoz lehetőségünk van tesztek/kérdések feltöltésére, a tesztek menüpontban.


# 5. Használati esetek
1. Egy kívül álló az oldalra téved. Rövid tájékoztatót kap arról mi is ez az oldal.
2. Egy tanár létrehoz egy kurzust.
3. Egy diák létrehoz egy kurzust, tanuló szoba céljából.
4. Egy diák bejelentkezik egy kurzusra, amihez hozzáférést kap miután a tulajdonosa jóvá hagyta.
5. Egy kurzus tulajdonos tananyagot töltfel.
6. Egy kurzus tulajdonos _zárthelyit_ hírdet.
7. Egy diák kitölt egy _zárthelyit_.

# 6. Jelenlegi üzleti folyamatok
Az egyetem egy elearning rendszert megrendelt, amely képes megállni a helyét a szélesebb körben elterjedt rendszerekkel szemben. A forrása a megrendelőt illeti majd, és mivel igényt tartanak a tovább fejlesztésre, bővythetőnek kell lennie. Elvárás az, hogy a kód bázis egyszerűen felhasználható legyen, hiszen az oldal működtetésére nem nekünk kell majd felkészülni, hanem a megrendelő moderálási pozíciókba olyan embereket terveznek kinevezni, akik nem rendelkeznek programozói háttérrel. Minden felmerülő CRUD műveletre biztosítanunk kell felhasználó barát grafikus felületet.
A projekt teljesítésére 2 hónap áll majd rendelkezésre.

# 7. Igényelt üzleti folyamatok
Az e-learning rendszerben három kölönböző belentkezési felület lesz elérhető : adminisztrátor, tanár és diák. Az alkalmazásunk a követelmény listában feltüntetett funkcionális és nem funkcionális követelményeknek megfelelően fog létrejönni. Az adminisztrátoroknak és tanároknak biztosítunk egy regisztrációs felületet, a diákokat az intézménybe való jelentkezésük és személyes adataik felhasználásával vesszük fel a rendszerbe. A felhasználókat szerepkörük alapján csoportosítjuk.

# 8. Vágyálomrendszer

A projekt célja egy webes tanulásszervezési rendszer, ahol az elérhető funkciók felhasználói kategóriánként eltérőek, például egy diák számára más funkciók elérhetőek mint egy tanár számára, ezért a funkciók csak sikeres regisztráció és bejelentkezés után használhatóak.

Az alap felhasználókon felül kell egy magasabb rendű felhasználó, egy adminisztrátor, aki teljes hozzáféréssel rendelkezik a rendszerben. Az esetleges hibákat neki jelzik a felhasználók. Az admin korlátlanul módosíthatja, törölheti bármelyik kurzust valamint a felhasználók adatait is módosíthatja vagy adhat hozzá új felhasználót. A többi felhasználó jelentkezhet a kurzusokra de nem módosíthatja azt, csak a sajátjait.

Adminisztrátori vagy tanári jogosultsági szinttel a felhasználók létrehozhatnak kurzusokat amelyekben tananyagokat, teszteket, feladatokat tölthetnek fel. A kurzusok létrehozása során, készíthetnek komplexebb vagy szimplább kurzusokat, függően attól, hogy milyen céllal, milyen témával fog rendelkezni.
