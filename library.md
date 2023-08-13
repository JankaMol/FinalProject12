Knihovna s panelem správce
Stručný popis systému
V rámci projektu vytvoříme aplikaci, která bude mít funkci knihovny - umožní přidávat 
knížky prostřednictvím administrativního panelu, umožní registraci a přihlašování 
uživatelů a zadávání jejich objednávek + hodnocení knih.
Hlavní funkce systému
Přihlašovací panel.
Admin: 
* Přidávání kategorií pro žánry.
* Přidávání knih.
* Seznam knih.
Uživatel - čtenář:
* Registrace.
* Vyhledávání knih dle abecedy, autora, žánru.
* Možnost objednávky knih.
* Zobrazení již půjčených knih pro uživatele.
* Hlídání dostupnosti knihy.
* [Prodloužení registrace (není-li rezervováno)].
Uživatel - knihovník:
* Přidání/odebrání knihy ze seznamu.
* Obnovení registrace
* Potvrzení úhrady pokuty
Obecné pokyny
Tvorba webové knihovny pomocí Djanga.
Základní subjekty (návrh)
Žánry
• Název
Uživatelský účet
• přihlášení (e-mail)
• heslo (hash)
• adresa (země, město, ulice, PSČ)
• role (ADMIN/USER - entita)
• seznam vypůjčených knih
• Datum výpůjčky
• Datum registrace
Knihy
• Název (+ originální název)
• Žánr
• Rok vydání
• Jazyk
• Autor
• Obrázek
• Status (vypůjčeno)
• Popis
• Hodnocení + komentáře
• Počet stran
• ISBN
• Počet kusů
Objednávkový řádek
• Kniha
• Počet knih
• Doba výpůjčky (u každé knihy zvlášť)
Objednávka
• Uživatelské jméno
• Datum podání
• Řádky objednávky
• Stav (výčet)
Autor
• Jméno
• Příjmení
• Datum narození
• Národnost
• Seznam knih
• Biografie
Role
• Název role
• Výpis funkcí
Košík
• Objednávkové řádky
Funkce
ADMIN: Přidání knihy, žánru či autora, 
Knihovník
vrácení knihy (navýšení počtu kusů)
Přidání produktu
• Název
• Dostupnost
• Kategorie
• Autor
Objednávka
• Seznam knih
• Tlačítko přidat/odebrat
• Hledání knih/autorů
Uživatel:
Uživatelská registrace
• Vložit osobní údaje
Přihlášení
• Přihlášení
• [Zrušení účtu]
• Odhlášení
Seznam knih, autorů
• Dle data přidání knihy/žánru/autora
• Třídit dle žánru/autora
• Vyhledávání dle názvu (CZ, originál)
• ISBN
• Datum vydání
• [Dle věkové kategorie]
• Dle jazyka knihy
Košík
• Zobrazení produktů přidaných do košíku
• Možnost objednávat produkty -> poděkování za objednávku a snížení
dostupnosti produktu
• Číslo rezervace
• Datum výpůjčky (28 dní od vypůjčení)
Další rozšíření
• Úprava uživatelského účtu (uživatelem)
• Přehled uživatelských objednávek (uživatel - jen svoje, i administrátor - vše)
• Přehled půjčovaných knih a autorů (administrátor)
• Přehled uživatelů (admin)
• [Propadlá výpůjčka – pokuta dle délky prodlení + upozornění (admin)]
• [Propadlá registra]