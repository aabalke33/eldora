# Parser Concept

Biggest problem is tesseract has trouble breaking down tables

Steps
1. Use ML to Classify form type (ie. W2 Form type A, type B etc)
2. Use template of how to chop up Type A form to chop image up
3. From chopped up image extract individual values (ie. Wages)
4. Append Indiviual Values to Json file
