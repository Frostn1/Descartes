# Descartes
עיצבנו שפת תכנות שלוקחת עד הסוף את הקטע של מבני נתונים אלגבריים, וכמעט כל דבר בה הוא מכפלה קרטזית, ולכן שמה בישראל Descartes (מבוטא ״זה קל״, כדי להטעות את העוברים ושבים)
תכונה מעניינת של זהקל: שם של מבנה נתונים בלי פרמטרים הוא map על האפשרויות בו, למשל:
#if:
BoardCoords = 0..9 * 0..19
# then:
BoardCoords (a * b -> less_than a 5)
# gives a 2d array of Booleans where the first 5 columns are all True and the rest are all False
הפעולה / היא reduce
אז ככה סוכמים את המספרים מאחד עד עשר:
add * 0 / 1..10
וככה סוכמים את הריבועים שלהם:
add * 0 / 1..10 (x -> mul x x)



