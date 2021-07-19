# -*- coding: UTF-8 -*-

from lxml import etree
judge1_1=" can cause a decrease in the absorption of "
judge1_2=" resulting in a reduced serum concentration and potentially a decrease in efficacy."
#Drug a can cause a decrease in the absorption of Drug b resulting in a reduced serum concentration and potentially a decrease in efficacy.
#a+1+b+2

judge2_1=" can cause an increase in the absorption of "
judge2_2=" resulting in an increased serum concentration and potentially a worsening of adverse effects."
#Drug a can cause an increase in the absorption of Drug b resulting in an increased serum concentration and potentially a worsening of adverse effects.
#a+1+b+2

judge3_1="The absorption of "
judge3_2=" can be decreased when combined with "
judge3_3="."
#1+b+2+a+3
#The absorption of Drug b can be decreased when combined with Drug a.

judge4_1="The bioavailability of "
judge4_2=" can be decreased when combined with "
judge4_3="."
#1+b+2+a+3
#The bioavailability of Drug b can be decreased when combined with Drug a.

judge5_1="The bioavailability of "
judge5_2=" can be increased when combined with "
judge5_3="."
#1+b+2+a+3
#The bioavailability of Drug b can be increased when combined with Drug a.

judge6_1="The metabolism of "
judge6_2=" can be decreased when combined with "
judge6_3="."
#1+b+2+a+3
#The metabolism of Drug b can be decreased when combined with Drug a.

judge7_1="The metabolism of "
judge7_2=" can be increased when combined with "
judge7_3="."
#1+b+2+a+3
#The metabolism of Drug b can be increased when combined with Drug a.

judge8_1="The protein binding of "
judge8_2=" can be decreased when combined with "
judge8_3="."
#1+b+2+a+3
#The protein binding of Drug b can be decreased when combined with Drug a.

judge9_1="The serum concentration of "
judge9_2=" can be decreased when it is combined with "
judge9_3="."
#1+b+2+a+3
#The serum concentration of Drug b can be decreased when it is combined with Drug a.

judge10_1="The serum concentration of "
judge10_2=" can be increased when it is combined with "
judge10_3="."
#1+b+2+a+3
#The serum concentration of Drug b can be increased when it is combined with Drug a.

judge11_1="The serum concentration of the active metabolites of "
judge11_2=" can be increased when "
judge11_3=" is used in combination with "
judge11_4="."
#1+b+2+b+3+a+4
#The serum concentration of the active metabolites of Drug b can be increased when Drug b is used in combination with Drug a.

judge12_1="The serum concentration of the active metabolites of "
judge12_2=" can be reduced when "
judge12_3=" is used in combination with "
judge12_4=" resulting in a loss in efficacy."
#1+b+2+b+3+a+4
#The serum concentration of the active metabolites of Drug b can be reduced when Drug b is used in combination with Drug a resulting in a loss in efficacy.


judge13_1="The therapeutic efficacy of "
judge13_2=" can be decreased when used in combination with "
judge13_3="."
#1+b+2+a+3
#The therapeutic efficacy of Drug b can be decreased when used in combination with Drug a.

judge14_1="The therapeutic efficacy of "
judge14_2=" can be increased when used in combination with "
judge14_3="."
#1+b+2+a+3
#The therapeutic efficacy of Drug b can be increased when used in combination with Drug a.

judge15_1=" may decrease the excretion rate of "
judge15_2=" which could result in a higher serum level."
#a+1+b+2
#Drug a may decrease the excretion rate of Drug b which could result in a higher serum level.

judge16_1=" may increase the excretion rate of "
judge16_2=" which could result in a lower serum level and potentially a reduction in efficacy."
#a+1+b+2
#Drug a may increase the excretion rate of Drug b which could result in a lower serum level and potentially a reduction in efficacy.

judge17_1=" may decrease the cardiotoxic activities of "
judge17_2="."
#a+1+b+2
#Drug a may decrease the cardiotoxic activities of Drug b.

judge18_1=" may increase the cardiotoxic activities of "
judge18_2="."
#a+1+b+2
#Drug a may increase the cardiotoxic activities of Drug b.

judge19_1=" may increase the central neurotoxic activities of "
judge19_2="."
#a+1+b+2
#Drug a may increase the central neurotoxic activities of Drug b.

judge20_1=" may increase the hepatotoxic activities of "
judge20_2="."
#a+1+b+2
#Drug a may increase the hepatotoxic activities of Drug b.

judge21_1=" may increase the nephrotoxic activities of "
judge21_2="."
#a+1+b+2
#Drug a may increase the nephrotoxic activities of Drug b.

judge22_1=" may increase the neurotoxic activities of "
judge22_2="."
#a+1+b+2
#Drug a may increase the neurotoxic activities of Drug b.

judge23_1=" may increase the ototoxic activities of "
judge23_2="."
#a+1+b+2
#Drug a may increase the ototoxic activities of Drug b.

judge24_1=" may decrease effectiveness of "
judge24_2=" as a diagnostic agent."
#a+1+b+2
#Drug a may decrease effectiveness of Drug b as a diagnostic agent.

judge25_1="The risk of a hypersensitivity reaction to "
judge25_2=" is increased when it is combined with "
judge25_3="."
#1+b+2+a+3
#The risk of a hypersensitivity reaction to Drug b is increased when it is combined with Drug a.

judge26_1="The risk or severity of adverse effects can be increased when "
judge26_2=" is combined with "
judge26_3="."
#1+a+2+b+3
#The risk or severity of adverse effects can be increased when Drug a is combined with Drug b.

judge27_1="The risk or severity of bleeding can be increased when "
judge27_2=" is combined with "
judge27_3="."
#1+a+2+b+3
#The risk or severity of bleeding can be increased when Drug a is combined with Drug b.

judge28_1="The risk or severity of heart failure can be increased when "
judge28_2=" is combined with "
judge28_3="."
#1+b+2+a+3
#The risk or severity of heart failure can be increased when Drug b is combined with Drug a.

judge29_1="The risk or severity of hyperkalemia can be increased when "
judge29_2=" is combined with "
judge29_3="."
#1+a+2+b+3
#The risk or severity of hyperkalemia can be increased when Drug a is combined with Drug b.

judge30_1="The risk or severity of hypertension can be increased when "
judge30_2=" is combined with "
judge30_3="."
#1+b+2+a+3
#The risk or severity of hypertension can be increased when Drug b is combined with Drug a.

judge31_1="The risk or severity of hypotension can be increased when "
judge31_2=" is combined with "
judge31_3="."
#1+a+2+b+3
#The risk or severity of hypotension can be increased when Drug a is combined with Drug b.

judge32_1="The risk or severity of QTc prolongation can be increased when "
judge32_2=" is combined with "
judge32_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation can be increased when Drug a is combined with Drug b.

judge33_1=" may decrease the analgesic activities of Drug b."
judge33_2="."
#a+1+b+2
#Drug a may decrease the analgesic activities of Drug b.

judge34_1=" may decrease the anticoagulant activities of "
judge34_2="."
#a+1+b+2
#Drug a may decrease the anticoagulant activities of Drug b.

judge35_1=" may decrease the antihypertensive activities of Drug b."
judge35_2="."
#a+1+b+2
#Drug a may decrease the antihypertensive activities of Drug b.

judge36_1=" may decrease the antiplatelet activities of "
judge36_2="."
#a+1+b+2
#Drug a may decrease the antiplatelet activities of Drug b.

judge37_1=" may decrease the bronchodilatory activities of "
judge37_2="."
#a+1+b+2
#Drug a may decrease the bronchodilatory activities of Drug b.

judge38_1=" may decrease the diuretic activities of "
judge38_2="."
#a+1+b+2
#Drug a may decrease the diuretic activities of Drug b.

judge39_1=" may decrease the neuromuscular blocking activities of "
judge39_2="."
#a+1+b+2
#Drug a may decrease the neuromuscular blocking activities of Drug b.

judge40_1=" may decrease the sedative activities of "
judge40_2="."
#a+1+b+2
#Drug a may decrease the sedative activities of Drug b.

judge41_1=" may decrease the stimulatory activities of "
judge41_2="."
#a+1+b+2
#Drug a may decrease the stimulatory activities of Drug b.

judge42_1=" may decrease the vasoconstricting activities of "
judge42_2="."
#a+1+b+2
#Drug a may decrease the vasoconstricting activities of Drug b.

judge43_1=" may increase the adverse neuromuscular activities of "
judge43_2="."
#a+1+b+2
#Drug a may increase the adverse neuromuscular activities of Drug b.

judge44_1=" may increase the analgesic activities of "
judge44_2="."
#a+1+b+2
#Drug a may increase the analgesic activities of Drug b.

judge45_1=" may increase the anticholinergic activities of "
judge45_2="."
#a+1+b+2
#Drug a may increase the anticholinergic activities of Drug b.

judge46_1=" may increase the anticoagulant activities of "
judge46_2="."
#a+1+b+2
#Drug a may increase the anticoagulant activities of Drug b.

judge47_1=" may increase the antihypertensive activities of "
judge47_2="."
#a+1+b+2
#Drug a may increase the antihypertensive activities of Drug b.

judge48_1=" may increase the antiplatelet activities of "
judge48_2="."
#a+1+b+2
#Drug a may increase the antiplatelet activities of Drug b.

judge49_1=" may increase the antipsychotic activities of "
judge49_2="."
#a+1+b+2
#Drug a may increase the antipsychotic activities of Drug b.

judge50_1=" may increase the arrhythmogenic activities of "
judge50_2="."
#a+1+b+2
#Drug a may increase the arrhythmogenic activities of Drug b.

judge51_1=" may increase the atrioventricular blocking (AV block) activities of "
judge51_2="."
#a+1+b+2
#Drug a may increase the atrioventricular blocking (AV block) activities of Drug b.

judge52_1=" may increase the bradycardic activities of "
judge52_2="."
#a+1+b+2
#Drug a may increase the bradycardic activities of Drug b.

judge53_1=" may increase the bronchoconstrictory activities of "
judge53_2="."
#a+1+b+2
#Drug a may increase the bronchoconstrictory activities of Drug b.

judge54_1=" may increase the central nervous system depressant (CNS depressant) activities of "
judge54_2="."
#a+1+b+2
#Drug a may increase the central nervous system depressant (CNS depressant) activities of Drug b.

judge55_1=" may increase the central nervous system depressant (CNS depressant) and hypertensive activities of "
judge55_2="."
#a+1+b+2
#Drug a may increase the central nervous system depressant (CNS depressant) and hypertensive activities of Drug b.

judge56_1=" may increase the constipating activities of "
judge56_2="."
#a+1+b+2
#Drug a may increase the constipating activities of Drug b.

judge57_1=" may increase the dermatologic adverse activities of "
judge57_2="."
#a+1+b+2
#Drug a may increase the dermatologic adverse activities of Drug b.

judge58_1=" may increase the fluid retaining activities of "
judge58_2="."
#a+1+b+2
#Drug a may increase the fluid retaining activities of Drug b.

judge59_1=" may increase the hypercalcemic activities of "
judge59_2="."
#a+1+b+2
#Drug a may increase the hypercalcemic activities of Drug b.

judge60_1=" may increase the hyperglycemic activities of "
judge60_2="."
#a+1+b+2
#Drug a may increase the hyperglycemic activities of Drug b.

judge61_1=" may increase the hyperkalemic activities of "
judge61_2="."
#a+1+b+2
#Drug a may increase the hyperkalemic activities of Drug b.

judge62_1=" may increase the hypertensive activities of "
judge62_2="."
#a+1+b+2
#Drug a may increase the hypertensive activities of Drug b.

judge63_1=" may increase the hypocalcemic activities of "
judge63_2="."
#a+1+b+2
#Drug a may increase the hypocalcemic activities of Drug b.

judge64_1=" may increase the hypoglycemic activities of "
judge64_2="."
#a+1+b+2
#Drug a may increase the hypoglycemic activities of Drug b.

judge65_1=" may increase the hypokalemic activities of "
judge65_2="."
#a+1+b+2
#Drug a may increase the hypokalemic activities of Drug b.

judge66_1=" may increase the hyponatremic activities of "
judge66_2="."
#a+1+b+2
#Drug a may increase the hyponatremic activities of Drug b.

judge67_1=" may increase the hypotensive activities of "
judge67_2="."
#a+1+b+2
#Drug a may increase the hypotensive activities of Drug b.

judge68_1=" may increase the hypotensive and central nervous system depressant (CNS depressant) activities of "
judge68_2="."
#a+1+b+2
#Drug a may increase the hypotensive and central nervous system depressant (CNS depressant) activities of Drug b.

judge69_1=" may increase the immunosuppressive activities of "
judge69_2="."
#a+1+b+2
#Drug a may increase the immunosuppressive activities of Drug b.

judge70_1=" may increase the myelosuppressive activities of "
judge70_2="."
#a+1+b+2
#Drug a may increase the myelosuppressive activities of Drug b.

judge71_1=" may increase the myopathic rhabdomyolysis activities of "
judge71_2="."
#a+1+b+2
#Drug a may increase the myopathic rhabdomyolysis activities of Drug b.

judge72_1=" may increase the neuroexcitatory activities of "
judge72_2="."
#a+1+b+2
#Drug a may increase the neuroexcitatory activities of Drug b.

judge73_1=" may increase the neuromuscular blocking activities of "
judge73_2="."
#a+1+b+2
#Drug a may increase the neuromuscular blocking activities of Drug b.

judge74_1=" may increase the orthostatic hypotensive activities of "
judge74_2="."
#a+1+b+2
#Drug a may increase the orthostatic hypotensive activities of Drug b.

judge75_1=" may increase the photosensitizing activities of "
judge75_2="."
#a+1+b+2
#Drug a may increase the photosensitizing activities of Drug b.

judge76_1=" may increase the QTc-prolonging activities of "
judge76_2="."
#a+1+b+2
#Drug a may increase the QTc-prolonging activities of Drug b.

judge77_1=" may increase the respiratory depressant activities of "
judge77_2="."
#a+1+b+2
#Drug a may increase the respiratory depressant activities of Drug b.

judge78_1=" may increase the sedative activities of "
judge78_2="."
#a+1+b+2
#Drug a may increase the sedative activities of Drug b.

judge79_1=" may increase the serotonergic activities of "
judge79_2="."
#a+1+b+2
#Drug a may increase the serotonergic activities of Drug b.

judge80_1=" may increase the stimulatory activities of "
judge80_2="."
#a+1+b+2
#Drug a may increase the stimulatory activities of Drug b.

judge81_1=" may increase the tachycardic activities of "
judge81_2="."
#a+1+b+2
#Drug a may increase the tachycardic activities of Drug b.

judge82_1=" may increase the thrombogenic activities of "
judge82_2="."
#a+1+b+2
#Drug a may increase the thrombogenic activities of Drug b.

judge83_1=" may increase the ulcerogenic activities of "
judge83_2="."
#a+1+b+2
#Drug a may increase the ulcerogenic activities of Drug b.


judge84_1=" may increase the vasoconstricting activities of "
judge84_2="."
#a+1+b+2
#Drug a may increase the vasoconstricting activities of Drug b.

judge85_1=" may increase the vasodilatory activities of "
judge85_2="."
#a+1+b+2
#Drug a may increase the vasodilatory activities of Drug b.

judge86_1=" may increase the vasopressor activities of "
judge86_2="."
#a+1+b+2
#Drug a may increase the vasopressor activities of Drug b.

judge87_1="The risk or severity of constipation can be increased when "
judge87_2=" is combined with "
judge87_3="."
#1+a+2+b+3
#The risk or severity of constipation can be increased when Drug a is combined with Drug b.

judge88_1="The risk or severity of bleeding and hemorrhage can be increased when "
judge88_2=" is combined with "
judge88_3="."
#1+a+2+b+3
#The risk or severity of bleeding and hemorrhage can be increased when Drug a is combined with Drug b.

judge89_1="The risk or severity of gastrointestinal bleeding can be increased when "
judge89_2=" is combined with "
judge89_3="."
#1+a+2+b+3
#The risk or severity of gastrointestinal bleeding can be increased when Drug a is combined with Drug b.

judge90_1="The risk or severity of bleeding and bruising can be increased when "
judge90_2=" is combined with "
judge90_3="."
#1+a+2+b+3
#The risk or severity of bleeding and bruising can be increased when Drug a is combined with Drug b.

judge91_1="The risk or severity of bradycardia can be increased when "
judge91_2=" is combined with "
judge91_3="."
#1+a+2+b+3
#The risk or severity of bradycardia can be increased when Drug a is combined with Drug b.

judge92_1="The risk or severity of hemorrhage can be increased when "
judge92_2=" is combined with "
judge92_3="."
#1+a+2+b+3
#The risk or severity of hemorrhage can be increased when Drug a is combined with Drug b.

judge93_1="The risk or severity of thromboembolism can be increased when "
judge93_2=" is combined with "
judge93_3="."
#1+a+2+b+3
#The risk or severity of thromboembolism can be increased when Drug a is combined with Drug b.

judge94_1="The risk or severity of gastrointestinal irritation can be increased when "
judge94_2=" is combined with "
judge94_3="."
#1+a+2+b+3
#The risk or severity of gastrointestinal irritation can be increased when Drug a is combined with Drug b.

judge95_1="The excretion of "
judge95_2=" can be decreased when combined with "
judge95_3="."
#1+a+2+b+3
#The excretion of Drug a can be decreased when combined with Drug b.

judge96_1="The excretion of "
judge96_2=" can be increased when combined with "
judge96_3="."
#1+a+2+b+3
#The excretion of Drug a can be increased when combined with Drug b.

judge97_1="The risk or severity of ventricular arrhythmias and Cardiac Arrhythmia can be increased when "
judge97_2=" is combined with "
judge97_3="."
#1+a+2+b+3
#The risk or severity of ventricular arrhythmias and Cardiac Arrhythmia can be increased when Drug a is combined with Drug b.

judge98_1="The risk or severity of hypercalcemia can be increased when "
judge98_2=" is combined with "
judge98_3="."
#1+a+2+b+3
#The risk or severity of hypercalcemia can be increased when Drug a is combined with Drug b.

judge99_1="The risk or severity of hypotension and neuromuscular blockade can be increased when "
judge99_2=" is combined with "
judge99_3="."
#1+a+2+b+3
#The risk or severity of hypotension and neuromuscular blockade can be increased when Drug a  is combined with Drug b.

judge100_1="The risk or severity of nephrotoxicity can be increased when "
judge100_2=" is combined with "
judge100_3="."
#1+a+2+b+3
#The risk or severity of nephrotoxicity can be increased when Drug a is combined with Drug b.

judge101_1="The risk or severity of serotonin syndrome can be increased when "
judge101_2=" is combined with "
judge101_3="."
#1+a+2+b+3
#The risk or severity of serotonin syndrome can be increased when Drug a is combined with Drug b.

judge102_1="The risk or severity of myopathy, rhabdomyolysis, and myoglobinuria can be increased when "
judge102_2=" is combined with "
judge102_3="."
#1+a+2+b+3
#The risk or severity of myopathy, rhabdomyolysis, and myoglobinuria can be increased when Drug a is combined with Drug b.

judge103_1="The risk or severity of urinary retention can be increased when "
judge103_2=" is combined with "
judge103_3="."
#1+a+2+b+3
#The risk or severity of urinary retention can be increased when Drug a is combined with Drug b.

judge104_1="The risk or severity of Tachycardia and drowsiness can be increased when "
judge104_2=" is combined with "
judge104_3="."
#1+a+2+b+3
#The risk or severity of Tachycardia and drowsiness can be increased when Drug a is combined with Drug b.

judge105_1="The risk or severity of renal failure and hypertension can be increased when "
judge105_2=" is combined with "
judge105_3="."
#1+a+2+b+3
#The risk or severity of renal failure and hypertension can be increased when Drug a is combined with Drug b.

judge106_1="The risk or severity of hyponatremia can be increased when "
judge106_2=" is combined with "
judge106_3="."
#1+a+2+b+3
#The risk or severity of hyponatremia can be increased when Drug a is combined with Drug b.

judge107_1="The risk or severity of myopathy can be increased when "
judge107_2=" is combined with "
judge107_3="."
#1+a+2+b+3
#The risk or severity of myopathy can be increased when Drug a is combined with Drug b.

judge108_1="The risk or severity of increased transaminases can be increased when "
judge108_2=" is combined with "
judge108_3="."
#1+a+2+b+3
#The risk or severity of increased transaminases can be increased when Drug a is combined with Drug b.

judge109_1="The risk or severity of neutropenia and thrombocytopenia can be increased when "
judge109_2=" is combined with "
judge109_3="."
#1+a+2+b+3
#The risk or severity of neutropenia and thrombocytopenia can be increased when Drug a is combined with Drug b.

judge110_1="The risk or severity of infection can be increased when "
judge110_2=" is combined with "
judge110_3="."
#1+a+2+b+3
#The risk or severity of infection can be increased when Drug a is combined with Drug b.

judge111_1="The risk or severity of Cardiovascular Impairment can be increased when "
judge111_2=" is combined with "
judge111_3="."
#1+a+2+b+3
#The risk or severity of Cardiovascular Impairment can be increased when Drug a is combined with Drug b.

judge112_1="The risk or severity of serotonin syndrome and hypomania can be increased when "
judge112_2=" is combined with "
judge112_3="."
#1+a+2+b+3
#The risk or severity of serotonin syndrome and hypomania can be increased when Drug a is combined with Drug b.

judge113_1=" may increase the arrhythmogenic and cardiotoxic activities of "
judge113_2="."
#a+1+b+2
#Drug a may increase the arrhythmogenic and cardiotoxic activities of Drug b.

judge114_1="The risk or severity of hyponatremia and water intoxication can be increased when "
judge114_2=" is combined with "
judge114_3="."
#1+a+2+b+3
#The risk or severity of hyponatremia and water intoxication can be increased when Drug a is combined with Drug b.

judge115_1="The risk or severity of hypertension, hyponatremia, and water intoxication can be increased when "
judge115_2=" is combined with "
judge115_3="."
#1+a+2+b+3
#The risk or severity of hypertension, hyponatremia, and water intoxication can be increased when Drug a is combined with Drug b.

judge116_1="The risk or severity of renal failure can be increased when "
judge116_2=" is combined with "
judge116_3="."
#1+a+2+b+3
#The risk or severity of renal failure can be increased when Drug a is combined with Drug b.

judge117_1="The risk or severity of Hypertrichosis can be increased when "
judge117_2=" is combined with "
judge117_3="."
#1+a+2+b+3
#The risk or severity of Hypertrichosis can be increased when Drug a is combined with Drug b.

judge118_1="The risk or severity of liver damage can be increased when "
judge118_2=" is combined with "
judge118_3="."
#1+a+2+b+3
#The risk or severity of liver damage can be increased when Drug a is combined with Drug b.

judge119_1="The risk or severity of nephrotoxicity and hypocalcemia can be increased when "
judge119_2=" is combined with "
judge119_3="."
#1+a+2+b+3
#The risk or severity of nephrotoxicity and hypocalcemia can be increased when Drug a is combined with Drug b.

judge120_1="The risk or severity of seizure can be increased when "
judge120_2=" is combined with "
judge120_3="."
#1+a+2+b+3
#The risk or severity of seizure can be increased when Drug a is combined with Drug b.

judge121_1="The risk or severity of neuromuscular blockade can be increased when "
judge121_2=" is combined with "
judge121_3="."
#1+a+2+b+3
#The risk or severity of neuromuscular blockade can be increased when Drug a is combined with Drug b.

judge122_1="The risk or severity of hypoglycemia can be increased when "
judge122_2=" is combined with "
judge122_3="."
#1+a+2+b+3
#The risk or severity of hypoglycemia can be increased when Drug a is combined with Drug b.

judge123_1="The risk or severity of neutropenia can be increased when "
judge123_2=" is combined with "
judge123_3="."
#1+a+2+b+3
#The risk or severity of neutropenia can be increased when Drug a is combined with Drug b.

judge124_1="The risk or severity of gastrointestinal bleeding and peptic ulcer can be increased when "
judge124_2=" is combined with "
judge124_3="."
#1+a+2+b+3
#The risk or severity of gastrointestinal bleeding and peptic ulcer can be increased when Drug a is combined with Drug b

judge125_1="The risk or severity of renal failure, hyperkalemia, and hypertension can be increased when "
judge125_2=" is combined with "
judge125_3="."
#1+a+2+b+3
#The risk or severity of renal failure, hyperkalemia, and hypertension can be increased when Drug a is combined with Drug b

judge126_1="The risk or severity of gastrointestinal bleeding and gastrointestinal ulceration can be increased when "
judge126_2=" is combined with "
judge126_3="."
#1+a+2+b+3
#The risk or severity of gastrointestinal bleeding and gastrointestinal ulceration can be increased when Drug a is combined with Drug b

judge127_1=" may increase the Pseudotumor Cerebri activities of "
judge127_2="."
#a+1+b+2
#Drug a may increase the Pseudotumor Cerebri activities of Drug b

judge128_1="The risk or severity of pseudotumor cerebri and elevated intracranial pressure can be increased when "
judge128_2=" is combined with "
judge128_3="."
#1+a+2+b+3
#The risk or severity of pseudotumor cerebri and elevated intracranial pressure can be increased when Drug a is combined with Drug b

judge129_1="The risk or severity of rhabdomyolysis can be increased when "
judge129_2=" is combined with "
judge129_3="."
#1+a+2+b+3
#The risk or severity of rhabdomyolysis can be increased when Drug a is combined with Drug b.

judge130_1="The risk or severity of increased glucose can be increased when "
judge130_2=" is combined with "
judge130_3="."
#1+a+2+b+3
#The risk or severity of increased glucose can be increased when Drug a is combined with Drug b.

judge131_1="The risk or severity of rhabdomyolysis, myoglobinuria, and elevated creatine kinase (CPK) can be increased when "
judge131_2=" is combined with "
judge131_3="."
#1+a+2+b+3
#The risk or severity of rhabdomyolysis, myoglobinuria, and elevated creatine kinase (CPK) can be increased when Drug a is combined with Drug b

judge132_1="The risk or severity of myopathy and rhabdomyolysis can be increased when "
judge132_2=" is combined with "
judge132_3="."
#1+a+2+b+3
#The risk or severity of myopathy and rhabdomyolysis can be increased when Drug a is combined with Drug b

judge133_1=" may increase the hypolipidaemic activities of "
judge133_2="."
#a+1+b+2
#Drug a may increase the hypolipidaemic activities of Drug b

judge134_1="The risk or severity of serotonin syndrome, extrapyramidal symptoms, and neuroleptic malignant syndrome can be increased when "
judge134_2=" is combined with "
judge134_3="."
#1+a+2+b+3
#The risk or severity of serotonin syndrome, extrapyramidal symptoms, and neuroleptic malignant syndrome can be increased when Drug a is combined with Drug b

judge135_1="The risk or severity of orthostatic hypotension and syncope can be increased when "
judge135_2=" is combined with "
judge135_3="."
#1+a+2+b+3
#The risk or severity of orthostatic hypotension and syncope can be increased when Drug a is combined with Drug b

judge136_1="The risk or severity of Thrombosis can be increased when "
judge136_2=" is combined with "
judge136_3="."
#1+a+2+b+3
#The risk or severity of Thrombosis can be increased when Drug a is combined with Drug b

judge137_1="The risk or severity of angioedema can be increased when "
judge137_2=" is combined with "
judge137_3="."
#1+a+2+b+3
#The risk or severity of angioedema can be increased when Drug a is combined with Drug b

judge138_1="The risk or severity of myopathy and rhabdomyolysis can be decreased when "
judge138_2=" is combined with "
judge138_3="."
#1+a+2+b+3
#The risk or severity of myopathy and rhabdomyolysis can be decreased when Drug a is combined with Drug b

judge139_1="The risk or severity of hypotension and orthostatic hypotension can be increased when "
judge139_2=" is combined with "
judge139_3="."
#1+a+2+b+3
#The risk or severity of hypotension and orthostatic hypotension can be increased when Drug a is combined with Drug b

judge140_1=" may increase the hypotensive and Electrolyte Disturbance activities of "
judge140_2="."
#a+1+b+2
#Drug a may increase the hypotensive and Electrolyte Disturbance activities of Drug b

judge141_1="The risk or severity of anaphylaxis can be increased when "
judge141_2=" is combined with "
judge141_3="."
#1+a+2+b+3
#The risk or severity of anaphylaxis can be increased when Drug a is combined with Drug b

judge142_1="The risk or severity of hyperkalemia and reduced intravascular volume can be increased when "
judge142_2=" is combined with "
judge142_3="."
#1+a+2+b+3
#The risk or severity of hyperkalemia and reduced intravascular volume can be increased when Drug a is combined with Drug b

judge143_1="The risk or severity of renal failure, hypotension, and hyperkalemia can be increased when "
judge143_2=" is combined with "
judge143_3="."
#1+a+2+b+3
#The risk or severity of renal failure, hypotension, and hyperkalemia can be increased when Drug a is combined with Drug b

judge144_1="The risk or severity of hypotension, hyperkalemia, and nephrotoxicity can be increased when "
judge144_2=" is combined with "
judge144_3="."
#1+a+2+b+3
#The risk or severity of hypotension, hyperkalemia, and nephrotoxicity can be increased when Drug a is combined with Drug b

judge145_1="The risk or severity of anemia and severe leukopenia can be increased when "
judge145_2=" is combined with "
judge145_3="."
#1+a+2+b+3
#The risk or severity of anemia and severe leukopenia can be increased when Drug a is combined with Drug b

judge146_1="The risk or severity of lactic acidosis can be increased when "
judge146_2=" is combined with "
judge146_3="."
#1+a+2+b+3
#The risk or severity of lactic acidosis can be increased when Drug a is combined with Drug b

judge147_1="The risk or severity of hypotension, nitritoid reactions, facial flushing, nausea, and vomiting can be increased when "
judge147_2=" is combined with "
judge147_3="."
#1+a+2+b+3
#The risk or severity of hypotension, nitritoid reactions, facial flushing, nausea, and vomiting can be increased when Drug a is combined with Drug b

judge148_1=""
judge148_2=""
judge148_3=""
#1+a+2+b+3
#The risk or severity of renal failure and hyperkalemia can be increased when Drug a is combined with Drug b

judge149_1="The risk or severity of hyperglycemia can be increased when "
judge149_2=" is combined with "
judge149_3="."
#1+a+2+b+3
#The risk or severity of hyperglycemia can be increased when Drug a is combined with Drug b

judge150_1="The risk or severity of gastrointestinal ulceration and gastrointestinal irritation can be increased when "
judge150_2=" is combined with "
judge150_3="."
#1+a+2+b+3
#The risk or severity of gastrointestinal ulceration and gastrointestinal irritation can be increased when Drug a is combined with Drug b

judge151_1="The risk or severity of hypokalemia can be increased when "
judge151_2=" is combined with "
judge151_3="."
#1+a+2+b+3
#The risk or severity of hypokalemia can be increased when Drug a is combined with Drug b

judge152_1="The risk or severity of ulceration can be increased when "
judge152_2=" is combined with "
judge152_3="."
#1+a+2+b+3
#The risk or severity of ulceration can be increased when Drug a is combined with Drug b

judge153_1="The risk or severity of tendinopathy can be increased when "
judge153_2=" is combined with "
judge153_3="."
#1+a+2+b+3
#The risk or severity of tendinopathy can be increased when Drug a is combined with Drug b

judge154_1="The risk or severity of fluid retention can be increased when "
judge154_2=" is combined with "
judge154_3="."
#1+a+2+b+3
#The risk or severity of fluid retention can be increased when Drug a is combined with Drug b

judge155_1="The risk or severity of hypokalemia can be increased when "
judge155_2=" is combined with "
judge155_3="."
#1+a+2+b+3
#The risk or severity of hypokalemia can be increased when Drug a is combined with Drug b

judge156_1="The risk or severity of myopathy and weakness can be increased when "
judge156_2=" is combined with "
judge156_3="."
#1+a+2+b+3
#The risk or severity of myopathy and weakness can be increased when Drug a is combined with Drug b.

judge157_1="The risk or severity of edema formation can be increased when "
judge157_2=" is combined with "
judge157_3="."
#1+a+2+b+3
#The risk or severity of edema formation can be increased when Drug a is combined with Drug b.

judge158_1=" may decrease the sedative and stimulatory activities of "
judge158_2="."
#a+1+b+2
#Drug a may decrease the sedative and stimulatory activities of Drug b.

judge159_1="The risk or severity of Tachycardia can be increased when "
judge159_2=" is combined with "
judge159_3="."
#1+a+2+b+3
#The risk or severity of Tachycardia can be increased when Drug a is combined with Drug b

judge160_1=" may increase the atrioventricular blocking (AV block) and tachycardic activities of "
judge160_2="."
#a+1+b+2
#Drug a may increase the atrioventricular blocking (AV block) and tachycardic activities of Drug b

judge161_1=" may decrease the anticholinergic activities of "
judge161_2="."
#a+1+b+2
#Drug a may decrease the anticholinergic activities of Drug b

judge162_1="The risk or severity of sedation can be increased when "
judge162_2=" is combined with "
judge162_3="."
#1+a+2+b+3
#The risk or severity of sedation can be increased when Drug a is combined with Drug b

judge163_1="The risk or severity of sedation and somnolence can be increased when "
judge163_2=" is combined with "
judge163_3="."
#1+a+2+b+3
#The risk or severity of sedation and somnolence can be increased when Drug a is combined with Drug b

judge164_1="The risk or severity of congestive heart failure and hypotension can be increased when "
judge164_2=" is combined with "
judge164_3="."
#1+a+2+b+3
#The risk or severity of congestive heart failure and hypotension can be increased when Drug a is combined with Drug b

judge165_1="The risk or severity of QTc prolongation can be decreased when "
judge165_2=" is combined with "
judge165_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation can be decreased when Drug a is combined with Drug b

judge166_1="The risk or severity of hypersensitivity reaction can be increased when "
judge166_2=" is combined with "
judge166_3="."
#1+a+2+b+3
#The risk or severity of hypersensitivity reaction can be increased when Drug a is combined with Drug b

judge167_1="The risk or severity of cardiotoxicity can be increased when "
judge167_2=" is combined with "
judge167_3="."
#1+a+2+b+3
#The risk or severity of cardiotoxicity can be increased when Drug a is combined with Drug b

judge168_1="The serum concentration of norepinephrine, an active metabolite of "
judge168_2=", can be decreased when used in combination with "
judge168_3="."
#1+a+2+b+3
#The serum concentration of norepinephrine, an active metabolite of Drug a, can be decreased when used in combination with Drug b

judge169_1="The risk or severity of serotonin syndrome and neuroleptic malignant syndrome can be increased when "
judge169_2=" is combined with "
judge169_3="."
#1+a+2+b+3
#The risk or severity of serotonin syndrome and neuroleptic malignant syndrome can be increased when Drug a is combined with Drug b

judge170_1="The risk or severity of cytotoxicity can be increased when "
judge170_2=" is combined with "
judge170_3="."
#1+a+2+b+3
#The risk or severity of cytotoxicity can be increased when Drug a is combined with Drug b

judge171_1="The risk or severity of serotonin syndrome, sedation, and seizure can be increased when "
judge171_2=" is combined with "
judge171_3="."
#1+a+2+b+3
#The risk or severity of serotonin syndrome, sedation, and seizure can be increased when Drug a is combined with Drug b

judge172_1="The risk or severity of serotonin syndrome and seizure can be increased when "
judge172_2=" is combined with "
judge172_3="."
#1+a+2+b+3
#The risk or severity of serotonin syndrome and seizure can be increased when Drug a is combined with Drug b

judge173_1="The risk or severity of hypotension and central nervous system depression can be increased when "
judge173_2=" is combined with "
judge173_3="."
#1+a+2+b+3
#The risk or severity of hypotension and central nervous system depression can be increased when Drug a is combined with Drug b

judge174_1="The risk or severity of gastrointestinal ulceration can be increased when "
judge174_2=" is combined with "
judge174_3="."
#1+a+2+b+3
#The risk or severity of gastrointestinal ulceration can be increased when Drug a is combined with Drug b

judge175_1="The risk or severity of reduced gastrointestinal motility can be increased when "
judge175_2=" is combined with "
judge175_3="."
#1+a+2+b+3
#The risk or severity of reduced gastrointestinal motility can be increased when Drug a is combined with Drug b

judge176_1="The risk or severity of hyperthermia and oligohydrosis can be increased when "
judge176_2=" is combined with "
judge176_3="."
#1+a+2+b+3
#The risk or severity of hyperthermia and oligohydrosis can be increased when Drug a is combined with Drug b

judge177_1=" may increase the gastrointestinal motility reducing activities of "
judge177_2="."
#a+1+b+2
#Drug a may increase the gastrointestinal motility reducing activities of Drug b

judge178_1="The risk or severity of serotonin syndrome and seizure can be increased when "
judge178_2=" is combined with "
judge178_3="."
#1+a+2+b+3
#The risk or severity of serotonin syndrome and seizure can be increased when Drug a is combined with Drug b

judge179_1=" may increase the QTc-prolonging and arrhythmogenic activities of "
judge179_2="."
#a+1+b+2
#Drug a may increase the QTc-prolonging and arrhythmogenic activities of Drug b

judge180_1="The risk or severity of QTc prolongation and serotonin syndrome can be increased when "
judge180_2=" is combined with "
judge180_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation and serotonin syndrome can be increased when Drug a is combined with Drug b

judge181_1="The serum concentration of E3174, an active metabolite of "
judge181_2=" can be decreased when used in combination with "
judge181_3="."
#1+a+2+b+3
#The serum concentration of E3174, an active metabolite of Drug a can be decreased when used in combination with Drug b

judge182_1="The risk or severity of QTc prolongation and ventricular arrhythmias can be increased when "
judge182_2=" is combined with "
judge182_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation and ventricular arrhythmias can be increased when Drug a is combined with Drug b

judge183_1="The risk or severity of ventricular arrhythmias and torsade de pointes can be increased when "
judge183_2=" is combined with "
judge183_3="."
#1+a+2+b+3
#The risk or severity of ventricular arrhythmias and torsade de pointes can be increased when Drug a is combined with Drug b

judge184_1="The risk or severity of QTc prolongation and hypotension can be increased when "
judge184_2=" is combined with "
judge184_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation and hypotension can be increased when Drug a is combined with Drug b

judge185_1=" may decrease the vasodilatory activities of "
judge185_2="."
#a+1+b+2
#Drug a may decrease the vasodilatory activities of Drug b

judge186_1="The risk or severity of Cardiac Arrhythmia can be increased when "
judge186_2=" is combined with "
judge186_3="."
#1+a+2+b+3
#The risk or severity of Cardiac Arrhythmia can be increased when Drug a is combined with Drug b

judge187_1="The risk or severity of hypotension and priapism can be increased when "
judge187_2=" is combined with "
judge187_3="."
#1+a+2+b+3
#The risk or severity of hypotension and priapism can be increased when Drug a is combined with Drug b

judge188_1="The risk or severity of orthostatic hypotension can be increased when "
judge188_2=" is combined with "
judge188_3="."
#1+a+2+b+3
#The risk or severity of orthostatic hypotension can be increased when Drug a is combined with Drug b

judge189_1="The risk or severity of hypotension, dyspepsia, and headache can be increased when "
judge189_2=" is combined with "
judge189_3="."
#1+a+2+b+3
#The risk or severity of hypotension, dyspepsia, and headache can be increased when Drug a is combined with Drug b

judge190_1="The risk or severity of QTc prolongation, torsade de pointes, hypokalemia, hypomagnesemia, and cardiac arrest can be increased when "
judge190_2=" is combined with "
judge190_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation, torsade de pointes, hypokalemia, hypomagnesemia, and cardiac arrest can be increased when Drug a is combined with Drug b

judge191_1=" may increase the bradycardic, atrioventricular blocking (AV block), and arrhythmogenic activities of "
judge191_2="."
#a+1+b+2
#Drug a may increase the bradycardic, atrioventricular blocking (AV block), and arrhythmogenic activities of Drug b

judge192_1=" may increase the hypertensive and vasoconstricting activities of "
judge192_2="."
#a+1+b+2
#Drug a may increase the hypertensive and vasoconstricting activities of Drug b

judge193_1="The risk or severity of ototoxicity and nephrotoxicity can be increased when "
judge193_2=" is combined with "
judge193_3="."
#1+a+2+b+3
#The risk or severity of ototoxicity and nephrotoxicity can be increased when Drug a is combined with Drug b

judge194_1="The risk or severity of hypocalcemia can be increased when "
judge194_2=" is combined with "
judge194_3="."
#1+a+2+b+3
#The risk or severity of hypocalcemia can be increased when Drug a is combined with Drug b

judge195_1="The risk or severity of hypotension, hyperkalemia, and hypokalemia can be increased when "
judge195_2=" is combined with "
judge195_3="."
#1+a+2+b+3
#The risk or severity of hypotension, hyperkalemia, and hypokalemia can be increased when Drug a is combined with Drug b

judge196_1=" may decrease the hypoglycemic activities of "
judge196_2="."
#a+1+b+2
#Drug a may decrease the hypoglycemic activities of Drug b

judge197_1="The risk or severity of hyperbilirubinemia can be increased when "
judge197_2=" is combined with "
judge197_3="."
#1+a+2+b+3
#The risk or severity of hyperbilirubinemia can be increased when Drug a is combined with Drug b

judge198_1="The risk or severity of weight gain and edema formation can be increased when "
judge198_2=" is combined with "
judge198_3="."
#1+a+2+b+3
#The risk or severity of weight gain and edema formation can be increased when Drug a is combined with Drug b

judge199_1="The risk or severity of granulocytopenia can be increased when "
judge199_2=" is combined with "
judge199_3="."
#1+a+2+b+3
#The risk or severity of granulocytopenia can be increased when Drug a is combined with Drug b

judge200_1="The risk or severity of hypotension, hyperglycemia, and hyperuricemia can be increased when "
judge200_2=" is combined with "
judge200_3="."
#1+a+2+b+3
#The risk or severity of hypotension, hyperglycemia, and hyperuricemia can be increased when Drug a is combined with Drug b

judge201_1="The risk or severity of bleeding and gastrointestinal bleeding can be increased when "
judge201_2=" is combined with "
judge201_3="."
#1+a+2+b+3
#The risk or severity of bleeding and gastrointestinal bleeding can be increased when Drug a is combined with Drug b

judge202_1="The risk or severity of bleeding, nephrotoxicity, and gastrointestinal bleeding can be increased when "
judge202_2=" is combined with "
judge202_3="."
#1+a+2+b+3
#The risk or severity of bleeding, nephrotoxicity, and gastrointestinal bleeding can be increased when Drug a is combined with Drug b

judge203_1="The risk or severity of congestive heart failure, bleeding, hypotension, and Tachycardia can be increased when "
judge203_2=" is combined with "
judge203_3="."
#1+a+2+b+3
#The risk or severity of congestive heart failure, bleeding, hypotension, and Tachycardia can be increased when Drug a is combined with Drug b

judge204_1="The risk or severity of methemoglobinemia can be increased when "
judge204_2=" is combined with "
judge204_3="."
#1+a+2+b+3
#The risk or severity of methemoglobinemia can be increased when Drug a is combined with Drug b

judge205_1="The risk or severity of myelosuppression can be increased when "
judge205_2=" is combined with "
judge205_3="."
#1+a+2+b+3
#The risk or severity of myelosuppression can be increased when Drug a is combined with Drug b

judge206_1=" may increase the orthostatic hypotensive, hypotensive, and antihypertensive activities of "
judge206_2="."
#a+1+b+2
#Drug a may increase the orthostatic hypotensive, hypotensive, and antihypertensive activities of Drug b

judge207_1=" may decrease the hypertensive activities of "
judge207_2="."
#a+1+b+2
#Drug a may decrease the hypertensive activities of Drug b

judge208_1="The risk or severity of adverse effects can be decreased when "
judge208_2=" is combined with "
judge208_3="."
#1+a+2+b+3
#The risk or severity of adverse effects can be decreased when Drug a is combined with Drug b

judge209_1="The risk or severity of peripheral neuropathy can be increased when "
judge209_2=" is combined with "
judge209_3="."
#1+a+2+b+3
#The risk or severity of peripheral neuropathy can be increased when Drug a is combined with Drug b

judge210_1="The risk or severity of osteomalacia can be increased when "
judge210_2=" is combined with "
judge210_3="."
#1+a+2+b+3
#The risk or severity of osteomalacia can be increased when Drug a is combined with Drug b

judge211_1="The risk or severity of liver enzyme elevations can be increased when "
judge211_2=" is combined with "
judge211_3="."
#1+a+2+b+3
#The risk or severity of liver enzyme elevations can be increased when Drug a is combined with Drug b

judge212_1="The risk or severity of pulmonary toxicity can be increased when "
judge212_2=" is combined with "
judge212_3="."
#1+a+2+b+3
#The risk or severity of pulmonary toxicity can be increased when Drug a is combined with Drug b

judge213_1="The risk or severity of hypotension and neuromuscular blockade can be increased when "
judge213_2=" is combined with "
judge213_3="."
#1+a+2+b+3
#The risk or severity of hypotension and neuromuscular blockade can be increased when Drug a is combined with Drug b

judge214_1=" may decrease the nephrotoxic activities of "
judge214_2="."
#a+1+b+2
#Drug a may decrease the nephrotoxic activities of Drug b

judge215_1="The risk or severity of Cardiac Arrhythmia and CNS stimulation can be increased when "
judge215_2=" is combined with "
judge215_3="."
#1+a+2+b+3
#The risk or severity of Cardiac Arrhythmia and CNS stimulation can be increased when Drug a is combined with Drug b

judge216_1="The risk or severity of confusion, irritability, and sleep disorders can be increased when "
judge216_2=" is combined with "
judge216_3="."
#1+a+2+b+3
#The risk or severity of confusion, irritability, and sleep disorders can be increased when Drug a is combined with Drug b

judge217_1="The risk or severity of sinus node depression can be increased when "
judge217_2=" is combined with "
judge217_3="."
#1+a+2+b+3
#The risk or severity of sinus node depression can be increased when Drug a is combined with Drug b

judge218_1="The risk or severity of generalized seizure and bradycardia can be increased when "
judge218_2=" is combined with "
judge218_3="."
#1+a+2+b+3
#The risk or severity of generalized seizure and bradycardia can be increased when Drug a is combined with Drug b

judge219_1="The risk or severity of jaw osteonecrosis and anti-angiogenesis can be increased when "
judge219_2=" is combined with "
judge219_3="."
#1+a+2+b+3
#The risk or severity of jaw osteonecrosis and anti-angiogenesis can be increased when Drug a is combined with Drug b

judge220_1="The risk or severity of generalized seizure can be increased when "
judge220_2=" is combined with "
judge220_3="."
#1+a+2+b+3
#The risk or severity of generalized seizure can be increased when Drug a is combined with Drug b

judge221_1="The risk or severity of bronchospasm, shortness of breath, and dyspnea can be increased when "
judge221_2=" is combined with "
judge221_3="."
#1+a+2+b+3
#The risk or severity of bronchospasm, shortness of breath, and dyspnea can be increased when Drug a is combined with Drug b

judge222_1=" may increase the thrombocytopenic activities of "
judge222_2="."
#a+1+b+2
#Drug a may increase the thrombocytopenic activities of Drug b

judge223_1=" may increase the neutropenic activities of "
judge223_2="."
#a+1+b+2
#Drug a may increase the neutropenic activities of Drug b

judge224_1=" may increase the uterotonic activities of "
judge224_2="."
#a+1+b+2
#Drug a may increase the uterotonic activities of Drug b

judge225_1="The risk or severity of QTc prolongation and torsade de pointes can be increased when "
judge225_2=" is combined with "
judge225_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation and torsade de pointes can be increased when Drug a is combined with Drug b

judge226_1=" may increase the atrioventricular blocking (AV block) and arrhythmogenic activities of "
judge226_2="."
#a+1+b+2
#Drug a may increase the atrioventricular blocking (AV block) and arrhythmogenic activities of Drug b

judge227_1="The risk or severity of congestive heart failure can be increased when "
judge227_2=" is combined with "
judge227_3="."
#1+a+2+b+3
#The risk or severity of congestive heart failure can be increased when Drug a is combined with Drug b

judge228_1="The risk or severity of hyperkalemia and metabolic acidosis can be increased when "
judge228_2=" is combined with "
judge228_3="."
#1+a+2+b+3
#The risk or severity of hyperkalemia and metabolic acidosis can be increased when Drug a is combined with Drug b

judge229_1="The risk or severity of visual accommodation disturbances can be increased when "
judge229_2=" is combined with "
judge229_3="."
#1+a+2+b+3
#The risk or severity of visual accommodation disturbances can be increased when Drug a is combined with Drug b

judge230_1="The risk or severity of Stevens-Johnson syndrome can be increased when "
judge230_2=" is combined with "
judge230_3="."
#1+a+2+b+3
#The risk or severity of Stevens-Johnson syndrome can be increased when Drug a is combined with Drug b

judge231_1="The risk or severity of cytopenia can be increased when "
judge231_2=" is combined with "
judge231_3="."
#1+a+2+b+3
#The risk or severity of cytopenia can be increased when Drug a is combined with Drug b

judge232_1="The risk or severity of serotonin syndrome and opioid toxicity can be increased when "
judge232_2=" is combined with "
judge232_3="."
#1+a+2+b+3
#The risk or severity of serotonin syndrome and opioid toxicity can be increased when Drug a is combined with Drug b

judge233_1=" may increase the teratogenic activities of "
judge233_2="."
#a+1+b+2
#Drug a may increase the teratogenic activities of Drug b

judge234_1=" may increase the hypothyroid activities of "
judge234_2="."
#a+1+b+2
#Drug a may increase the hypothyroid activities of Drug b

judge235_1=" may increase the opioid antagonism activities of "
judge235_2="."
#a+1+b+2
#Drug a may increase the opioid antagonism activities of Drug b

judge236_1=" may increase the hypotensive and vasodilatory activities of "
judge236_2="."
#a+1+b+2
#Drug a may increase the hypotensive and vasodilatory activities of Drug b

judge237_1=" may increase the orthostatic hypotensive and hypotensive activities of "
judge237_2="."
#a+1+b+2
#Drug a may increase the orthostatic hypotensive and hypotensive activities of Drug b

judge238_1=" may increase the pancreatitis activities of "
judge238_2="."
#a+1+b+2
#Drug a may increase the pancreatitis activities of Drug b

judge239_1=" may decrease the hypotensive activities of "
judge239_2="."
#a+1+b+2
#Drug a may decrease the hypotensive activities of Drug b

judge240_1=" may increase the sympathomimetic activities of "
judge240_2="."
#a+1+b+2
#Drug a may increase the sympathomimetic activities of Drug b

judge241_1=" may increase the serotonergic and central nervous system depressant (CNS depressant) activities of "
judge241_2="."
#a+1+b+2
#Drug a may increase the serotonergic and central nervous system depressant (CNS depressant) activities of Drug b

judge242_1=" may increase the alpha-adrenergic activities of "
judge242_2="."
#a+1+b+2
#Drug a may increase the alpha-adrenergic activities of Drug b

judge243_1=" may decrease the antineoplastic activities of "
judge243_2="."
#a+1+b+2
#Drug a may decrease the antineoplastic activities of Drug b

judge244_1="The risk or severity of rash can be increased when "
judge244_2=" is combined with "
judge244_3="."
#1+a+2+b+3
#The risk or severity of rash can be increased when Drug a is combined with Drug b

judge245_1="The risk or severity of leukopenia can be increased when "
judge245_2=" is combined with "
judge245_3="."
#1+a+2+b+3
#The risk or severity of leukopenia can be increased when Drug a is combined with Drug b

judge246_1="The serum concentration of carbamazepine-10,11­ epoxide (CBZ-E), an active metabolite of "
judge246_2=", can be increased when used in combination with "
judge246_3="."
#1+a+2+b+3
#The serum concentration of carbamazepine-10,11­ epoxide (CBZ-E), an active metabolite of Drug a, can be increased when used in combination with Drug b

judge247_1="The serum concentration of 5-amino-imidazole-4-carboxamide (AIC), an active metabolite of "
judge247_2=", can be increased when used in combination with "
judge247_3="."
#1+a+2+b+3
#The serum concentration of 5-amino-imidazole-4-carboxamide (AIC), an active metabolite of Drug a, can be increased when used in combination with Drug b

judge248_1="The risk or severity of QTc prolongation, ventricular arrhythmias, torsade de pointes, and convulsion can be increased when "
judge248_2=" is combined with "
judge248_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation, ventricular arrhythmias, torsade de pointes, and convulsion can be increased when Drug a is combined with Drug b

judge249_1="The risk or severity of torsade de pointes and Cardiac Arrhythmia can be increased when "
judge249_2=" is combined with "
judge249_3="."
#1+a+2+b+3
#The risk or severity of torsade de pointes and Cardiac Arrhythmia can be increased when Drug a is combined with Drug b

judge250_1="The serum concentration of 14-OH-Clarithromycin, an active metabolite of "
judge250_2=", can be increased when used in combination with "
judge250_3="."
#1+a+2+b+3
#The serum concentration of 14-OH-Clarithromycin, an active metabolite of Drug a, can be increased when used in combination with Drug b

judge251_1="The serum concentration of Amprenavir, an active metabolite of "
judge251_2=", can be decreased when used in combination with "
judge251_3="."
#1+a+2+b+3
#The serum concentration of Amprenavir, an active metabolite of Drug a, can be decreased when used in combination with Drug b

judge252_1="The risk or severity of QTc prolongation, torsade de pointes, and cardiotoxicity can be increased when "
judge252_2=" is combined with "
judge252_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation, torsade de pointes, and cardiotoxicity can be increased when Drug a is combined with Drug b

judge253_1="The risk or severity of hypertension, serotonin syndrome, and CNS depression can be increased when "
judge253_2=" is combined with "
judge253_3="."
#1+a+2+b+3
#The risk or severity of hypertension, serotonin syndrome, and CNS depression can be increased when Drug a is combined with Drug b

judge254_1="The serum concentration of 25-O-Desacetylrifabutin, an active metabolite of "
judge254_2=", can be increased when used in combination with "
judge254_3="."
#1+a+2+b+3
#The serum concentration of 25-O-Desacetylrifabutin, an active metabolite of Drug a, can be increased when used in combination with Drug b

judge255_1="The risk or severity of seizure and encephalopathy can be increased when "
judge255_2=" is combined with "
judge255_3="."
#1+a+2+b+3
#The risk or severity of seizure and encephalopathy can be increased when Drug a is combined with Drug b

judge256_1="The risk or severity of QTc prolongation and Cardiac Arrhythmia can be increased when "
judge256_2=" is combined with "
judge256_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation and Cardiac Arrhythmia can be increased when Drug a is combined with Drug b

judge257_1="The serum concentration of Cycloguanil, an active metabolite of "
judge257_2=", can be decreased when used in combination with "
judge257_3="."
#1+a+2+b+3
#The serum concentration of Cycloguanil, an active metabolite of Drug a, can be decreased when used in combination with Drug b

judge258_1="The risk or severity of ventricular arrhythmias can be increased when "
judge258_2=" is combined with "
judge258_3="."
#1+a+2+b+3
#The risk or severity of ventricular arrhythmias can be increased when Drug a is combined with Drug b

judge259_1="The risk or severity of seizure can be decreased when "
judge259_2=" is combined with "
judge259_3="."
#1+a+2+b+3
#The risk or severity of seizure can be decreased when Drug a is combined with Drug b

judge260_1="The risk or severity of intraocular pressure can be increased when "
judge260_2=" is combined with "
judge260_3="."
#1+a+2+b+3
#The risk or severity of intraocular pressure can be increased when Drug a is combined with Drug b

judge261_1="The risk or severity of CNS depression can be increased when "
judge261_2=" is combined with "
judge261_3="."
#1+a+2+b+3
#The risk or severity of CNS depression can be increased when Drug a is combined with Drug b

judge262_1="The risk or severity of QTc prolongation, torsade de pointes, and Cardiac Arrhythmia can be increased when "
judge262_2=" is combined with "
judge262_3="."
#1+a+2+b+3
#The risk or severity of QTc prolongation, torsade de pointes, and Cardiac Arrhythmia can be increased when Drug a is combined with Drug b

judge263_1="The risk or severity of ototoxicity can be increased when "
judge263_2=" is combined with "
judge263_3="."
#1+a+2+b+3
#The risk or severity of ototoxicity can be increased when Drug a is combined with Drug b

judge264_1="The risk or severity of sedation and extrapyramidal symptoms can be increased when "
judge264_2=" is combined with "
judge264_3="."
#1+a+2+b+3
#The risk or severity of sedation and extrapyramidal symptoms can be increased when Drug a is combined with Drug b

judge265_1=" may increase the central nervous system depressant (CNS depressant) and sedative activities of "
judge265_2="."
#a+1+b+2
#Drug a may increase the central nervous system depressant (CNS depressant) and sedative activities of Drug b

judge266_1="The serum concentration of Phenobarbital, an active metabolite of "
judge266_2=", can be increased when used in combination with "
judge266_3="."
#1+a+2+b+3
#The serum concentration of Phenobarbital, an active metabolite of Drug a, can be increased when used in combination with Drug b

judge267_1="The risk or severity of anemia can be increased when "
judge267_2=" is combined with "
judge267_3="."
#1+a+2+b+3
#The risk or severity of anemia can be increased when Drug a is combined with Drug b

judge268_1="The serum concentration of dideoxyadenosine 5’-triphosphate, an active metabolite of "
judge268_2=", can be increased when used in combination with "
judge268_3="."
#1+a+2+b+3
#The serum concentration of dideoxyadenosine 5’-triphosphate, an active metabolite of Drug a, can be increased when used in combination with Drug b

judge269_1="The risk or severity of CNS stimulation can be increased when "
judge269_2=" is combined with "
judge269_3="."
#1+a+2+b+3
#The risk or severity of CNS stimulation can be increased when Drug a is combined with Drug b

judge270_1="The serum concentration of Fingolimod-phosphate, an active metabolite of "
judge270_2=", can be increased when used in combination with "
judge270_3="."
#1+a+2+b+3
#The serum concentration of Fingolimod-phosphate, an active metabolite of Drug a, can be increased when used in combination with Drug b

judge271_1="The risk or severity of ergotism can be increased when "
judge271_2=" is combined with "
judge271_3="."
#1+a+2+b+3
#The risk or severity of ergotism can be increased when Drug a is combined with Drug b

judge272_1="The risk or severity of hypotension and sinus node depression can be increased when "
judge272_2=" is combined with "
judge272_3="."
#1+a+2+b+3
#The risk or severity of hypotension and sinus node depression can be increased when Drug a is combined with Drug b

judge273_1="The serum concentration of dihydroartemisinin, an active metabolite of "
judge273_2=", can be decreased when used in combination with "
judge273_3="."
#1+a+2+b+3
#The serum concentration of dihydroartemisinin, an active metabolite of Drug a, can be decreased when used in combination with Drug b

judge274_1=" may decrease the arrhythmogenic activities of "
judge274_2="."
#a+1+b+2
#Drug a may decrease the arrhythmogenic activities of Drug b

def parseXml(ParseFunc, inFile="", outFile="", **kwargs):
    ns = '{http://www.drugbank.ca}'
    count = 0
    b = open('D:/paper2/muti_DDI_id.txt', "w")
    print('解析开始---------------------------')
    with open(outFile, 'w') as out:
        for event, drug in etree.iterparse(inFile, events=('end',), tag=ns+'drug'):

            # 条件一判断
            if (drug.get('type') != 'small molecule'):
                continue

            # 条件二判断
            flag = False
            groups = drug.find(ns + 'groups')
            for group in groups.iter(ns + 'group'):
                if(group.text == 'approved'):
                    flag = True
                    break
            if (not flag):
                continue

            result_str = ''
            # 当前drug的id
            drug_pri_id = drug.find(ns + 'drugbank-id').text

            drug_name=drug.find(ns+'name').text
            #zch

            # 解析当前drug 得到输出的字符串


            result_str = ParseFunc(
                drugElement=drug, drug_pri_id=drug_pri_id, drug_name=drug_name, ns=ns, **kwargs)
            #zch

            # 清理引用，减少内存占用
            drug.clear()
            while drug.getprevious() is not None:
                del drug.getparent()[0]

            # 写入文件
            out.write(result_str)
            b.write(drug_pri_id+"\n")
            # 记数
            count += 1
            print(count)
            # if(count == 10):
            #     return 0
    b.close()
    print('解析结束---------------------------')

def parseInteraction(drugElement, drug_pri_id, drug_name, ns):
    result_str = ''
    drug_interactions = drugElement.find(ns + 'drug-interactions')
    for drug_interaction in drug_interactions.iter(ns + 'drug-interaction'):
        # 拼装字符串
        result_str += drug_pri_id + ' ' + \
            drug_interaction[0].text + ' '

        drug_name_2=drug_interaction[1].text
        if(drug_interaction[2].text==drug_name+judge1_1+drug_name_2+judge1_2):
            result_str+=drug_pri_id+' '+ \
                'pk/pd'+' '+'-'+' '+'0'+' '+'1'+' '
        elif(drug_interaction[2].text==drug_name_2+judge1_1+drug_name+judge1_2):
            result_str+=drug_interaction[0].text+' '+ \
                'pk/pd'+' '+'-'+' '+'0'+' '+'1'+' '
        #1

        if (drug_interaction[2].text == drug_name + judge2_1 + drug_name_2 + judge2_2):
            result_str += drug_pri_id + ' ' + \
                          'pk/a' + ' ' + '+' + ' '+'0'+' ' + '2' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge2_1 + drug_name + judge2_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk/a' + ' ' + '+' + ' '+'0'+' '+'2' + ' '
        # 2

        if (drug_interaction[2].text == judge3_1+drug_name_2+judge3_2+drug_name+judge3_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' ' + '3' + ' '
        elif (drug_interaction[2].text == judge3_1+drug_name+judge3_2+drug_name_2+judge3_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' '+'3' + ' '
        # 3

        if (drug_interaction[2].text == judge4_1+drug_name_2+judge4_2+drug_name+judge4_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' ' + '4' + ' '
        elif (drug_interaction[2].text == judge4_1+drug_name+judge4_2+drug_name_2+judge4_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' '+'4' + ' '
        # 4

        if (drug_interaction[2].text == judge5_1+drug_name_2+judge5_2+drug_name+judge5_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' ' +'0'+' '+ '5' + ' '
        elif (drug_interaction[2].text == judge5_1+drug_name+judge5_2+drug_name_2+judge5_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' '+'0'+' '+ '5' + ' '
        #5

        if (drug_interaction[2].text == judge6_1+drug_name_2+judge6_2+drug_name+judge6_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' ' + '6' + ' '
        elif (drug_interaction[2].text == judge6_1+drug_name+judge6_2+drug_name_2+judge6_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' '+ '6' + ' '
        #6

        if (drug_interaction[2].text == judge7_1+drug_name_2+judge7_2+drug_name+judge7_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' '+'0'+' ' + '7' + ' '
        elif (drug_interaction[2].text == judge7_1+drug_name+judge7_2+drug_name_2+judge7_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' '+'0'+' '+ '7' + ' '
        #7

        if (drug_interaction[2].text == judge8_1+drug_name_2+judge8_2+drug_name+judge8_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' ' + '8' + ' '
        elif (drug_interaction[2].text == judge8_1+drug_name+judge8_2+drug_name_2+judge8_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' '+ '8' + ' '
        #8

        if (drug_interaction[2].text == judge9_1+drug_name_2+judge9_2+drug_name+judge9_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' ' + '9' + ' '
        elif (drug_interaction[2].text == judge9_1+drug_name+judge9_2+drug_name_2+judge9_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' '+ '9' + ' '
        #9

        if (drug_interaction[2].text == judge10_1+drug_name_2+judge10_2+drug_name+judge10_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' ' +'0'+' '+ '10' + ' '
        elif (drug_interaction[2].text == judge10_1+drug_name+judge10_2+drug_name_2+judge10_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' '+'0'+' '+ '10' + ' '
        #10

        if (drug_interaction[2].text == judge11_1+drug_name_2+judge11_2+drug_name_2+judge11_3+drug_name+judge11_4):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' ' +'0'+' '+ '11' + ' '
        elif (drug_interaction[2].text == judge11_1+drug_name+judge11_2+drug_name+judge11_3+drug_name_2+judge11_4):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' '+'0'+' '+ '11' + ' '
        #11

        if (drug_interaction[2].text == judge12_1+drug_name_2+judge12_2+drug_name_2+judge12_3+drug_name+judge12_4):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' ' + '12' + ' '
        elif (drug_interaction[2].text == judge12_1+drug_name+judge12_2+drug_name+judge12_3+drug_name_2+judge12_4):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' '+ '12' + ' '
        #12

        if (drug_interaction[2].text == judge13_1 + drug_name_2 + judge13_2 + drug_name + judge13_3):
            result_str += drug_pri_id + ' ' + \
                          'pd' + ' ' + '-' + ' ' +'0'+' '+ '13' + ' '
        elif (drug_interaction[2].text == judge13_1 + drug_name + judge13_2 + drug_name_2 + judge13_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd' + ' ' + '-' + ' '+'0'+' ' + '13' + ' '
        #13

        if (drug_interaction[2].text == judge14_1 + drug_name_2 + judge14_2 + drug_name + judge14_3):
            result_str += drug_pri_id + ' ' + \
                          'pd' + ' ' + '+' + ' '+'0'+' ' + '14' + ' '
        elif (drug_interaction[2].text == judge14_1 + drug_name + judge14_2 + drug_name_2 + judge14_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd' + ' ' + '+' + ' ' +'0'+' '+ '14' + ' '
        #14

        if (drug_interaction[2].text == drug_name + judge15_1 + drug_name_2 + judge15_2):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' ' + '15' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge15_1 + drug_name + judge15_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' '+'0'+' ' + '15' + ' '
        #15

        if (drug_interaction[2].text == drug_name + judge16_1 + drug_name_2 + judge16_2):
            result_str += drug_pri_id + ' ' + \
                          'pk/pd' + ' ' + '+' + ' ' +'0'+' '+ '16' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge16_1 + drug_name + judge16_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk/pd' + ' ' + '+' + ' '+'0'+' ' + '16' + ' '
        #16

        if (drug_interaction[2].text == drug_name + judge17_1 + drug_name_2 + judge17_2):
            result_str += drug_pri_id + ' ' + \
                          'pd/tox' + ' ' + '-' + ' ' +'1'+' '+ '17' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge17_1 + drug_name + judge17_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd/tox' + ' ' + '-' + ' '+'1'+' ' + '17' + ' '
        #17

        if (drug_interaction[2].text == drug_name + judge18_1 + drug_name_2 + judge18_2):
            result_str += drug_pri_id + ' ' + \
                          'pd/tox' + ' ' + '+' + ' ' +'1'+' '+ '18' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge18_1 + drug_name + judge18_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' ' + '18' + ' '
        #18

        if (drug_interaction[2].text == drug_name + judge19_1 + drug_name_2 + judge19_2):
            result_str += drug_pri_id + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' ' + '19' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge19_1 + drug_name + judge19_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' ' + '19' + ' '
        #19

        if (drug_interaction[2].text == drug_name + judge20_1 + drug_name_2 + judge20_2):
            result_str += drug_pri_id + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' ' + '20' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge20_1 + drug_name + judge20_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' ' + '20' + ' '
        #20

        if (drug_interaction[2].text == drug_name + judge21_1 + drug_name_2 + judge21_2):
            result_str += drug_pri_id + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' ' + '21' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge21_1 + drug_name + judge21_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' ' + '21' + ' '
        #21

        if (drug_interaction[2].text == drug_name + judge22_1 + drug_name_2 + judge22_2):
            result_str += drug_pri_id + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' '  + '22' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge22_1 + drug_name + judge22_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' '  + '22' + ' '
        #22

        if (drug_interaction[2].text == drug_name + judge23_1 + drug_name_2 + judge23_2):
            result_str += drug_pri_id + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' '  + '23' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge23_1 + drug_name + judge23_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd/tox' + ' ' + '+' + ' '+'1'+' '  + '23' + ' '
        #23

        if (drug_interaction[2].text == drug_name + judge24_1 + drug_name_2 + judge24_2):
            result_str += drug_pri_id + ' ' + \
                          'pd' + ' ' + '-' + ' '+'0'+' '+ '24' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge24_1 + drug_name + judge24_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd' + ' ' + '-' + ' '+'0'+' '+ '24' + ' '
        #24

        if (drug_interaction[2].text == judge25_1 + drug_name_2 + judge25_2 + drug_name + judge25_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '25' + ' '
        elif (drug_interaction[2].text == judge25_1 + drug_name + judge25_2 + drug_name_2 + judge25_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '25' + ' '
        #25

        if (drug_interaction[2].text == judge26_1 + drug_name + judge26_2 + drug_name_2 + judge26_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '26' + ' '
        elif (drug_interaction[2].text == judge26_1 + drug_name_2 + judge26_2 + drug_name + judge26_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '26' + ' '
        #26

        if (drug_interaction[2].text == judge27_1 + drug_name + judge27_2 + drug_name_2 + judge27_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '27' + ' '
        elif (drug_interaction[2].text == judge27_1 + drug_name_2 + judge27_2 + drug_name + judge27_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '27' + ' '
        #27

        if (drug_interaction[2].text == judge28_1 + drug_name_2 + judge28_2 + drug_name + judge28_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '28' + ' '
        elif (drug_interaction[2].text == judge28_1 + drug_name + judge28_2 + drug_name_2 + judge28_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '28' + ' '
        #28

        if (drug_interaction[2].text == judge29_1 + drug_name + judge29_2 + drug_name_2 + judge29_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '29' + ' '
        elif (drug_interaction[2].text == judge29_1 + drug_name_2 + judge29_2 + drug_name + judge29_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '29' + ' '
        #29

        if (drug_interaction[2].text == judge30_1 + drug_name_2 + judge30_2 + drug_name + judge30_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '30' + ' '
        elif (drug_interaction[2].text == judge30_1 + drug_name + judge30_2 + drug_name_2 + judge30_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '30' + ' '
        #30

        if (drug_interaction[2].text == judge31_1 + drug_name + judge31_2 + drug_name_2 + judge31_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' '+ '31' + ' '
        elif (drug_interaction[2].text == judge31_1 + drug_name_2 + judge31_2 + drug_name + judge31_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '31' + ' '
        #31

        if (drug_interaction[2].text == judge32_1 + drug_name + judge32_2 + drug_name_2 + judge32_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '32' + ' '
        elif (drug_interaction[2].text == judge32_1 + drug_name_2 + judge32_2 + drug_name + judge32_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' '+'0'+' ' + '32' + ' '
        #32

        if (drug_interaction[2].text == drug_name + judge33_1 + drug_name_2 + judge33_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '33' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge33_1 + drug_name + judge33_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '33' + ' '
        #33

        if (drug_interaction[2].text == drug_name + judge34_1 + drug_name_2 + judge34_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' +'1'+' '+ '34' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge34_1 + drug_name + judge34_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '34' + ' '
        #34

        if (drug_interaction[2].text == drug_name + judge35_1 + drug_name_2 + judge35_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '35' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge35_1 + drug_name + judge35_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '35' + ' '
        #35

        if (drug_interaction[2].text == drug_name + judge36_1 + drug_name_2 + judge36_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '36' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge36_1 + drug_name + judge36_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '36' + ' '
        #36

        if (drug_interaction[2].text == drug_name + judge37_1 + drug_name_2 + judge37_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '37' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge37_1 + drug_name + judge37_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '37' + ' '
        #37

        if (drug_interaction[2].text == drug_name + judge38_1 + drug_name_2 + judge38_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '38' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge38_1 + drug_name + judge38_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '38' + ' '
        #38

        if (drug_interaction[2].text == drug_name + judge39_1 + drug_name_2 + judge39_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '39' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge39_1 + drug_name + judge39_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '39' + ' '
        #39

        if (drug_interaction[2].text == drug_name + judge40_1 + drug_name_2 + judge40_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '40' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge40_1 + drug_name + judge40_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '40' + ' '
        #40

        if (drug_interaction[2].text == drug_name + judge41_1 + drug_name_2 + judge41_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '41' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge41_1 + drug_name + judge41_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '41' + ' '
        #41

        if (drug_interaction[2].text == drug_name + judge42_1 + drug_name_2 + judge42_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '42' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge42_1 + drug_name + judge42_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' '+'1'+' ' + '42' + ' '
        #42

        if (drug_interaction[2].text == drug_name + judge43_1 + drug_name_2 + judge43_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '43' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge43_1 + drug_name + judge43_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '43' + ' '
        #43

        if (drug_interaction[2].text == drug_name + judge44_1 + drug_name_2 + judge44_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '44' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge44_1 + drug_name + judge44_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '44' + ' '
        #44

        if (drug_interaction[2].text == drug_name + judge45_1 + drug_name_2 + judge45_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '45' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge45_1 + drug_name + judge45_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' +'1'+' '+ '45' + ' '
        #45

        if (drug_interaction[2].text == drug_name + judge46_1 + drug_name_2 + judge46_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' +'1'+' ' + '46' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge46_1 + drug_name + judge46_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' +'1'+' ' + '46' + ' '
        #46

        if (drug_interaction[2].text == drug_name + judge47_1 + drug_name_2 + judge47_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '47' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge47_1 + drug_name + judge47_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '47' + ' '
        #47

        if (drug_interaction[2].text == drug_name + judge48_1 + drug_name_2 + judge48_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '48' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge48_1 + drug_name + judge48_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '48' + ' '
        #48

        if (drug_interaction[2].text == drug_name + judge49_1 + drug_name_2 + judge49_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '49' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge49_1 + drug_name + judge49_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '49' + ' '
        #49

        if (drug_interaction[2].text == drug_name + judge50_1 + drug_name_2 + judge50_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '50' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge50_1 + drug_name + judge50_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '50' + ' '
        #50

        if (drug_interaction[2].text == drug_name + judge51_1 + drug_name_2 + judge51_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '51' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge51_1 + drug_name + judge51_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '51' + ' '
        #51

        if (drug_interaction[2].text == drug_name + judge52_1 + drug_name_2 + judge52_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '52' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge52_1 + drug_name + judge52_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '52' + ' '
        #52

        if (drug_interaction[2].text == drug_name + judge53_1 + drug_name_2 + judge53_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '53' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge53_1 + drug_name + judge53_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '53' + ' '
        #53

        if (drug_interaction[2].text == drug_name + judge54_1 + drug_name_2 + judge54_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '54' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge54_1 + drug_name + judge54_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '54' + ' '
        #54

        if (drug_interaction[2].text == drug_name + judge55_1 + drug_name_2 + judge55_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '55' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge55_1 + drug_name + judge55_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '55' + ' '
        #55

        if (drug_interaction[2].text == drug_name + judge56_1 + drug_name_2 + judge56_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '56' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge56_1 + drug_name + judge56_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' '+'1'+' ' + '56' + ' '
        #56

        if (drug_interaction[2].text == drug_name + judge57_1 + drug_name_2 + judge57_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '57' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge57_1 + drug_name + judge57_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '57' + ' '
        #57

        if (drug_interaction[2].text == drug_name + judge58_1 + drug_name_2 + judge58_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '58' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge58_1 + drug_name + judge58_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '58' + ' '
        #58

        if (drug_interaction[2].text == drug_name + judge59_1 + drug_name_2 + judge59_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '59' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge59_1 + drug_name + judge59_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '59' + ' '
        #59

        if (drug_interaction[2].text == drug_name + judge60_1 + drug_name_2 + judge60_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '60' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge60_1 + drug_name + judge60_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '60' + ' '
        #60

        if (drug_interaction[2].text == drug_name + judge61_1 + drug_name_2 + judge61_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '61' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge61_1 + drug_name + judge61_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '61' + ' '
        #61

        if (drug_interaction[2].text == drug_name + judge62_1 + drug_name_2 + judge62_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '62' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge62_1 + drug_name + judge62_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '62' + ' '
        #62

        if (drug_interaction[2].text == drug_name + judge63_1 + drug_name_2 + judge63_2):
            result_str += drug_pri_id + ' ' + \
                           'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '63' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge63_1 + drug_name + judge63_2):
            result_str += drug_interaction[0].text + ' ' + \
                           'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '63' + ' '
        #63

        if (drug_interaction[2].text == drug_name + judge64_1 + drug_name_2 + judge64_2):
            result_str += drug_pri_id + ' ' + \
                           'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '64' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge64_1 + drug_name + judge64_2):
            result_str += drug_interaction[0].text + ' ' + \
                           'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '64' + ' '
        #64

        if (drug_interaction[2].text == drug_name + judge65_1 + drug_name_2 + judge65_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '65' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge65_1 + drug_name + judge65_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '65' + ' '
        #65

        if (drug_interaction[2].text == drug_name + judge66_1 + drug_name_2 + judge66_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '66' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge66_1 + drug_name + judge66_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '66' + ' '
        #66

        if (drug_interaction[2].text == drug_name + judge67_1 + drug_name_2 + judge67_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '67' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge67_1 + drug_name + judge67_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '67' + ' '
        #67

        if (drug_interaction[2].text == drug_name + judge68_1 + drug_name_2 + judge68_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '68' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge68_1 + drug_name + judge68_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '68' + ' '
        #68

        if (drug_interaction[2].text == drug_name + judge69_1 + drug_name_2 + judge69_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '69' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge69_1 + drug_name + judge69_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '69' + ' '
        #69

        if (drug_interaction[2].text == drug_name + judge70_1 + drug_name_2 + judge70_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '70' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge70_1 + drug_name + judge70_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '70' + ' '
        #70

        if (drug_interaction[2].text == drug_name + judge71_1 + drug_name_2 + judge71_2):
            result_str += drug_pri_id + ' ' + \
                           'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '71' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge71_1 + drug_name + judge71_2):
            result_str += drug_interaction[0].text + ' ' + \
                           'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '71' + ' '
        #71

        if (drug_interaction[2].text == drug_name + judge72_1 + drug_name_2 + judge72_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '72' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge72_1 + drug_name + judge72_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '72' + ' '
        #72

        if (drug_interaction[2].text == drug_name + judge73_1 + drug_name_2 + judge73_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '73' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge73_1 + drug_name + judge73_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '73' + ' '
        #73

        if (drug_interaction[2].text == drug_name + judge74_1 + drug_name_2 + judge74_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '74' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge74_1 + drug_name + judge74_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '74' + ' '
        #74

        if (drug_interaction[2].text == drug_name + judge75_1 + drug_name_2 + judge75_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '75' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge75_1 + drug_name + judge75_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '75' + ' '
        #75

        if (drug_interaction[2].text == drug_name + judge76_1 + drug_name_2 + judge76_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '76' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge76_1 + drug_name + judge76_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '76' + ' '
        #76

        if (drug_interaction[2].text == drug_name + judge77_1 + drug_name_2 + judge77_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '77' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge77_1 + drug_name + judge77_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '77' + ' '
        #77

        if (drug_interaction[2].text == drug_name + judge78_1 + drug_name_2 + judge78_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '78' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge78_1 + drug_name + judge78_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '78' + ' '
        #78

        if (drug_interaction[2].text == drug_name + judge79_1 + drug_name_2 + judge79_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '79' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge79_1 + drug_name + judge79_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '79' + ' '
        #79

        if (drug_interaction[2].text == drug_name + judge80_1 + drug_name_2 + judge80_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '80' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge80_1 + drug_name + judge80_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '80' + ' '
        #80

        if (drug_interaction[2].text == drug_name + judge81_1 + drug_name_2 + judge81_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '81' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge81_1 + drug_name + judge81_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '81' + ' '
        #81

        if (drug_interaction[2].text == drug_name + judge82_1 + drug_name_2 + judge82_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '82' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge82_1 + drug_name + judge82_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '82' + ' '
        #82

        if (drug_interaction[2].text == drug_name + judge83_1 + drug_name_2 + judge83_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '83' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge83_1 + drug_name + judge83_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '83' + ' '
        #83

        if (drug_interaction[2].text == drug_name + judge84_1 + drug_name_2 + judge84_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '84' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge84_1 + drug_name + judge84_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '84' + ' '
        #84

        if (drug_interaction[2].text == drug_name + judge85_1 + drug_name_2 + judge85_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '85' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge85_1 + drug_name + judge85_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '85' + ' '
        #85

        if (drug_interaction[2].text == drug_name + judge86_1 + drug_name_2 + judge86_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '86' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge86_1 + drug_name + judge86_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '86' + ' '
        #86

        if (drug_interaction[2].text == judge87_1+ drug_name+ judge87_2 + drug_name_2 + judge87_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '87' + ' '
        elif (drug_interaction[2].text == judge87_1+ drug_name_2+ judge87_2 + drug_name + judge87_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '87' + ' '
        #87

        if (drug_interaction[2].text == judge88_1+ drug_name+ judge88_2 + drug_name_2 + judge88_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '88' + ' '
        elif (drug_interaction[2].text == judge88_1+ drug_name_2+ judge88_2 + drug_name + judge88_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '88' + ' '
        #88

        if (drug_interaction[2].text == judge89_1+ drug_name+ judge89_2 + drug_name_2 + judge89_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '89' + ' '
        elif (drug_interaction[2].text == judge89_1+ drug_name_2+ judge89_2 + drug_name + judge89_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '89' + ' '
        #89

        if (drug_interaction[2].text == judge90_1+ drug_name+ judge90_2 + drug_name_2 + judge90_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '90' + ' '
        elif (drug_interaction[2].text == judge90_1+ drug_name_2+ judge90_2 + drug_name + judge90_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '90' + ' '
        #90

        if (drug_interaction[2].text == judge91_1+ drug_name+ judge91_2 + drug_name_2 + judge91_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '91' + ' '
        elif (drug_interaction[2].text == judge91_1+ drug_name_2+ judge91_2 + drug_name + judge91_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '91' + ' '
        #91

        if (drug_interaction[2].text == judge92_1+ drug_name+ judge92_2 + drug_name_2 + judge92_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '92' + ' '
        elif (drug_interaction[2].text == judge92_1+ drug_name_2+ judge92_2 + drug_name + judge92_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '92' + ' '
        #92

        if (drug_interaction[2].text == judge93_1+ drug_name+ judge93_2 + drug_name_2 + judge93_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '93' + ' '
        elif (drug_interaction[2].text == judge93_1+ drug_name_2+ judge93_2 + drug_name + judge93_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '93' + ' '
        #93

        if (drug_interaction[2].text == judge94_1+ drug_name+ judge94_2 + drug_name_2 + judge94_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '94' + ' '
        elif (drug_interaction[2].text == judge94_1+ drug_name_2+ judge94_2 + drug_name + judge94_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '94' + ' '
        #94

        if (drug_interaction[2].text == judge95_1+ drug_name+ judge95_2 + drug_name_2 + judge95_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' '+ '0' + ' ' + '95' + ' '
        elif (drug_interaction[2].text == judge95_1+ drug_name_2+ judge95_2 + drug_name + judge95_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' '+ '0' + ' ' + '95' + ' '
        #95

        if (drug_interaction[2].text == judge96_1+ drug_name+ judge96_2 + drug_name_2 + judge96_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' '+ '0' + ' ' + '96' + ' '
        elif (drug_interaction[2].text == judge96_1+ drug_name_2+ judge96_2 + drug_name + judge96_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' '+ '0' + ' '+ '96' + ' '
        #96

        if (drug_interaction[2].text == judge97_1 + drug_name + judge97_2 + drug_name_2 + judge97_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '97' + ' '
        elif (drug_interaction[2].text == judge97_1 + drug_name_2 + judge97_2 + drug_name + judge97_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '97' + ' '
        # 97

        if (drug_interaction[2].text == judge98_1 + drug_name + judge98_2 + drug_name_2 + judge98_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '98' + ' '
        elif (drug_interaction[2].text == judge98_1 + drug_name_2 + judge98_2 + drug_name + judge98_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '98' + ' '
        # 98

        if (drug_interaction[2].text == judge99_1 + drug_name + judge99_2 + drug_name_2 + judge99_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '99' + ' '
        elif (drug_interaction[2].text == judge99_1 + drug_name_2 + judge99_2 + drug_name + judge99_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '99' + ' '
        # 99

        if (drug_interaction[2].text == judge100_1 + drug_name + judge100_2 + drug_name_2 + judge100_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '100' + ' '
        elif (drug_interaction[2].text == judge100_1 + drug_name_2 + judge100_2 + drug_name + judge100_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '100' + ' '
        # 100

        if (drug_interaction[2].text == judge101_1 + drug_name + judge101_2 + drug_name_2 + judge101_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '101' + ' '
        elif (drug_interaction[2].text == judge101_1 + drug_name_2 + judge101_2 + drug_name + judge101_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '101' + ' '
        # 101

        if (drug_interaction[2].text == judge102_1 + drug_name + judge102_2 + drug_name_2 + judge102_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '102' + ' '
        elif (drug_interaction[2].text == judge102_1 + drug_name_2 + judge102_2 + drug_name + judge102_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '102' + ' '
        # 102

        if (drug_interaction[2].text == judge103_1 + drug_name + judge103_2 + drug_name_2 + judge103_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '103' + ' '
        elif (drug_interaction[2].text == judge103_1 + drug_name_2 + judge103_2 + drug_name + judge103_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '103' + ' '
        # 103

        if (drug_interaction[2].text == judge104_1 + drug_name + judge104_2 + drug_name_2 + judge104_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '104' + ' '
        elif (drug_interaction[2].text == judge104_1 + drug_name_2 + judge104_2 + drug_name + judge104_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '104' + ' '
        # 104

        if (drug_interaction[2].text == judge105_1 + drug_name + judge105_2 + drug_name_2 + judge105_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '105' + ' '
        elif (drug_interaction[2].text == judge105_1 + drug_name_2 + judge105_2 + drug_name + judge105_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '105' + ' '
        # 105

        if (drug_interaction[2].text == judge106_1 + drug_name + judge106_2 + drug_name_2 + judge106_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '106' + ' '
        elif (drug_interaction[2].text == judge106_1 + drug_name_2 + judge106_2 + drug_name + judge106_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '106' + ' '
        # 106

        if (drug_interaction[2].text == judge107_1 + drug_name + judge107_2 + drug_name_2 + judge107_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '107' + ' '
        elif (drug_interaction[2].text == judge107_1 + drug_name_2 + judge107_2 + drug_name + judge107_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '107' + ' '
        # 107

        if (drug_interaction[2].text == judge108_1 + drug_name + judge108_2 + drug_name_2 + judge108_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '108' + ' '
        elif (drug_interaction[2].text == judge108_1 + drug_name_2 + judge108_2 + drug_name + judge108_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '108' + ' '
        # 108

        if (drug_interaction[2].text == judge109_1 + drug_name + judge109_2 + drug_name_2 + judge109_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '109' + ' '
        elif (drug_interaction[2].text == judge109_1 + drug_name_2 + judge109_2 + drug_name + judge109_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '109' + ' '
        # 109

        if (drug_interaction[2].text == judge110_1 + drug_name + judge110_2 + drug_name_2 + judge110_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '110' + ' '
        elif (drug_interaction[2].text == judge110_1 + drug_name_2 + judge110_2 + drug_name + judge110_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '110' + ' '
        # 110

        if (drug_interaction[2].text == judge111_1 + drug_name + judge111_2 + drug_name_2 + judge111_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '111' + ' '
        elif (drug_interaction[2].text == judge111_1 + drug_name_2 + judge111_2 + drug_name + judge111_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '111' + ' '
        # 111

        if (drug_interaction[2].text == judge112_1 + drug_name + judge112_2 + drug_name_2 + judge112_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '112' + ' '
        elif (drug_interaction[2].text == judge112_1 + drug_name_2 + judge112_2 + drug_name + judge112_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '112' + ' '
        # 112

        if (drug_interaction[2].text == drug_name + judge113_1 + drug_name_2 + judge113_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '113' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge113_1 + drug_name + judge113_2):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '113' + ' '
        # 113

        if (drug_interaction[2].text == judge114_1 + drug_name + judge114_2 + drug_name_2 + judge114_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '114' + ' '
        elif (drug_interaction[2].text == judge114_1 + drug_name_2 + judge114_2 + drug_name + judge114_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '114' + ' '
        # 114

        if (drug_interaction[2].text == judge115_1 + drug_name + judge115_2 + drug_name_2 + judge115_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '115' + ' '
        elif (drug_interaction[2].text == judge115_1 + drug_name_2 + judge115_2 + drug_name + judge115_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '115' + ' '
        # 115

        if (drug_interaction[2].text == judge116_1 + drug_name + judge116_2 + drug_name_2 + judge116_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '116' + ' '
        elif (drug_interaction[2].text == judge116_1 + drug_name_2 + judge116_2 + drug_name + judge116_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '116' + ' '
        # 116

        if (drug_interaction[2].text == judge117_1 + drug_name + judge117_2 + drug_name_2 + judge117_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '117' + ' '
        elif (drug_interaction[2].text == judge117_1 + drug_name_2 + judge117_2 + drug_name + judge117_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '117' + ' '
        # 117

        if (drug_interaction[2].text == judge118_1 + drug_name + judge118_2 + drug_name_2 + judge118_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '118' + ' '
        elif (drug_interaction[2].text == judge118_1 + drug_name_2 + judge118_2 + drug_name + judge118_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '118' + ' '
        # 118

        if (drug_interaction[2].text == judge119_1 + drug_name + judge119_2 + drug_name_2 + judge119_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '119' + ' '
        elif (drug_interaction[2].text == judge119_1 + drug_name_2 + judge119_2 + drug_name + judge119_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '119' + ' '
        # 119

        if (drug_interaction[2].text == judge120_1 + drug_name + judge120_2 + drug_name_2 + judge120_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '120' + ' '
        elif (drug_interaction[2].text == judge120_1 + drug_name_2 + judge120_2 + drug_name + judge120_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '120' + ' '
        # 120

        if (drug_interaction[2].text == judge121_1 + drug_name + judge121_2 + drug_name_2 + judge121_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '121' + ' '
        elif (drug_interaction[2].text == judge121_1 + drug_name_2 + judge121_2 + drug_name + judge121_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '121' + ' '
        # 121

        if (drug_interaction[2].text == judge122_1 + drug_name + judge122_2 + drug_name_2 + judge122_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '122' + ' '
        elif (drug_interaction[2].text == judge122_1 + drug_name_2 + judge122_2 + drug_name + judge122_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '122' + ' '
        # 122

        if (drug_interaction[2].text == judge123_1 + drug_name + judge123_2 + drug_name_2 + judge123_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '123' + ' '
        elif (drug_interaction[2].text == judge123_1 + drug_name_2 + judge123_2 + drug_name + judge123_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '123' + ' '
        # 123

        if (drug_interaction[2].text == judge124_1 + drug_name + judge124_2 + drug_name_2 + judge124_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '124' + ' '
        elif (drug_interaction[2].text == judge124_1 + drug_name_2 + judge124_2 + drug_name + judge124_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '124' + ' '
        # 124

        if (drug_interaction[2].text == judge125_1 + drug_name + judge125_2 + drug_name_2 + judge125_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '125' + ' '
        elif (drug_interaction[2].text == judge125_1 + drug_name_2 + judge125_2 + drug_name + judge125_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '125' + ' '
        # 125

        if (drug_interaction[2].text == judge126_1 + drug_name + judge126_2 + drug_name_2 + judge126_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '126' + ' '
        elif (drug_interaction[2].text == judge126_1 + drug_name_2 + judge126_2 + drug_name + judge126_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '126' + ' '
        # 126

        if (drug_interaction[2].text == drug_name + judge127_1 + drug_name_2 + judge127_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '0' + ' ' + '127' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge127_1 + drug_name + judge127_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '0' + ' ' + '127' + ' '
        # 127

        if (drug_interaction[2].text == judge128_1 + drug_name + judge128_2 + drug_name_2 + judge128_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '128' + ' '
        elif (drug_interaction[2].text == judge128_1 + drug_name_2 + judge128_2 + drug_name + judge128_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '128' + ' '
        # 128

        if (drug_interaction[2].text == judge129_1 + drug_name + judge129_2 + drug_name_2 + judge129_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '129' + ' '
        elif (drug_interaction[2].text == judge129_1 + drug_name_2 + judge129_2 + drug_name + judge129_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '129' + ' '
        # 129

        if (drug_interaction[2].text == judge130_1 + drug_name + judge130_2 + drug_name_2 + judge130_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '130' + ' '
        elif (drug_interaction[2].text == judge130_1 + drug_name_2 + judge130_2 + drug_name + judge130_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '130' + ' '
        # 130

        if (drug_interaction[2].text == judge131_1 + drug_name + judge131_2 + drug_name_2 + judge131_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '131' + ' '
        elif (drug_interaction[2].text == judge131_1 + drug_name_2 + judge131_2 + drug_name + judge131_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '131' + ' '
        # 131

        if (drug_interaction[2].text == judge132_1 + drug_name + judge132_2 + drug_name_2 + judge132_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '132' + ' '
        elif (drug_interaction[2].text == judge132_1 + drug_name_2 + judge132_2 + drug_name + judge132_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '132' + ' '
        # 132

        if (drug_interaction[2].text == drug_name + judge133_1 + drug_name_2 + judge133_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'PD' + ' ' + '+' + ' ' + '1' + ' ' + '133' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge133_1 + drug_name + judge133_2):
            result_str += drug_pri_id + ' ' + \
                          'PD' + ' ' + '+' + ' ' + '1' + ' ' + '133' + ' '
        # 133

        if (drug_interaction[2].text == judge134_1 + drug_name + judge134_2 + drug_name_2 + judge134_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '134' + ' '
        elif (drug_interaction[2].text == judge134_1 + drug_name_2 + judge134_2 + drug_name + judge134_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '134' + ' '
        # 134

        if (drug_interaction[2].text == judge135_1 + drug_name + judge135_2 + drug_name_2 + judge135_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '135' + ' '
        elif (drug_interaction[2].text == judge135_1 + drug_name_2 + judge135_2 + drug_name + judge135_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '135' + ' '
        # 135

        if (drug_interaction[2].text == judge136_1 + drug_name + judge136_2 + drug_name_2 + judge136_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '136' + ' '
        elif (drug_interaction[2].text == judge136_1 + drug_name_2 + judge136_2 + drug_name + judge136_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '136' + ' '
        # 136

        if (drug_interaction[2].text == judge137_1 + drug_name + judge137_2 + drug_name_2 + judge137_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '137' + ' '
        elif (drug_interaction[2].text == judge137_1 + drug_name_2 + judge137_2 + drug_name + judge137_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '137' + ' '
        # 137

        if (drug_interaction[2].text == judge138_1 + drug_name + judge138_2 + drug_name_2 + judge138_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '-' + ' ' + '0' + ' ' + '138' + ' '
        elif (drug_interaction[2].text == judge138_1 + drug_name_2 + judge138_2 + drug_name + judge138_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '-' + ' ' + '0' + ' ' + '138' + ' '
        # 138

        if (drug_interaction[2].text == judge139_1 + drug_name + judge139_2 + drug_name_2 + judge139_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '139' + ' '
        elif (drug_interaction[2].text == judge139_1 + drug_name_2 + judge139_2 + drug_name + judge139_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '139' + ' '
        # 139

        if (drug_interaction[2].text == drug_name + judge140_1 + drug_name_2 + judge140_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '140' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge140_1 + drug_name + judge140_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '140' + ' '
        # 140

        if (drug_interaction[2].text == judge141_1 + drug_name + judge141_2 + drug_name_2 + judge141_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '141' + ' '
        elif (drug_interaction[2].text == judge141_1 + drug_name_2 + judge141_2 + drug_name + judge141_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '141' + ' '
        # 141

        if (drug_interaction[2].text == judge142_1 + drug_name + judge142_2 + drug_name_2 + judge142_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '142' + ' '
        elif (drug_interaction[2].text == judge142_1 + drug_name_2 + judge142_2 + drug_name + judge142_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '142' + ' '
        # 142

        if (drug_interaction[2].text == judge143_1 + drug_name + judge143_2 + drug_name_2 + judge143_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '143' + ' '
        elif (drug_interaction[2].text == judge143_1 + drug_name_2 + judge143_2 + drug_name + judge143_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '143' + ' '
        # 143

        if (drug_interaction[2].text == judge144_1 + drug_name + judge144_2 + drug_name_2 + judge144_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '144' + ' '
        elif (drug_interaction[2].text == judge144_1 + drug_name_2 + judge144_2 + drug_name + judge144_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '144' + ' '
        # 144

        if (drug_interaction[2].text == judge145_1 + drug_name + judge145_2 + drug_name_2 + judge145_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '145' + ' '
        elif (drug_interaction[2].text == judge145_1 + drug_name_2 + judge145_2 + drug_name + judge145_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '145' + ' '
        # 145

        if (drug_interaction[2].text == judge146_1 + drug_name + judge146_2 + drug_name_2 + judge146_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '146' + ' '
        elif (drug_interaction[2].text == judge146_1 + drug_name_2 + judge146_2 + drug_name + judge146_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '146' + ' '
        # 146

        if (drug_interaction[2].text == judge147_1 + drug_name + judge147_2 + drug_name_2 + judge147_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '147' + ' '
        elif (drug_interaction[2].text == judge147_1 + drug_name_2 + judge147_2 + drug_name + judge147_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '147' + ' '
        # 147

        if (drug_interaction[2].text == judge148_1 + drug_name + judge148_2 + drug_name_2 + judge148_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '148' + ' '
        elif (drug_interaction[2].text == judge148_1 + drug_name_2 + judge148_2 + drug_name + judge148_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '148' + ' '
        # 148

        if (drug_interaction[2].text == judge149_1 + drug_name + judge149_2 + drug_name_2 + judge149_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '149' + ' '
        elif (drug_interaction[2].text == judge149_1 + drug_name_2 + judge149_2 + drug_name + judge149_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '149' + ' '
        # 149

        if (drug_interaction[2].text == judge150_1 + drug_name + judge150_2 + drug_name_2 + judge150_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '150' + ' '
        elif (drug_interaction[2].text == judge150_1 + drug_name_2 + judge150_2 + drug_name + judge150_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '150' + ' '
        # 150

        if (drug_interaction[2].text == judge151_1 + drug_name + judge151_2 + drug_name_2 + judge151_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '151' + ' '
        elif (drug_interaction[2].text == judge151_1 + drug_name_2 + judge151_2 + drug_name + judge151_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '151' + ' '
        # 151

        if (drug_interaction[2].text == judge152_1 + drug_name + judge152_2 + drug_name_2 + judge152_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '152' + ' '
        elif (drug_interaction[2].text == judge152_1 + drug_name_2 + judge152_2 + drug_name + judge152_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '152' + ' '
        # 152

        if (drug_interaction[2].text == judge153_1 + drug_name + judge153_2 + drug_name_2 + judge153_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '153' + ' '
        elif (drug_interaction[2].text == judge153_1 + drug_name_2 + judge153_2 + drug_name + judge153_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '153' + ' '
        # 153

        if (drug_interaction[2].text == judge154_1 + drug_name + judge154_2 + drug_name_2 + judge154_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '154' + ' '
        elif (drug_interaction[2].text == judge154_1 + drug_name_2 + judge154_2 + drug_name + judge154_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '154' + ' '
        # 154

        if (drug_interaction[2].text == judge155_1 + drug_name + judge155_2 + drug_name_2 + judge155_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '155' + ' '
        elif (drug_interaction[2].text == judge155_1 + drug_name_2 + judge155_2 + drug_name + judge155_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '155' + ' '
        # 155

        if (drug_interaction[2].text == judge156_1 + drug_name + judge156_2 + drug_name_2 + judge156_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '156' + ' '
        elif (drug_interaction[2].text == judge156_1 + drug_name_2 + judge156_2 + drug_name + judge156_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '156' + ' '
        # 156

        if (drug_interaction[2].text == judge157_1 + drug_name + judge157_2 + drug_name_2 + judge157_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '157' + ' '
        elif (drug_interaction[2].text == judge157_1 + drug_name_2 + judge157_2 + drug_name + judge157_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '157' + ' '
        # 157

        if (drug_interaction[2].text == drug_name + judge158_1 + drug_name_2 + judge158_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '158' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge158_1 + drug_name + judge158_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '158' + ' '
        # 158

        if (drug_interaction[2].text == judge159_1 + drug_name + judge159_2 + drug_name_2 + judge159_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '159' + ' '
        elif (drug_interaction[2].text == judge159_1 + drug_name_2 + judge159_2 + drug_name + judge159_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '159' + ' '
        # 159

        if (drug_interaction[2].text == drug_name + judge160_1 + drug_name_2 + judge160_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '1' + ' ' + '160' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge160_1 + drug_name + judge160_2):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '1' + ' ' + '160' + ' '
        # 160

        if (drug_interaction[2].text == drug_name + judge161_1 + drug_name_2 + judge161_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '161' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge161_1 + drug_name + judge161_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '161' + ' '
        # 161

        if (drug_interaction[2].text == judge162_1 + drug_name + judge162_2 + drug_name_2 + judge162_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '162' + ' '
        elif (drug_interaction[2].text == judge162_1 + drug_name_2 + judge162_2 + drug_name + judge162_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '162' + ' '
        # 162

        if (drug_interaction[2].text == judge163_1 + drug_name + judge163_2 + drug_name_2 + judge163_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '163' + ' '
        elif (drug_interaction[2].text == judge163_1 + drug_name_2 + judge163_2 + drug_name + judge163_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '163' + ' '
        # 163

        if (drug_interaction[2].text == judge164_1 + drug_name + judge164_2 + drug_name_2 + judge164_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '164' + ' '
        elif (drug_interaction[2].text == judge164_1 + drug_name_2 + judge164_2 + drug_name + judge164_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '164' + ' '
        # 164

        if (drug_interaction[2].text == judge165_1 + drug_name + judge165_2 + drug_name_2 + judge165_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '-' + ' ' + '0' + ' ' + '165' + ' '
        elif (drug_interaction[2].text == judge165_1 + drug_name_2 + judge165_2 + drug_name + judge165_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '-' + ' ' + '0' + ' ' + '165' + ' '
        # 165

        if (drug_interaction[2].text == judge166_1 + drug_name + judge166_2 + drug_name_2 + judge166_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '166' + ' '
        elif (drug_interaction[2].text == judge166_1 + drug_name_2 + judge166_2 + drug_name + judge166_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '166' + ' '
        # 166

        if (drug_interaction[2].text == judge167_1 + drug_name + judge167_2 + drug_name_2 + judge167_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '167' + ' '
        elif (drug_interaction[2].text == judge167_1 + drug_name_2 + judge167_2 + drug_name + judge167_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '167' + ' '
        # 167

        if (drug_interaction[2].text == judge168_1 + drug_name + judge168_2 + drug_name_2 + judge168_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' ' + '0' + ' ' + '168' + ' '
        elif (drug_interaction[2].text == judge168_1 + drug_name_2 + judge168_2 + drug_name + judge168_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' ' + '0' + ' ' + '168' + ' '
        # 168

        if (drug_interaction[2].text == judge169_1 + drug_name + judge169_2 + drug_name_2 + judge169_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '169' + ' '
        elif (drug_interaction[2].text == judge169_1 + drug_name_2 + judge169_2 + drug_name + judge169_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '169' + ' '
        # 169

        if (drug_interaction[2].text == judge170_1 + drug_name + judge170_2 + drug_name_2 + judge170_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '170' + ' '
        elif (drug_interaction[2].text == judge170_1 + drug_name_2 + judge170_2 + drug_name + judge170_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '170' + ' '
        # 170

        if (drug_interaction[2].text == judge171_1 + drug_name + judge171_2 + drug_name_2 + judge171_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '171' + ' '
        elif (drug_interaction[2].text == judge171_1 + drug_name_2 + judge171_2 + drug_name + judge171_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '171' + ' '
        # 171

        if (drug_interaction[2].text == judge172_1 + drug_name + judge172_2 + drug_name_2 + judge172_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '172' + ' '
        elif (drug_interaction[2].text == judge172_1 + drug_name_2 + judge172_2 + drug_name + judge172_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '172' + ' '
        # 172

        if (drug_interaction[2].text == judge173_1 + drug_name + judge173_2 + drug_name_2 + judge173_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '173' + ' '
        elif (drug_interaction[2].text == judge173_1 + drug_name_2 + judge173_2 + drug_name + judge173_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '173' + ' '
        # 173

        if (drug_interaction[2].text == judge174_1 + drug_name + judge174_2 + drug_name_2 + judge174_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '174' + ' '
        elif (drug_interaction[2].text == judge174_1 + drug_name_2 + judge174_2 + drug_name + judge174_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '174' + ' '
        # 174

        if (drug_interaction[2].text == judge175_1 + drug_name + judge175_2 + drug_name_2 + judge175_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '175' + ' '
        elif (drug_interaction[2].text == judge175_1 + drug_name_2 + judge175_2 + drug_name + judge175_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '175' + ' '
        # 175

        if (drug_interaction[2].text == judge176_1 + drug_name + judge176_2 + drug_name_2 + judge176_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '176' + ' '
        elif (drug_interaction[2].text == judge176_1 + drug_name_2 + judge176_2 + drug_name + judge176_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '176' + ' '
        # 176

        if (drug_interaction[2].text == drug_name + judge177_1 + drug_name_2 + judge177_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '1' + ' ' + '177' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge177_1 + drug_name + judge177_2):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '1' + ' ' + '177' + ' '
        # 177

        if (drug_interaction[2].text == judge178_1 + drug_name + judge178_2 + drug_name_2 + judge178_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '0' + ' ' + '178' + ' '
        elif (drug_interaction[2].text == judge178_1 + drug_name_2 + judge178_2 + drug_name + judge178_3):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '0' + ' ' + '178' + ' '
        # 178

        if (drug_interaction[2].text == drug_name + judge179_1 + drug_name_2 + judge179_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '179' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge179_1 + drug_name + judge179_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '179' + ' '
        # 179

        if (drug_interaction[2].text == judge180_1 + drug_name + judge180_2 + drug_name_2 + judge180_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '180' + ' '
        elif (drug_interaction[2].text == judge180_1 + drug_name_2 + judge180_2 + drug_name + judge180_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '180' + ' '
        # 180

        if (drug_interaction[2].text == judge181_1 + drug_name + judge181_2 + drug_name_2 + judge181_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '-' + ' ' + '0' + ' ' + '181' + ' '
        elif (drug_interaction[2].text == judge181_1 + drug_name_2 + judge181_2 + drug_name + judge181_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '-' + ' ' + '0' + ' ' + '181' + ' '
        # 181

        if (drug_interaction[2].text == judge182_1 + drug_name + judge182_2 + drug_name_2 + judge182_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '182' + ' '
        elif (drug_interaction[2].text == judge182_1 + drug_name_2 + judge182_2 + drug_name + judge182_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '182' + ' '
        # 182

        if (drug_interaction[2].text == judge183_1 + drug_name + judge183_2 + drug_name_2 + judge183_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '183' + ' '
        elif (drug_interaction[2].text == judge183_1 + drug_name_2 + judge183_2 + drug_name + judge183_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '183' + ' '
        # 183

        if (drug_interaction[2].text == judge184_1 + drug_name + judge184_2 + drug_name_2 + judge184_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '184' + ' '
        elif (drug_interaction[2].text == judge184_1 + drug_name_2 + judge184_2 + drug_name + judge184_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '184' + ' '
        # 184

        if (drug_interaction[2].text == drug_name + judge185_1 + drug_name_2 + judge185_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '-' + ' ' + '1' + ' ' + '185' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge185_1 + drug_name + judge185_2):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '-' + ' ' + '1' + ' ' + '185' + ' '
        # 185

        if (drug_interaction[2].text == judge186_1 + drug_name + judge186_2 + drug_name_2 + judge186_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '186' + ' '
        elif (drug_interaction[2].text == judge186_1 + drug_name_2 + judge186_2 + drug_name + judge186_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '186' + ' '
        # 186

        if (drug_interaction[2].text == judge187_1 + drug_name + judge187_2 + drug_name_2 + judge187_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '187' + ' '
        elif (drug_interaction[2].text == judge187_1 + drug_name_2 + judge187_2 + drug_name + judge187_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '187' + ' '
        # 187

        if (drug_interaction[2].text == judge188_1 + drug_name + judge188_2 + drug_name_2 + judge188_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '0' + ' ' + '188' + ' '
        elif (drug_interaction[2].text == judge188_1 + drug_name_2 + judge188_2 + drug_name + judge188_3):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '0' + ' ' + '188' + ' '
        # 188

        if (drug_interaction[2].text == judge189_1 + drug_name + judge189_2 + drug_name_2 + judge189_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '189' + ' '
        elif (drug_interaction[2].text == judge189_1 + drug_name_2 + judge189_2 + drug_name + judge189_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '189' + ' '
        # 189

        if (drug_interaction[2].text == judge190_1 + drug_name + judge190_2 + drug_name_2 + judge190_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '190' + ' '
        elif (drug_interaction[2].text == judge190_1 + drug_name_2 + judge190_2 + drug_name + judge190_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '190' + ' '
        # 190

        if (drug_interaction[2].text == drug_name + judge191_1 + drug_name_2 + judge191_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '0' + ' ' + '191' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge191_1 + drug_name + judge191_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '0' + ' ' + '191' + ' '
        # 191

        if (drug_interaction[2].text == drug_name + judge192_1 + drug_name_2 + judge192_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '192' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge192_1 + drug_name + judge192_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '192' + ' '
        # 192

        if (drug_interaction[2].text == judge193_1 + drug_name + judge193_2 + drug_name_2 + judge193_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '193' + ' '
        elif (drug_interaction[2].text == judge193_1 + drug_name_2 + judge193_2 + drug_name + judge193_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '193' + ' '
        # 193

        if (drug_interaction[2].text == judge194_1 + drug_name + judge194_2 + drug_name_2 + judge194_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '194' + ' '
        elif (drug_interaction[2].text == judge194_1 + drug_name_2 + judge194_2 + drug_name + judge194_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '194' + ' '
        # 194

        if (drug_interaction[2].text == judge195_1 + drug_name + judge195_2 + drug_name_2 + judge195_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '195' + ' '
        elif (drug_interaction[2].text == judge195_1 + drug_name_2 + judge195_2 + drug_name + judge195_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '195' + ' '
        # 195

        if (drug_interaction[2].text == drug_name + judge196_1 + drug_name_2 + judge196_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '196' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge196_1 + drug_name + judge196_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '196' + ' '
        # 196

        if (drug_interaction[2].text == judge197_1 + drug_name + judge197_2 + drug_name_2 + judge197_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '197' + ' '
        elif (drug_interaction[2].text == judge197_1 + drug_name_2 + judge197_2 + drug_name + judge197_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '197' + ' '
        # 197

        if (drug_interaction[2].text == judge198_1 + drug_name + judge198_2 + drug_name_2 + judge198_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '198' + ' '
        elif (drug_interaction[2].text == judge198_1 + drug_name_2 + judge198_2 + drug_name + judge198_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '198' + ' '
        # 198

        if (drug_interaction[2].text == judge199_1 + drug_name + judge199_2 + drug_name_2 + judge199_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '199' + ' '
        elif (drug_interaction[2].text == judge199_1 + drug_name_2 + judge199_2 + drug_name + judge199_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '199' + ' '
        # 199

        if (drug_interaction[2].text == judge200_1 + drug_name + judge200_2 + drug_name_2 + judge200_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '200' + ' '
        elif (drug_interaction[2].text == judge200_1 + drug_name_2 + judge200_2 + drug_name + judge200_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '200' + ' '
        # 200

        if (drug_interaction[2].text == judge201_1 + drug_name + judge201_2 + drug_name_2 + judge201_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '201' + ' '
        elif (drug_interaction[2].text == judge201_1 + drug_name_2 + judge201_2 + drug_name + judge201_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '201' + ' '
        # 201

        if (drug_interaction[2].text == judge202_1 + drug_name + judge202_2 + drug_name_2 + judge202_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '202' + ' '
        elif (drug_interaction[2].text == judge202_1 + drug_name_2 + judge202_2 + drug_name + judge202_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '202' + ' '
        # 202

        if (drug_interaction[2].text == judge203_1 + drug_name + judge203_2 + drug_name_2 + judge203_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '203' + ' '
        elif (drug_interaction[2].text == judge203_1 + drug_name_2 + judge203_2 + drug_name + judge203_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '203' + ' '
        # 203

        if (drug_interaction[2].text == judge204_1 + drug_name + judge204_2 + drug_name_2 + judge204_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '204' + ' '
        elif (drug_interaction[2].text == judge204_1 + drug_name_2 + judge204_2 + drug_name + judge204_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '204' + ' '
        # 204

        if (drug_interaction[2].text == judge205_1 + drug_name + judge205_2 + drug_name_2 + judge205_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '205' + ' '
        elif (drug_interaction[2].text == judge205_1 + drug_name_2 + judge205_2 + drug_name + judge205_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '205' + ' '
        # 205

        if (drug_interaction[2].text == drug_name + judge206_1 + drug_name_2 + judge206_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '206' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge206_1 + drug_name + judge206_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '206' + ' '
        # 206

        if (drug_interaction[2].text == drug_name + judge207_1 + drug_name_2 + judge207_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '207' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge207_1 + drug_name + judge207_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '207' + ' '
        # 207

        if (drug_interaction[2].text == judge208_1 + drug_name + judge208_2 + drug_name_2 + judge208_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '-' + ' ' + '0' + ' ' + '208' + ' '
        elif (drug_interaction[2].text == judge208_1 + drug_name_2 + judge208_2 + drug_name + judge208_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '-' + ' ' + '0' + ' ' + '208' + ' '
        # 208

        if (drug_interaction[2].text == judge209_1 + drug_name + judge209_2 + drug_name_2 + judge209_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '209' + ' '
        elif (drug_interaction[2].text == judge209_1 + drug_name_2 + judge209_2 + drug_name + judge209_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '209' + ' '
        # 209

        if (drug_interaction[2].text == judge210_1 + drug_name + judge210_2 + drug_name_2 + judge210_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '210' + ' '
        elif (drug_interaction[2].text == judge210_1 + drug_name_2 + judge210_2 + drug_name + judge210_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '210' + ' '
        # 210

        if (drug_interaction[2].text == judge211_1 + drug_name + judge211_2 + drug_name_2 + judge211_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '211' + ' '
        elif (drug_interaction[2].text == judge211_1 + drug_name_2 + judge211_2 + drug_name + judge211_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '211' + ' '
        # 211

        if (drug_interaction[2].text == judge212_1 + drug_name + judge212_2 + drug_name_2 + judge212_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '212' + ' '
        elif (drug_interaction[2].text == judge212_1 + drug_name_2 + judge212_2 + drug_name + judge212_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '212' + ' '
        # 212

        if (drug_interaction[2].text == judge213_1 + drug_name + judge213_2 + drug_name_2 + judge213_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '213' + ' '
        elif (drug_interaction[2].text == judge213_1 + drug_name_2 + judge213_2 + drug_name + judge213_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '213' + ' '
        # 213

        if (drug_interaction[2].text == drug_name + judge214_1 + drug_name_2 + judge214_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd/tox' + ' ' + '-' + ' ' + '1' + ' ' + '214' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge214_1 + drug_name + judge214_2):
            result_str += drug_pri_id + ' ' + \
                          'pd/tox' + ' ' + '-' + ' ' + '1' + ' ' + '214' + ' '
        # 214

        if (drug_interaction[2].text == judge215_1 + drug_name + judge215_2 + drug_name_2 + judge215_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '215' + ' '
        elif (drug_interaction[2].text == judge215_1 + drug_name_2 + judge215_2 + drug_name + judge215_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '215' + ' '
        # 215

        if (drug_interaction[2].text == judge216_1 + drug_name + judge216_2 + drug_name_2 + judge216_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '216' + ' '
        elif (drug_interaction[2].text == judge216_1 + drug_name_2 + judge216_2 + drug_name + judge216_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '216' + ' '
        # 216

        if (drug_interaction[2].text == judge217_1 + drug_name + judge217_2 + drug_name_2 + judge217_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '217' + ' '
        elif (drug_interaction[2].text == judge217_1 + drug_name_2 + judge217_2 + drug_name + judge217_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '217' + ' '
        # 217

        if (drug_interaction[2].text == judge218_1 + drug_name + judge218_2 + drug_name_2 + judge218_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '218' + ' '
        elif (drug_interaction[2].text == judge218_1 + drug_name_2 + judge218_2 + drug_name + judge218_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '218' + ' '
        # 218

        if (drug_interaction[2].text == judge219_1 + drug_name + judge219_2 + drug_name_2 + judge219_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '219' + ' '
        elif (drug_interaction[2].text == judge219_1 + drug_name_2 + judge219_2 + drug_name + judge219_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '219' + ' '
        # 219

        if (drug_interaction[2].text == judge220_1 + drug_name + judge220_2 + drug_name_2 + judge220_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '220' + ' '
        elif (drug_interaction[2].text == judge220_1 + drug_name_2 + judge220_2 + drug_name + judge220_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '220' + ' '
        # 220

        if (drug_interaction[2].text == judge221_1 + drug_name + judge221_2 + drug_name_2 + judge221_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '221' + ' '
        elif (drug_interaction[2].text == judge221_1 + drug_name_2 + judge221_2 + drug_name + judge221_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '221' + ' '
        # 221

        if (drug_interaction[2].text == drug_name + judge222_1 + drug_name_2 + judge222_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '222' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge222_1 + drug_name + judge222_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '222' + ' '
        # 222

        if (drug_interaction[2].text == drug_name + judge223_1 + drug_name_2 + judge223_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '223' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge223_1 + drug_name + judge223_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '223' + ' '
        # 223

        if (drug_interaction[2].text == drug_name + judge224_1 + drug_name_2 + judge224_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '224' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge224_1 + drug_name + judge224_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '224' + ' '
        # 224

        if (drug_interaction[2].text == judge225_1 + drug_name + judge225_2 + drug_name_2 + judge225_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '225' + ' '
        elif (drug_interaction[2].text == judge225_1 + drug_name_2 + judge225_2 + drug_name + judge225_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '225' + ' '
        # 225

        if (drug_interaction[2].text == drug_name + judge226_1 + drug_name_2 + judge226_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '226' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge226_1 + drug_name + judge226_2):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '226' + ' '
        # 226

        if (drug_interaction[2].text == judge227_1 + drug_name + judge227_2 + drug_name_2 + judge227_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '227' + ' '
        elif (drug_interaction[2].text == judge227_1 + drug_name_2 + judge227_2 + drug_name + judge227_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '227' + ' '
        # 227

        if (drug_interaction[2].text == judge228_1 + drug_name + judge228_2 + drug_name_2 + judge228_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '228' + ' '
        elif (drug_interaction[2].text == judge228_1 + drug_name_2 + judge228_2 + drug_name + judge228_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '228' + ' '
        # 228

        if (drug_interaction[2].text == judge229_1 + drug_name + judge229_2 + drug_name_2 + judge229_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '229' + ' '
        elif (drug_interaction[2].text == judge229_1 + drug_name_2 + judge229_2 + drug_name + judge229_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '229' + ' '
        # 229

        if (drug_interaction[2].text == judge230_1 + drug_name + judge230_2 + drug_name_2 + judge230_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '230' + ' '
        elif (drug_interaction[2].text == judge230_1 + drug_name_2 + judge230_2 + drug_name + judge230_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '230' + ' '
        # 230

        if (drug_interaction[2].text == judge231_1 + drug_name + judge231_2 + drug_name_2 + judge231_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '231' + ' '
        elif (drug_interaction[2].text == judge231_1 + drug_name_2 + judge231_2 + drug_name + judge231_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '231' + ' '
        # 231

        if (drug_interaction[2].text == judge232_1 + drug_name + judge232_2 + drug_name_2 + judge232_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '232' + ' '
        elif (drug_interaction[2].text == judge232_1 + drug_name_2 + judge232_2 + drug_name + judge232_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '232' + ' '
        # 232

        if (drug_interaction[2].text == drug_name + judge233_1 + drug_name_2 + judge233_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '233' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge233_1 + drug_name + judge233_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '233' + ' '
        # 233

        if (drug_interaction[2].text == drug_name + judge234_1 + drug_name_2 + judge234_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '234' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge234_1 + drug_name + judge234_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '234' + ' '
        # 234

        if (drug_interaction[2].text == drug_name + judge235_1 + drug_name_2 + judge235_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '235' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge235_1 + drug_name + judge235_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '235' + ' '
        # 235

        if (drug_interaction[2].text == drug_name + judge236_1 + drug_name_2 + judge236_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '236' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge236_1 + drug_name + judge236_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '236' + ' '
        # 236

        if (drug_interaction[2].text == drug_name + judge237_1 + drug_name_2 + judge237_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '237' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge237_1 + drug_name + judge237_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '237' + ' '
        # 237

        if (drug_interaction[2].text == drug_name + judge238_1 + drug_name_2 + judge238_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '238' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge238_1 + drug_name + judge238_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '238' + ' '
        # 238

        if (drug_interaction[2].text == drug_name + judge239_1 + drug_name_2 + judge239_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '239' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge239_1 + drug_name + judge239_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '239' + ' '
        # 239

        if (drug_interaction[2].text == drug_name + judge240_1 + drug_name_2 + judge240_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '240' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge240_1 + drug_name + judge240_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '240' + ' '
        # 240

        if (drug_interaction[2].text == drug_name + judge241_1 + drug_name_2 + judge241_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '241' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge241_1 + drug_name + judge241_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '241' + ' '
        # 241

        if (drug_interaction[2].text == drug_name + judge242_1 + drug_name_2 + judge242_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '242' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge242_1 + drug_name + judge242_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '242' + ' '
        # 242

        if (drug_interaction[2].text == drug_name + judge243_1 + drug_name_2 + judge243_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '243' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge243_1 + drug_name + judge243_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '243' + ' '
        # 243

        if (drug_interaction[2].text == judge244_1 + drug_name + judge244_2 + drug_name_2 + judge244_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '244' + ' '
        elif (drug_interaction[2].text == judge244_1 + drug_name_2 + judge244_2 + drug_name + judge244_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '244' + ' '
        # 244

        if (drug_interaction[2].text == judge245_1 + drug_name + judge245_2 + drug_name_2 + judge245_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '245' + ' '
        elif (drug_interaction[2].text == judge245_1 + drug_name_2 + judge245_2 + drug_name + judge245_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '245' + ' '
        # 245

        if (drug_interaction[2].text == judge246_1 + drug_name + judge246_2 + drug_name_2 + judge246_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '0' + ' ' + '246' + ' '
        elif (drug_interaction[2].text == judge246_1 + drug_name_2 + judge246_2 + drug_name + judge246_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '1' + ' ' + '246' + ' '
        # 246

        if (drug_interaction[2].text == judge247_1 + drug_name + judge247_2 + drug_name_2 + judge247_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '0' + ' ' + '247' + ' '
        elif (drug_interaction[2].text == judge247_1 + drug_name_2 + judge247_2 + drug_name + judge247_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '1' + ' ' + '247' + ' '
        # 247

        if (drug_interaction[2].text == judge248_1 + drug_name + judge248_2 + drug_name_2 + judge248_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '248' + ' '
        elif (drug_interaction[2].text == judge248_1 + drug_name_2 + judge248_2 + drug_name + judge248_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '248' + ' '
        # 248

        if (drug_interaction[2].text == judge249_1 + drug_name + judge249_2 + drug_name_2 + judge249_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '249' + ' '
        elif (drug_interaction[2].text == judge249_1 + drug_name_2 + judge249_2 + drug_name + judge249_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '249' + ' '
        # 249

        if (drug_interaction[2].text == judge250_1 + drug_name + judge250_2 + drug_name_2 + judge250_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '1' + ' ' + '250' + ' '
        elif (drug_interaction[2].text == judge250_1 + drug_name_2 + judge250_2 + drug_name + judge250_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '1' + ' ' + '250' + ' '
        # 250

        if (drug_interaction[2].text == judge251_1 + drug_name + judge251_2 + drug_name_2 + judge251_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' ' + '1' + ' ' + '251' + ' '
        elif (drug_interaction[2].text == judge251_1 + drug_name_2 + judge251_2 + drug_name + judge251_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' ' + '1' + ' ' + '251' + ' '
        # 251

        if (drug_interaction[2].text == judge252_1 + drug_name + judge252_2 + drug_name_2 + judge252_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '252' + ' '
        elif (drug_interaction[2].text == judge252_1 + drug_name_2 + judge252_2 + drug_name + judge252_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '252' + ' '
        # 252

        if (drug_interaction[2].text == judge253_1 + drug_name + judge253_2 + drug_name_2 + judge253_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '253' + ' '
        elif (drug_interaction[2].text == judge253_1 + drug_name_2 + judge253_2 + drug_name + judge253_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '253' + ' '
        # 253

        if (drug_interaction[2].text == judge254_1 + drug_name + judge254_2 + drug_name_2 + judge254_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '1' + ' ' + '254' + ' '
        elif (drug_interaction[2].text == judge254_1 + drug_name_2 + judge254_2 + drug_name + judge254_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '1' + ' ' + '254' + ' '
        # 254

        if (drug_interaction[2].text == judge255_1 + drug_name + judge255_2 + drug_name_2 + judge255_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '255' + ' '
        elif (drug_interaction[2].text == judge255_1 + drug_name_2 + judge255_2 + drug_name + judge255_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '255' + ' '
        # 255

        if (drug_interaction[2].text == judge256_1 + drug_name + judge256_2 + drug_name_2 + judge256_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '256' + ' '
        elif (drug_interaction[2].text == judge256_1 + drug_name_2 + judge256_2 + drug_name + judge256_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '256' + ' '
        # 256

        if (drug_interaction[2].text == judge257_1 + drug_name + judge257_2 + drug_name_2 + judge257_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' ' + '1' + ' ' + '257' + ' '
        elif (drug_interaction[2].text == judge257_1 + drug_name_2 + judge257_2 + drug_name + judge257_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' ' + '1' + ' ' + '257' + ' '
        # 257

        if (drug_interaction[2].text == judge258_1 + drug_name + judge258_2 + drug_name_2 + judge258_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '258' + ' '
        elif (drug_interaction[2].text == judge258_1 + drug_name_2 + judge258_2 + drug_name + judge258_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '258' + ' '
        # 258

        if (drug_interaction[2].text == judge259_1 + drug_name + judge259_2 + drug_name_2 + judge259_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '259' + ' '
        elif (drug_interaction[2].text == judge259_1 + drug_name_2 + judge259_2 + drug_name + judge259_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '259' + ' '
        # 259

        if (drug_interaction[2].text == judge260_1 + drug_name + judge260_2 + drug_name_2 + judge260_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '260' + ' '
        elif (drug_interaction[2].text == judge260_1 + drug_name_2 + judge260_2 + drug_name + judge260_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '260' + ' '
        # 260

        if (drug_interaction[2].text == judge261_1 + drug_name + judge261_2 + drug_name_2 + judge261_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '261' + ' '
        elif (drug_interaction[2].text == judge261_1 + drug_name_2 + judge261_2 + drug_name + judge261_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '261' + ' '
        # 261

        if (drug_interaction[2].text == judge262_1 + drug_name + judge262_2 + drug_name_2 + judge262_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '262' + ' '
        elif (drug_interaction[2].text == judge262_1 + drug_name_2 + judge262_2 + drug_name + judge262_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '262' + ' '
        # 262

        if (drug_interaction[2].text == judge263_1 + drug_name + judge263_2 + drug_name_2 + judge263_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '263' + ' '
        elif (drug_interaction[2].text == judge263_1 + drug_name_2 + judge263_2 + drug_name + judge263_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '263' + ' '
        # 263

        if (drug_interaction[2].text == judge264_1 + drug_name + judge264_2 + drug_name_2 + judge264_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '264' + ' '
        elif (drug_interaction[2].text == judge264_1 + drug_name_2 + judge264_2 + drug_name + judge264_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '264' + ' '
        # 264

        if (drug_interaction[2].text == drug_name + judge265_1 + drug_name_2 + judge265_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '265' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge265_1 + drug_name + judge265_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '+' + ' ' + '1' + ' ' + '265' + ' '
        # 265

        if (drug_interaction[2].text == judge266_1 + drug_name + judge266_2 + drug_name_2 + judge266_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '1' + ' ' + '266' + ' '
        elif (drug_interaction[2].text == judge266_1 + drug_name_2 + judge266_2 + drug_name + judge266_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '1' + ' ' + '266' + ' '
        # 266

        if (drug_interaction[2].text == judge267_1 + drug_name + judge267_2 + drug_name_2 + judge267_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '267' + ' '
        elif (drug_interaction[2].text == judge267_1 + drug_name_2 + judge267_2 + drug_name + judge267_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '267' + ' '
        # 267

        if (drug_interaction[2].text == judge268_1 + drug_name + judge268_2 + drug_name_2 + judge268_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '1' + ' ' + '268' + ' '
        elif (drug_interaction[2].text == judge268_1 + drug_name_2 + judge268_2 + drug_name + judge268_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '+' + ' ' + '1' + ' ' + '268' + ' '
        # 268

        if (drug_interaction[2].text == judge269_1 + drug_name + judge269_2 + drug_name_2 + judge269_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '269' + ' '
        elif (drug_interaction[2].text == judge269_1 + drug_name_2 + judge269_2 + drug_name + judge269_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '269' + ' '
        # 269

        if (drug_interaction[2].text == judge270_1 + drug_name + judge270_2 + drug_name_2 + judge270_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '1' + ' ' + '270' + ' '
        elif (drug_interaction[2].text == judge270_1 + drug_name_2 + judge270_2 + drug_name + judge270_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '1' + ' ' + '270' + ' '
        # 270

        if (drug_interaction[2].text == judge271_1 + drug_name + judge271_2 + drug_name_2 + judge271_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '271' + ' '
        elif (drug_interaction[2].text == judge271_1 + drug_name_2 + judge271_2 + drug_name + judge271_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '271' + ' '
        # 271

        if (drug_interaction[2].text == judge272_1 + drug_name + judge272_2 + drug_name_2 + judge272_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '272' + ' '
        elif (drug_interaction[2].text == judge272_1 + drug_name_2 + judge272_2 + drug_name + judge272_3):
            result_str += drug_pri_id + ' ' + \
                          'a' + ' ' + '+' + ' ' + '0' + ' ' + '272' + ' '
        # 272

        if (drug_interaction[2].text == judge273_1 + drug_name + judge273_2 + drug_name_2 + judge273_3):
            result_str += drug_interaction[0].text + ' ' + \
                          'pk' + ' ' + '-' + ' ' + '1' + ' ' + '273' + ' '
        elif (drug_interaction[2].text == judge273_1 + drug_name_2 + judge273_2 + drug_name + judge273_3):
            result_str += drug_pri_id + ' ' + \
                          'pk' + ' ' + '-' + ' ' + '1' + ' ' + '273' + ' '
        # 273

        if (drug_interaction[2].text == drug_name + judge274_1 + drug_name_2 + judge274_2):
            result_str += drug_interaction[0].text + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '274' + ' '
        elif (drug_interaction[2].text == drug_name_2 + judge274_1 + drug_name + judge274_2):
            result_str += drug_pri_id + ' ' + \
                          'pd_a' + ' ' + '-' + ' ' + '1' + ' ' + '274' + ' '
        # 274

        exp1_1 = drug_name + judge1_1 + drug_name_2 + judge1_2
        exp1_2 = drug_name_2 + judge1_1 + drug_name + judge1_2

        exp2_1 = drug_name + judge2_1 + drug_name_2 + judge2_2
        exp2_2 = drug_name_2 + judge2_1 + drug_name + judge2_2

        exp3_1 = judge3_1 + drug_name_2 + judge3_2 + drug_name + judge3_3
        exp3_2 = judge3_1 + drug_name + judge3_2 + drug_name_2 + judge3_3

        exp4_1 = judge4_1 + drug_name_2 + judge4_2 + drug_name + judge4_3
        exp4_2 = judge4_1 + drug_name + judge4_2 + drug_name_2 + judge4_3

        exp5_1 = judge5_1 + drug_name_2 + judge5_2 + drug_name + judge5_3
        exp5_2 = judge5_1 + drug_name + judge5_2 + drug_name_2 + judge5_3

        exp6_1 = judge6_1 + drug_name_2 + judge6_2 + drug_name + judge6_3
        exp6_2 = judge6_1 + drug_name + judge6_2 + drug_name_2 + judge6_3

        exp7_1 = judge7_1 + drug_name_2 + judge7_2 + drug_name + judge7_3
        exp7_2 = judge7_1 + drug_name + judge7_2 + drug_name_2 + judge7_3

        exp8_1 = judge8_1 + drug_name_2 + judge8_2 + drug_name + judge8_3
        exp8_2 = judge8_1 + drug_name + judge8_2 + drug_name_2 + judge8_3

        exp9_1 = judge9_1 + drug_name_2 + judge9_2 + drug_name + judge9_3
        exp9_2 = judge9_1 + drug_name + judge9_2 + drug_name_2 + judge9_3

        exp10_1 = judge10_1 + drug_name_2 + judge10_2 + drug_name + judge10_3
        exp10_2 = judge10_1 + drug_name + judge10_2 + drug_name_2 + judge10_3

        exp11_1 = judge11_1 + drug_name_2 + judge11_2 + drug_name_2 + judge11_3 + drug_name + judge11_4
        exp11_2 = judge11_1 + drug_name + judge11_2 + drug_name + judge11_3 + drug_name_2 + judge11_4

        exp12_1 = judge12_1 + drug_name_2 + judge12_2 + drug_name_2 + judge12_3 + drug_name + judge12_4
        exp12_2 = judge12_1 + drug_name + judge12_2 + drug_name + judge12_3 + drug_name_2 + judge12_4

        exp13_1 = judge13_1 + drug_name_2 + judge13_2 + drug_name + judge13_3
        exp13_2 = judge13_1 + drug_name + judge13_2 + drug_name_2 + judge13_3

        exp14_1 = judge14_1 + drug_name_2 + judge14_2 + drug_name + judge14_3
        exp14_2 = judge14_1 + drug_name + judge14_2 + drug_name_2 + judge14_3

        exp15_1 = drug_name + judge15_1 + drug_name_2 + judge15_2
        exp15_2 = drug_name_2 + judge15_1 + drug_name + judge15_2

        exp16_1 = drug_name + judge16_1 + drug_name_2 + judge16_2
        exp16_2 = drug_name_2 + judge16_1 + drug_name + judge16_2

        exp17_1 = drug_name + judge17_1 + drug_name_2 + judge17_2
        exp17_2 = drug_name_2 + judge17_1 + drug_name + judge17_2

        exp18_1 = drug_name + judge18_1 + drug_name_2 + judge18_2
        exp18_2 = drug_name_2 + judge18_1 + drug_name + judge18_2

        exp19_1 = drug_name + judge19_1 + drug_name_2 + judge19_2
        exp19_2 = drug_name_2 + judge19_1 + drug_name + judge19_2

        exp20_1 = drug_name + judge20_1 + drug_name_2 + judge20_2
        exp20_2 = drug_name_2 + judge20_1 + drug_name + judge20_2

        exp21_1 = drug_name + judge21_1 + drug_name_2 + judge21_2
        exp21_2 = drug_name_2 + judge21_1 + drug_name + judge21_2

        exp22_1 = drug_name + judge22_1 + drug_name_2 + judge22_2
        exp22_2 = drug_name_2 + judge22_1 + drug_name + judge22_2

        exp23_1 = drug_name + judge23_1 + drug_name_2 + judge23_2
        exp23_2 = drug_name_2 + judge23_1 + drug_name + judge23_2

        exp24_1 = drug_name + judge24_1 + drug_name_2 + judge24_2
        exp24_2 = drug_name_2 + judge24_1 + drug_name + judge24_2

        exp25_1 = judge25_1 + drug_name_2 + judge25_2 + drug_name + judge25_3
        exp25_2 = judge25_1 + drug_name + judge25_2 + drug_name_2 + judge25_3

        exp26_1 = judge26_1 + drug_name + judge26_2 + drug_name_2 + judge26_3
        exp26_2 = judge26_1 + drug_name_2 + judge26_2 + drug_name + judge26_3

        exp27_1 = judge27_1 + drug_name + judge27_2 + drug_name_2 + judge27_3
        exp27_2 = judge27_1 + drug_name_2 + judge27_2 + drug_name + judge27_3

        exp28_1 = judge28_1 + drug_name_2 + judge28_2 + drug_name + judge28_3
        exp28_2 = judge28_1 + drug_name + judge28_2 + drug_name_2 + judge28_3

        exp29_1 = judge29_1 + drug_name + judge29_2 + drug_name_2 + judge29_3
        exp29_2 = judge29_1 + drug_name_2 + judge29_2 + drug_name + judge29_3

        exp30_1 = judge30_1 + drug_name_2 + judge30_2 + drug_name + judge30_3
        exp30_2 = judge30_1 + drug_name + judge30_2 + drug_name_2 + judge30_3

        exp31_1 = judge31_1 + drug_name + judge31_2 + drug_name_2 + judge31_3
        exp31_2 = judge31_1 + drug_name_2 + judge31_2 + drug_name + judge31_3

        exp32_1 = judge32_1 + drug_name + judge32_2 + drug_name_2 + judge32_3
        exp32_2 = judge32_1 + drug_name_2 + judge32_2 + drug_name + judge32_3

        exp33_1 = drug_name + judge33_1 + drug_name_2 + judge33_2
        exp33_2 = drug_name_2 + judge33_1 + drug_name + judge33_2

        exp34_1 = drug_name + judge34_1 + drug_name_2 + judge34_2
        exp34_2 = drug_name_2 + judge34_1 + drug_name + judge34_2

        exp35_1 = drug_name + judge35_1 + drug_name_2 + judge35_2
        exp35_2 = drug_name_2 + judge35_1 + drug_name + judge35_2

        exp36_1 = drug_name + judge36_1 + drug_name_2 + judge36_2
        exp36_2 = drug_name_2 + judge36_1 + drug_name + judge36_2

        exp37_1 = drug_name + judge37_1 + drug_name_2 + judge37_2
        exp37_2 = drug_name_2 + judge37_1 + drug_name + judge37_2

        exp38_1 = drug_name + judge38_1 + drug_name_2 + judge38_2
        exp38_2 = drug_name_2 + judge38_1 + drug_name + judge38_2

        exp39_1 = drug_name + judge39_1 + drug_name_2 + judge39_2
        exp39_2 = drug_name_2 + judge39_1 + drug_name + judge39_2

        exp40_1 = drug_name + judge40_1 + drug_name_2 + judge40_2
        exp40_2 = drug_name_2 + judge40_1 + drug_name + judge40_2

        exp41_1 = drug_name + judge41_1 + drug_name_2 + judge41_2
        exp41_2 = drug_name_2 + judge41_1 + drug_name + judge41_2

        exp42_1 = drug_name + judge42_1 + drug_name_2 + judge42_2
        exp42_2 = drug_name_2 + judge42_1 + drug_name + judge42_2

        exp43_1 = drug_name + judge43_1 + drug_name_2 + judge43_2
        exp43_2 = drug_name_2 + judge43_1 + drug_name + judge43_2

        exp44_1 = drug_name + judge44_1 + drug_name_2 + judge44_2
        exp44_2 = drug_name_2 + judge44_1 + drug_name + judge44_2

        exp45_1 = drug_name + judge45_1 + drug_name_2 + judge45_2
        exp45_2 = drug_name_2 + judge45_1 + drug_name + judge45_2

        exp46_1 = drug_name + judge46_1 + drug_name_2 + judge46_2
        exp46_2 = drug_name_2 + judge46_1 + drug_name + judge46_2

        exp47_1 = drug_name + judge47_1 + drug_name_2 + judge47_2
        exp47_2 = drug_name_2 + judge47_1 + drug_name + judge47_2

        exp48_1 = drug_name + judge48_1 + drug_name_2 + judge48_2
        exp48_2 = drug_name_2 + judge48_1 + drug_name + judge48_2

        exp49_1 = drug_name + judge49_1 + drug_name_2 + judge49_2
        exp49_2 = drug_name_2 + judge49_1 + drug_name + judge49_2

        exp50_1 = drug_name + judge50_1 + drug_name_2 + judge50_2
        exp50_2 = drug_name_2 + judge50_1 + drug_name + judge50_2

        exp51_1 = drug_name + judge51_1 + drug_name_2 + judge51_2
        exp51_2 = drug_name_2 + judge51_1 + drug_name + judge51_2

        exp52_1 = drug_name + judge52_1 + drug_name_2 + judge52_2
        exp52_2 = drug_name_2 + judge52_1 + drug_name + judge52_2

        exp53_1 = drug_name + judge53_1 + drug_name_2 + judge53_2
        exp53_2 = drug_name_2 + judge53_1 + drug_name + judge53_2

        exp54_1 = drug_name + judge54_1 + drug_name_2 + judge54_2
        exp54_2 = drug_name_2 + judge54_1 + drug_name + judge54_2

        exp55_1 = drug_name + judge55_1 + drug_name_2 + judge55_2
        exp55_2 = drug_name_2 + judge55_1 + drug_name + judge55_2

        exp56_1 = drug_name + judge56_1 + drug_name_2 + judge56_2
        exp56_2 = drug_name_2 + judge56_1 + drug_name + judge56_2

        exp57_1 = drug_name + judge57_1 + drug_name_2 + judge57_2
        exp57_2 = drug_name_2 + judge57_1 + drug_name + judge57_2

        exp58_1 = drug_name + judge58_1 + drug_name_2 + judge58_2
        exp58_2 = drug_name_2 + judge58_1 + drug_name + judge58_2

        exp59_1 = drug_name + judge59_1 + drug_name_2 + judge59_2
        exp59_2 = drug_name_2 + judge59_1 + drug_name + judge59_2

        exp60_1 = drug_name + judge60_1 + drug_name_2 + judge60_2
        exp60_2 = drug_name_2 + judge60_1 + drug_name + judge60_2

        exp61_1 = drug_name + judge61_1 + drug_name_2 + judge61_2
        exp61_2 = drug_name_2 + judge61_1 + drug_name + judge61_2

        exp62_1 = drug_name + judge62_1 + drug_name_2 + judge62_2
        exp62_2 = drug_name_2 + judge62_1 + drug_name + judge62_2

        exp63_1 = drug_name + judge63_1 + drug_name_2 + judge63_2
        exp63_2 = drug_name_2 + judge63_1 + drug_name + judge63_2

        exp64_1 = drug_name + judge64_1 + drug_name_2 + judge64_2
        exp64_2 = drug_name_2 + judge64_1 + drug_name + judge64_2

        exp65_1 = drug_name + judge65_1 + drug_name_2 + judge65_2
        exp65_2 = drug_name_2 + judge65_1 + drug_name + judge65_2

        exp66_1 = drug_name + judge66_1 + drug_name_2 + judge66_2
        exp66_2 = drug_name_2 + judge66_1 + drug_name + judge66_2

        exp67_1 = drug_name + judge67_1 + drug_name_2 + judge67_2
        exp67_2 = drug_name_2 + judge67_1 + drug_name + judge67_2

        exp68_1 = drug_name + judge68_1 + drug_name_2 + judge68_2
        exp68_2 = drug_name_2 + judge68_1 + drug_name + judge68_2

        exp69_1 = drug_name + judge69_1 + drug_name_2 + judge69_2
        exp69_2 = drug_name_2 + judge69_1 + drug_name + judge69_2

        exp70_1 = drug_name + judge70_1 + drug_name_2 + judge70_2
        exp70_2 = drug_name_2 + judge70_1 + drug_name + judge70_2

        exp71_1 = drug_name + judge71_1 + drug_name_2 + judge71_2
        exp71_2 = drug_name_2 + judge71_1 + drug_name + judge71_2

        exp72_1 = drug_name + judge72_1 + drug_name_2 + judge72_2
        exp72_2 = drug_name_2 + judge72_1 + drug_name + judge72_2

        exp73_1 = drug_name + judge73_1 + drug_name_2 + judge73_2
        exp73_2 = drug_name_2 + judge73_1 + drug_name + judge73_2

        exp74_1 = drug_name + judge74_1 + drug_name_2 + judge74_2
        exp74_2 = drug_name_2 + judge74_1 + drug_name + judge74_2

        exp75_1 = drug_name + judge75_1 + drug_name_2 + judge75_2
        exp75_2 = drug_name_2 + judge75_1 + drug_name + judge75_2

        exp76_1 = drug_name + judge76_1 + drug_name_2 + judge76_2
        exp76_2 = drug_name_2 + judge76_1 + drug_name + judge76_2

        exp77_1 = drug_name + judge77_1 + drug_name_2 + judge77_2
        exp77_2 = drug_name_2 + judge77_1 + drug_name + judge77_2

        exp78_1 = drug_name + judge78_1 + drug_name_2 + judge78_2
        exp78_2 = drug_name_2 + judge78_1 + drug_name + judge78_2

        exp79_1 = drug_name + judge79_1 + drug_name_2 + judge79_2
        exp79_2 = drug_name_2 + judge79_1 + drug_name + judge79_2

        exp80_1 = drug_name + judge80_1 + drug_name_2 + judge80_2
        exp80_2 = drug_name_2 + judge80_1 + drug_name + judge80_2

        exp81_1 = drug_name + judge81_1 + drug_name_2 + judge81_2
        exp81_2 = drug_name_2 + judge81_1 + drug_name + judge81_2

        exp82_1 = drug_name + judge82_1 + drug_name_2 + judge82_2
        exp82_2 = drug_name_2 + judge82_1 + drug_name + judge82_2

        exp83_1 = drug_name + judge83_1 + drug_name_2 + judge83_2
        exp83_2 = drug_name_2 + judge83_1 + drug_name + judge83_2

        exp84_1 = drug_name + judge84_1 + drug_name_2 + judge84_2
        exp84_2 = drug_name_2 + judge84_1 + drug_name + judge84_2

        exp85_1 = drug_name + judge85_1 + drug_name_2 + judge85_2
        exp85_2 = drug_name_2 + judge85_1 + drug_name + judge85_2

        exp86_1 = drug_name + judge86_1 + drug_name_2 + judge86_2
        exp86_2 = drug_name_2 + judge86_1 + drug_name + judge86_2

        exp87_1 = judge87_1 + drug_name + judge87_2 + drug_name_2 + judge87_3
        exp87_2 = judge87_1 + drug_name_2 + judge87_2 + drug_name + judge87_3

        exp88_1 = judge88_1 + drug_name + judge88_2 + drug_name_2 + judge88_3
        exp88_2 = judge88_1 + drug_name_2 + judge88_2 + drug_name + judge88_3

        exp89_1 = judge89_1 + drug_name + judge89_2 + drug_name_2 + judge89_3
        exp89_2 = judge89_1 + drug_name_2 + judge89_2 + drug_name + judge89_3

        exp90_1 = judge90_1 + drug_name + judge90_2 + drug_name_2 + judge90_3
        exp90_2 = judge90_1 + drug_name_2 + judge90_2 + drug_name + judge90_3

        exp91_1 = judge91_1 + drug_name + judge91_2 + drug_name_2 + judge91_3
        exp91_2 = judge91_1 + drug_name_2 + judge91_2 + drug_name + judge91_3

        exp92_1 = judge92_1 + drug_name + judge92_2 + drug_name_2 + judge92_3
        exp92_2 = judge92_1 + drug_name_2 + judge92_2 + drug_name + judge92_3

        exp93_1 = judge93_1 + drug_name + judge93_2 + drug_name_2 + judge93_3
        exp93_2 = judge93_1 + drug_name_2 + judge93_2 + drug_name + judge93_3

        exp94_1 = judge94_1 + drug_name + judge94_2 + drug_name_2 + judge94_3
        exp94_2 = judge94_1 + drug_name_2 + judge94_2 + drug_name + judge94_3

        exp95_1 = judge95_1 + drug_name + judge95_2 + drug_name_2 + judge95_3
        exp95_2 = judge95_1 + drug_name_2 + judge95_2 + drug_name + judge95_3

        exp96_1 = judge96_1 + drug_name + judge96_2 + drug_name_2 + judge96_3
        exp96_2 = judge96_1 + drug_name_2 + judge96_2 + drug_name + judge96_3

        exp97_1 = judge97_1 + drug_name + judge97_2 + drug_name_2 + judge97_3
        exp97_2 = judge97_1 + drug_name_2 + judge97_2 + drug_name + judge97_3

        exp98_1 = judge98_1 + drug_name + judge98_2 + drug_name_2 + judge98_3
        exp98_2 = judge98_1 + drug_name_2 + judge98_2 + drug_name + judge98_3

        exp99_1 = judge99_1 + drug_name + judge99_2 + drug_name_2 + judge99_3
        exp99_2 = judge99_1 + drug_name_2 + judge99_2 + drug_name + judge99_3

        exp100_1 = judge100_1 + drug_name + judge100_2 + drug_name_2 + judge100_3
        exp100_2 = judge100_1 + drug_name_2 + judge100_2 + drug_name + judge100_3

        exp101_1 = judge101_1 + drug_name + judge101_2 + drug_name_2 + judge101_3
        exp101_2 = judge101_1 + drug_name_2 + judge101_2 + drug_name + judge101_3

        exp102_1 = judge102_1 + drug_name + judge102_2 + drug_name_2 + judge102_3
        exp102_2 = judge102_1 + drug_name_2 + judge102_2 + drug_name + judge102_3

        exp103_1 = judge103_1 + drug_name + judge103_2 + drug_name_2 + judge103_3
        exp103_2 = judge103_1 + drug_name_2 + judge103_2 + drug_name + judge103_3

        exp104_1 = judge104_1 + drug_name + judge104_2 + drug_name_2 + judge104_3
        exp104_2 = judge104_1 + drug_name_2 + judge104_2 + drug_name + judge104_3

        exp105_1 = judge105_1 + drug_name + judge105_2 + drug_name_2 + judge105_3
        exp105_2 = judge105_1 + drug_name_2 + judge105_2 + drug_name + judge105_3

        exp106_1 = judge106_1 + drug_name + judge106_2 + drug_name_2 + judge106_3
        exp106_2 = judge106_1 + drug_name_2 + judge106_2 + drug_name + judge106_3

        exp107_1 = judge107_1 + drug_name + judge107_2 + drug_name_2 + judge107_3
        exp107_2 = judge107_1 + drug_name_2 + judge107_2 + drug_name + judge107_3

        exp108_1 = judge108_1 + drug_name + judge108_2 + drug_name_2 + judge108_3
        exp108_2 = judge108_1 + drug_name_2 + judge108_2 + drug_name + judge108_3

        exp109_1 = judge109_1 + drug_name + judge109_2 + drug_name_2 + judge109_3
        exp109_2 = judge109_1 + drug_name_2 + judge109_2 + drug_name + judge109_3

        exp110_1 = judge110_1 + drug_name + judge110_2 + drug_name_2 + judge110_3
        exp110_2 = judge110_1 + drug_name_2 + judge110_2 + drug_name + judge110_3

        exp111_1 = judge111_1 + drug_name + judge111_2 + drug_name_2 + judge111_3
        exp111_2 = judge111_1 + drug_name_2 + judge111_2 + drug_name + judge111_3

        exp112_1 = judge112_1 + drug_name + judge112_2 + drug_name_2 + judge112_3
        exp112_2 = judge112_1 + drug_name_2 + judge112_2 + drug_name + judge112_3

        exp113_1 = drug_name + judge113_1 + drug_name_2 + judge113_2
        exp113_2 = drug_name_2 + judge113_1 + drug_name + judge113_2

        exp114_1 = judge114_1 + drug_name + judge114_2 + drug_name_2 + judge114_3
        exp114_2 = judge114_1 + drug_name_2 + judge114_2 + drug_name + judge114_3

        exp115_1 = judge115_1 + drug_name + judge115_2 + drug_name_2 + judge115_3
        exp115_2 = judge115_1 + drug_name_2 + judge115_2 + drug_name + judge115_3

        exp116_1 = judge116_1 + drug_name + judge116_2 + drug_name_2 + judge116_3
        exp116_2 = judge116_1 + drug_name_2 + judge116_2 + drug_name + judge116_3

        exp117_1 = judge117_1 + drug_name + judge117_2 + drug_name_2 + judge117_3
        exp117_2 = judge117_1 + drug_name_2 + judge117_2 + drug_name + judge117_3

        exp118_1 = judge118_1 + drug_name + judge118_2 + drug_name_2 + judge118_3
        exp118_2 = judge118_1 + drug_name_2 + judge118_2 + drug_name + judge118_3

        exp119_1 = judge119_1 + drug_name + judge119_2 + drug_name_2 + judge119_3
        exp119_2 = judge119_1 + drug_name_2 + judge119_2 + drug_name + judge119_3

        exp120_1 = judge120_1 + drug_name + judge120_2 + drug_name_2 + judge120_3
        exp120_2 = judge120_1 + drug_name_2 + judge120_2 + drug_name + judge120_3

        exp121_1 = judge121_1 + drug_name + judge121_2 + drug_name_2 + judge121_3
        exp121_2 = judge121_1 + drug_name_2 + judge121_2 + drug_name + judge121_3

        exp122_1 = judge122_1 + drug_name + judge122_2 + drug_name_2 + judge122_3
        exp122_2 = judge122_1 + drug_name_2 + judge122_2 + drug_name + judge122_3

        exp123_1 = judge123_1 + drug_name + judge123_2 + drug_name_2 + judge123_3
        exp123_2 = judge123_1 + drug_name_2 + judge123_2 + drug_name + judge123_3

        exp124_1 = judge124_1 + drug_name + judge124_2 + drug_name_2 + judge124_3
        exp124_2 = judge124_1 + drug_name_2 + judge124_2 + drug_name + judge124_3

        exp125_1 = judge125_1 + drug_name + judge125_2 + drug_name_2 + judge125_3
        exp125_2 = judge125_1 + drug_name_2 + judge125_2 + drug_name + judge125_3

        exp126_1 = judge126_1 + drug_name + judge126_2 + drug_name_2 + judge126_3
        exp126_2 = judge126_1 + drug_name_2 + judge126_2 + drug_name + judge126_3

        exp127_1 = drug_name + judge127_1 + drug_name_2 + judge127_2
        exp127_2 = drug_name_2 + judge127_1 + drug_name + judge127_2

        exp128_1 = judge128_1 + drug_name + judge128_2 + drug_name_2 + judge128_3
        exp128_2 = judge128_1 + drug_name_2 + judge128_2 + drug_name + judge128_3

        exp129_1 = judge129_1 + drug_name + judge129_2 + drug_name_2 + judge129_3
        exp129_2 = judge129_1 + drug_name_2 + judge129_2 + drug_name + judge129_3

        exp130_1 = judge130_1 + drug_name + judge130_2 + drug_name_2 + judge130_3
        exp130_2 = judge130_1 + drug_name_2 + judge130_2 + drug_name + judge130_3

        exp131_1 = judge131_1 + drug_name + judge131_2 + drug_name_2 + judge131_3
        exp131_2 = judge131_1 + drug_name_2 + judge131_2 + drug_name + judge131_3

        exp132_1 = judge132_1 + drug_name + judge132_2 + drug_name_2 + judge132_3
        exp132_2 = judge132_1 + drug_name_2 + judge132_2 + drug_name + judge132_3

        exp133_1 = drug_name + judge133_1 + drug_name_2 + judge133_2
        exp133_2 = drug_name_2 + judge133_1 + drug_name + judge133_2

        exp134_1 = judge134_1 + drug_name + judge134_2 + drug_name_2 + judge134_3
        exp134_2 = judge134_1 + drug_name_2 + judge134_2 + drug_name + judge134_3

        exp135_1 = judge135_1 + drug_name + judge135_2 + drug_name_2 + judge135_3
        exp135_2 = judge135_1 + drug_name_2 + judge135_2 + drug_name + judge135_3

        exp136_1 = judge136_1 + drug_name + judge136_2 + drug_name_2 + judge136_3
        exp136_2 = judge136_1 + drug_name_2 + judge136_2 + drug_name + judge136_3

        exp137_1 = judge137_1 + drug_name + judge137_2 + drug_name_2 + judge137_3
        exp137_2 = judge137_1 + drug_name_2 + judge137_2 + drug_name + judge137_3

        exp138_1 = judge138_1 + drug_name + judge138_2 + drug_name_2 + judge138_3
        exp138_2 = judge138_1 + drug_name_2 + judge138_2 + drug_name + judge138_3

        exp139_1 = judge139_1 + drug_name + judge139_2 + drug_name_2 + judge139_3
        exp139_2 = judge139_1 + drug_name_2 + judge139_2 + drug_name + judge139_3

        exp140_1 = drug_name + judge140_1 + drug_name_2 + judge140_2
        exp140_2 = drug_name_2 + judge140_1 + drug_name + judge140_2

        exp141_1 = judge141_1 + drug_name + judge141_2 + drug_name_2 + judge141_3
        exp141_2 = judge141_1 + drug_name_2 + judge141_2 + drug_name + judge141_3

        exp142_1 = judge142_1 + drug_name + judge142_2 + drug_name_2 + judge142_3
        exp142_2 = judge142_1 + drug_name_2 + judge142_2 + drug_name + judge142_3

        exp143_1 = judge143_1 + drug_name + judge143_2 + drug_name_2 + judge143_3
        exp143_2 = judge143_1 + drug_name_2 + judge143_2 + drug_name + judge143_3

        exp144_1 = judge144_1 + drug_name + judge144_2 + drug_name_2 + judge144_3
        exp144_2 = judge144_1 + drug_name_2 + judge144_2 + drug_name + judge144_3

        exp145_1 = judge145_1 + drug_name + judge145_2 + drug_name_2 + judge145_3
        exp145_2 = judge145_1 + drug_name_2 + judge145_2 + drug_name + judge145_3

        exp146_1 = judge146_1 + drug_name + judge146_2 + drug_name_2 + judge146_3
        exp146_2 = judge146_1 + drug_name_2 + judge146_2 + drug_name + judge146_3

        exp147_1 = judge147_1 + drug_name + judge147_2 + drug_name_2 + judge147_3
        exp147_2 = judge147_1 + drug_name_2 + judge147_2 + drug_name + judge147_3

        exp148_1 = judge148_1 + drug_name + judge148_2 + drug_name_2 + judge148_3
        exp148_2 = judge148_1 + drug_name_2 + judge148_2 + drug_name + judge148_3

        exp149_1 = judge149_1 + drug_name + judge149_2 + drug_name_2 + judge149_3
        exp149_2 = judge149_1 + drug_name_2 + judge149_2 + drug_name + judge149_3

        exp150_1 = judge150_1 + drug_name + judge150_2 + drug_name_2 + judge150_3
        exp150_2 = judge150_1 + drug_name_2 + judge150_2 + drug_name + judge150_3

        exp151_1 = judge151_1 + drug_name + judge151_2 + drug_name_2 + judge151_3
        exp151_2 = judge151_1 + drug_name_2 + judge151_2 + drug_name + judge151_3

        exp152_1 = judge152_1 + drug_name + judge152_2 + drug_name_2 + judge152_3
        exp152_2 = judge152_1 + drug_name_2 + judge152_2 + drug_name + judge152_3

        exp153_1 = judge153_1 + drug_name + judge153_2 + drug_name_2 + judge153_3
        exp153_2 = judge153_1 + drug_name_2 + judge153_2 + drug_name + judge153_3

        exp154_1 = judge154_1 + drug_name + judge154_2 + drug_name_2 + judge154_3
        exp154_2 = judge154_1 + drug_name_2 + judge154_2 + drug_name + judge154_3

        exp155_1 = judge155_1 + drug_name + judge155_2 + drug_name_2 + judge155_3
        exp155_2 = judge155_1 + drug_name_2 + judge155_2 + drug_name + judge155_3

        exp156_1 = judge156_1 + drug_name + judge156_2 + drug_name_2 + judge156_3
        exp156_2 = judge156_1 + drug_name_2 + judge156_2 + drug_name + judge156_3

        exp157_1 = judge157_1 + drug_name + judge157_2 + drug_name_2 + judge157_3
        exp157_2 = judge157_1 + drug_name_2 + judge157_2 + drug_name + judge157_3

        exp158_1 = drug_name + judge158_1 + drug_name_2 + judge158_2
        exp158_2 = drug_name_2 + judge158_1 + drug_name + judge158_2

        exp159_1 = judge159_1 + drug_name + judge159_2 + drug_name_2 + judge159_3
        exp159_2 = judge159_1 + drug_name_2 + judge159_2 + drug_name + judge159_3

        exp160_1 = drug_name + judge160_1 + drug_name_2 + judge160_2
        exp160_2 = drug_name_2 + judge160_1 + drug_name + judge160_2

        exp161_1 = drug_name + judge161_1 + drug_name_2 + judge161_2
        exp161_2 = drug_name_2 + judge161_1 + drug_name + judge161_2

        exp162_1 = judge162_1 + drug_name + judge162_2 + drug_name_2 + judge162_3
        exp162_2 = judge162_1 + drug_name_2 + judge162_2 + drug_name + judge162_3

        exp163_1 = judge163_1 + drug_name + judge163_2 + drug_name_2 + judge163_3
        exp163_2 = judge163_1 + drug_name_2 + judge163_2 + drug_name + judge163_3

        exp164_1 = judge164_1 + drug_name + judge164_2 + drug_name_2 + judge164_3
        exp164_2 = judge164_1 + drug_name_2 + judge164_2 + drug_name + judge164_3

        exp165_1 = judge165_1 + drug_name + judge165_2 + drug_name_2 + judge165_3
        exp165_2 = judge165_1 + drug_name_2 + judge165_2 + drug_name + judge165_3

        exp166_1 = judge166_1 + drug_name + judge166_2 + drug_name_2 + judge166_3
        exp166_2 = judge166_1 + drug_name_2 + judge166_2 + drug_name + judge166_3

        exp167_1 = judge167_1 + drug_name + judge167_2 + drug_name_2 + judge167_3
        exp167_2 = judge167_1 + drug_name_2 + judge167_2 + drug_name + judge167_3

        exp168_1 = judge168_1 + drug_name + judge168_2 + drug_name_2 + judge168_3
        exp168_2 = judge168_1 + drug_name_2 + judge168_2 + drug_name + judge168_3

        exp169_1 = judge169_1 + drug_name + judge169_2 + drug_name_2 + judge169_3
        exp169_2 = judge169_1 + drug_name_2 + judge169_2 + drug_name + judge169_3

        exp170_1 = judge170_1 + drug_name + judge170_2 + drug_name_2 + judge170_3
        exp170_2 = judge170_1 + drug_name_2 + judge170_2 + drug_name + judge170_3

        exp171_1 = judge171_1 + drug_name + judge171_2 + drug_name_2 + judge171_3
        exp171_2 = judge171_1 + drug_name_2 + judge171_2 + drug_name + judge171_3

        exp172_1 = judge172_1 + drug_name + judge172_2 + drug_name_2 + judge172_3
        exp172_2 = judge172_1 + drug_name_2 + judge172_2 + drug_name + judge172_3

        exp173_1 = judge173_1 + drug_name + judge173_2 + drug_name_2 + judge173_3
        exp173_2 = judge173_1 + drug_name_2 + judge173_2 + drug_name + judge173_3

        exp174_1 = judge174_1 + drug_name + judge174_2 + drug_name_2 + judge174_3
        exp174_2 = judge174_1 + drug_name_2 + judge174_2 + drug_name + judge174_3

        exp175_1 = judge175_1 + drug_name + judge175_2 + drug_name_2 + judge175_3
        exp175_2 = judge175_1 + drug_name_2 + judge175_2 + drug_name + judge175_3

        exp176_1 = judge176_1 + drug_name + judge176_2 + drug_name_2 + judge176_3
        exp176_2 = judge176_1 + drug_name_2 + judge176_2 + drug_name + judge176_3

        exp177_1 = drug_name + judge177_1 + drug_name_2 + judge177_2
        exp177_2 = drug_name_2 + judge177_1 + drug_name + judge177_2

        exp178_1 = judge178_1 + drug_name + judge178_2 + drug_name_2 + judge178_3
        exp178_2 = judge178_1 + drug_name_2 + judge178_2 + drug_name + judge178_3

        exp179_1 = drug_name + judge179_1 + drug_name_2 + judge179_2
        exp179_2 = drug_name_2 + judge179_1 + drug_name + judge179_2

        exp180_1 = judge180_1 + drug_name + judge180_2 + drug_name_2 + judge180_3
        exp180_2 = judge180_1 + drug_name_2 + judge180_2 + drug_name + judge180_3

        exp181_1 = judge181_1 + drug_name + judge181_2 + drug_name_2 + judge181_3
        exp181_2 = judge181_1 + drug_name_2 + judge181_2 + drug_name + judge181_3

        exp182_1 = judge182_1 + drug_name + judge182_2 + drug_name_2 + judge182_3
        exp182_2 = judge182_1 + drug_name_2 + judge182_2 + drug_name + judge182_3

        exp183_1 = judge183_1 + drug_name + judge183_2 + drug_name_2 + judge183_3
        exp183_2 = judge183_1 + drug_name_2 + judge183_2 + drug_name + judge183_3

        exp184_1 = judge184_1 + drug_name + judge184_2 + drug_name_2 + judge184_3
        exp184_2 = judge184_1 + drug_name_2 + judge184_2 + drug_name + judge184_3

        exp185_1 = drug_name + judge185_1 + drug_name_2 + judge185_2
        exp185_2 = drug_name_2 + judge185_1 + drug_name + judge185_2

        exp186_1 = judge186_1 + drug_name + judge186_2 + drug_name_2 + judge186_3
        exp186_2 = judge186_1 + drug_name_2 + judge186_2 + drug_name + judge186_3

        exp187_1 = judge187_1 + drug_name + judge187_2 + drug_name_2 + judge187_3
        exp187_2 = judge187_1 + drug_name_2 + judge187_2 + drug_name + judge187_3

        exp188_1 = judge188_1 + drug_name + judge188_2 + drug_name_2 + judge188_3
        exp188_2 = judge188_1 + drug_name_2 + judge188_2 + drug_name + judge188_3

        exp189_1 = judge189_1 + drug_name + judge189_2 + drug_name_2 + judge189_3
        exp189_2 = judge189_1 + drug_name_2 + judge189_2 + drug_name + judge189_3

        exp190_1 = judge190_1 + drug_name + judge190_2 + drug_name_2 + judge190_3
        exp190_2 = judge190_1 + drug_name_2 + judge190_2 + drug_name + judge190_3

        exp191_1 = drug_name + judge191_1 + drug_name_2 + judge191_2
        exp191_2 = drug_name_2 + judge191_1 + drug_name + judge191_2

        exp192_1 = drug_name + judge192_1 + drug_name_2 + judge192_2
        exp192_2 = drug_name_2 + judge192_1 + drug_name + judge192_2

        exp193_1 = judge193_1 + drug_name + judge193_2 + drug_name_2 + judge193_3
        exp193_2 = judge193_1 + drug_name_2 + judge193_2 + drug_name + judge193_3

        exp194_1 = judge194_1 + drug_name + judge194_2 + drug_name_2 + judge194_3
        exp194_2 = judge194_1 + drug_name_2 + judge194_2 + drug_name + judge194_3

        exp195_1 = judge195_1 + drug_name + judge195_2 + drug_name_2 + judge195_3
        exp195_2 = judge195_1 + drug_name_2 + judge195_2 + drug_name + judge195_3

        exp196_1 = drug_name + judge196_1 + drug_name_2 + judge196_2
        exp196_2 = drug_name_2 + judge196_1 + drug_name + judge196_2

        exp197_1 = judge197_1 + drug_name + judge197_2 + drug_name_2 + judge197_3
        exp197_2 = judge197_1 + drug_name_2 + judge197_2 + drug_name + judge197_3

        exp198_1 = judge198_1 + drug_name + judge198_2 + drug_name_2 + judge198_3
        exp198_2 = judge198_1 + drug_name_2 + judge198_2 + drug_name + judge198_3

        exp199_1 = judge199_1 + drug_name + judge199_2 + drug_name_2 + judge199_3
        exp199_2 = judge199_1 + drug_name_2 + judge199_2 + drug_name + judge199_3

        exp200_1 = judge200_1 + drug_name + judge200_2 + drug_name_2 + judge200_3
        exp200_2 = judge200_1 + drug_name_2 + judge200_2 + drug_name + judge200_3

        exp201_1 = judge201_1 + drug_name + judge201_2 + drug_name_2 + judge201_3
        exp201_2 = judge201_1 + drug_name_2 + judge201_2 + drug_name + judge201_3

        exp202_1 = judge202_1 + drug_name + judge202_2 + drug_name_2 + judge202_3
        exp202_2 = judge202_1 + drug_name_2 + judge202_2 + drug_name + judge202_3

        exp203_1 = judge203_1 + drug_name + judge203_2 + drug_name_2 + judge203_3
        exp203_2 = judge203_1 + drug_name_2 + judge203_2 + drug_name + judge203_3

        exp204_1 = judge204_1 + drug_name + judge204_2 + drug_name_2 + judge204_3
        exp204_2 = judge204_1 + drug_name_2 + judge204_2 + drug_name + judge204_3

        exp205_1 = judge205_1 + drug_name + judge205_2 + drug_name_2 + judge205_3
        exp205_2 = judge205_1 + drug_name_2 + judge205_2 + drug_name + judge205_3

        exp206_1 = drug_name + judge206_1 + drug_name_2 + judge206_2
        exp206_2 = drug_name_2 + judge206_1 + drug_name + judge206_2

        exp207_1 = drug_name + judge207_1 + drug_name_2 + judge207_2
        exp207_2 = drug_name_2 + judge207_1 + drug_name + judge207_2

        exp208_1 = judge208_1 + drug_name + judge208_2 + drug_name_2 + judge208_3
        exp208_2 = judge208_1 + drug_name_2 + judge208_2 + drug_name + judge208_3

        exp209_1 = judge209_1 + drug_name + judge209_2 + drug_name_2 + judge209_3
        exp209_2 = judge209_1 + drug_name_2 + judge209_2 + drug_name + judge209_3

        exp210_1 = judge210_1 + drug_name + judge210_2 + drug_name_2 + judge210_3
        exp210_2 = judge210_1 + drug_name_2 + judge210_2 + drug_name + judge210_3

        exp211_1 = judge211_1 + drug_name + judge211_2 + drug_name_2 + judge211_3
        exp211_2 = judge211_1 + drug_name_2 + judge211_2 + drug_name + judge211_3

        exp212_1 = judge212_1 + drug_name + judge212_2 + drug_name_2 + judge212_3
        exp212_2 = judge212_1 + drug_name_2 + judge212_2 + drug_name + judge212_3

        exp213_1 = judge213_1 + drug_name + judge213_2 + drug_name_2 + judge213_3
        exp213_2 = judge213_1 + drug_name_2 + judge213_2 + drug_name + judge213_3

        exp214_1 = drug_name + judge214_1 + drug_name_2 + judge214_2
        exp214_2 = drug_name_2 + judge214_1 + drug_name + judge214_2

        exp215_1 = judge215_1 + drug_name + judge215_2 + drug_name_2 + judge215_3
        exp215_2 = judge215_1 + drug_name_2 + judge215_2 + drug_name + judge215_3

        exp216_1 = judge216_1 + drug_name + judge216_2 + drug_name_2 + judge216_3
        exp216_2 = judge216_1 + drug_name_2 + judge216_2 + drug_name + judge216_3

        exp217_1 = judge217_1 + drug_name + judge217_2 + drug_name_2 + judge217_3
        exp217_2 = judge217_1 + drug_name_2 + judge217_2 + drug_name + judge217_3

        exp218_1 = judge218_1 + drug_name + judge218_2 + drug_name_2 + judge218_3
        exp218_2 = judge218_1 + drug_name_2 + judge218_2 + drug_name + judge218_3

        exp219_1 = judge219_1 + drug_name + judge219_2 + drug_name_2 + judge219_3
        exp219_2 = judge219_1 + drug_name_2 + judge219_2 + drug_name + judge219_3

        exp220_1 = judge220_1 + drug_name + judge220_2 + drug_name_2 + judge220_3
        exp220_2 = judge220_1 + drug_name_2 + judge220_2 + drug_name + judge220_3

        exp221_1 = judge221_1 + drug_name + judge221_2 + drug_name_2 + judge221_3
        exp221_2 = judge221_1 + drug_name_2 + judge221_2 + drug_name + judge221_3

        exp222_1 = drug_name + judge222_1 + drug_name_2 + judge222_2
        exp222_2 = drug_name_2 + judge222_1 + drug_name + judge222_2

        exp223_1 = drug_name + judge223_1 + drug_name_2 + judge223_2
        exp223_2 = drug_name_2 + judge223_1 + drug_name + judge223_2

        exp224_1 = drug_name + judge224_1 + drug_name_2 + judge224_2
        exp224_2 = drug_name_2 + judge224_1 + drug_name + judge224_2

        exp225_1 = judge225_1 + drug_name + judge225_2 + drug_name_2 + judge225_3
        exp225_2 = judge225_1 + drug_name_2 + judge225_2 + drug_name + judge225_3

        exp226_1 = drug_name + judge226_1 + drug_name_2 + judge226_2
        exp226_2 = drug_name_2 + judge226_1 + drug_name + judge226_2

        exp227_1 = judge227_1 + drug_name + judge227_2 + drug_name_2 + judge227_3
        exp227_2 = judge227_1 + drug_name_2 + judge227_2 + drug_name + judge227_3

        exp228_1 = judge228_1 + drug_name + judge228_2 + drug_name_2 + judge228_3
        exp228_2 = judge228_1 + drug_name_2 + judge228_2 + drug_name + judge228_3

        exp229_1 = judge229_1 + drug_name + judge229_2 + drug_name_2 + judge229_3
        exp229_2 = judge229_1 + drug_name_2 + judge229_2 + drug_name + judge229_3

        exp230_1 = judge230_1 + drug_name + judge230_2 + drug_name_2 + judge230_3
        exp230_2 = judge230_1 + drug_name_2 + judge230_2 + drug_name + judge230_3

        exp231_1 = judge231_1 + drug_name + judge231_2 + drug_name_2 + judge231_3
        exp231_2 = judge231_1 + drug_name_2 + judge231_2 + drug_name + judge231_3

        exp232_1 = judge232_1 + drug_name + judge232_2 + drug_name_2 + judge232_3
        exp232_2 = judge232_1 + drug_name_2 + judge232_2 + drug_name + judge232_3

        exp233_1 = drug_name + judge233_1 + drug_name_2 + judge233_2
        exp233_2 = drug_name_2 + judge233_1 + drug_name + judge233_2

        exp234_1 = drug_name + judge234_1 + drug_name_2 + judge234_2
        exp234_2 = drug_name_2 + judge234_1 + drug_name + judge234_2

        exp235_1 = drug_name + judge235_1 + drug_name_2 + judge235_2
        exp235_2 = drug_name_2 + judge235_1 + drug_name + judge235_2

        exp236_1 = drug_name + judge236_1 + drug_name_2 + judge236_2
        exp236_2 = drug_name_2 + judge236_1 + drug_name + judge236_2

        exp237_1 = drug_name + judge237_1 + drug_name_2 + judge237_2
        exp237_2 = drug_name_2 + judge237_1 + drug_name + judge237_2

        exp238_1 = drug_name + judge238_1 + drug_name_2 + judge238_2
        exp238_2 = drug_name_2 + judge238_1 + drug_name + judge238_2

        exp239_1 = drug_name + judge239_1 + drug_name_2 + judge239_2
        exp239_2 = drug_name_2 + judge239_1 + drug_name + judge239_2

        exp240_1 = drug_name + judge240_1 + drug_name_2 + judge240_2
        exp240_2 = drug_name_2 + judge240_1 + drug_name + judge240_2

        exp241_1 = drug_name + judge241_1 + drug_name_2 + judge241_2
        exp241_2 = drug_name_2 + judge241_1 + drug_name + judge241_2

        exp242_1 = drug_name + judge242_1 + drug_name_2 + judge242_2
        exp242_2 = drug_name_2 + judge242_1 + drug_name + judge242_2

        exp243_1 = drug_name + judge243_1 + drug_name_2 + judge243_2
        exp243_2 = drug_name_2 + judge243_1 + drug_name + judge243_2

        exp244_1 = judge244_1 + drug_name + judge244_2 + drug_name_2 + judge244_3
        exp244_2 = judge244_1 + drug_name_2 + judge244_2 + drug_name + judge244_3

        exp245_1 = judge245_1 + drug_name + judge245_2 + drug_name_2 + judge245_3
        exp245_2 = judge245_1 + drug_name_2 + judge245_2 + drug_name + judge245_3

        exp246_1 = judge246_1 + drug_name + judge246_2 + drug_name_2 + judge246_3
        exp246_2 = judge246_1 + drug_name_2 + judge246_2 + drug_name + judge246_3

        exp247_1 = judge247_1 + drug_name + judge247_2 + drug_name_2 + judge247_3
        exp247_2 = judge247_1 + drug_name_2 + judge247_2 + drug_name + judge247_3

        exp248_1 = judge248_1 + drug_name + judge248_2 + drug_name_2 + judge248_3
        exp248_2 = judge248_1 + drug_name_2 + judge248_2 + drug_name + judge248_3

        exp249_1 = judge249_1 + drug_name + judge249_2 + drug_name_2 + judge249_3
        exp249_2 = judge249_1 + drug_name_2 + judge249_2 + drug_name + judge249_3

        exp250_1 = judge250_1 + drug_name + judge250_2 + drug_name_2 + judge250_3
        exp250_2 = judge250_1 + drug_name_2 + judge250_2 + drug_name + judge250_3

        exp251_1 = judge251_1 + drug_name + judge251_2 + drug_name_2 + judge251_3
        exp251_2 = judge251_1 + drug_name_2 + judge251_2 + drug_name + judge251_3

        exp252_1 = judge252_1 + drug_name + judge252_2 + drug_name_2 + judge252_3
        exp252_2 = judge252_1 + drug_name_2 + judge252_2 + drug_name + judge252_3

        exp253_1 = judge253_1 + drug_name + judge253_2 + drug_name_2 + judge253_3
        exp253_2 = judge253_1 + drug_name_2 + judge253_2 + drug_name + judge253_3

        exp254_1 = judge254_1 + drug_name + judge254_2 + drug_name_2 + judge254_3
        exp254_2 = judge254_1 + drug_name_2 + judge254_2 + drug_name + judge254_3

        exp255_1 = judge255_1 + drug_name + judge255_2 + drug_name_2 + judge255_3
        exp255_2 = judge255_1 + drug_name_2 + judge255_2 + drug_name + judge255_3

        exp256_1 = judge256_1 + drug_name + judge256_2 + drug_name_2 + judge256_3
        exp256_2 = judge256_1 + drug_name_2 + judge256_2 + drug_name + judge256_3

        exp257_1 = judge257_1 + drug_name + judge257_2 + drug_name_2 + judge257_3
        exp257_2 = judge257_1 + drug_name_2 + judge257_2 + drug_name + judge257_3

        exp258_1 = judge258_1 + drug_name + judge258_2 + drug_name_2 + judge258_3
        exp258_2 = judge258_1 + drug_name_2 + judge258_2 + drug_name + judge258_3

        exp259_1 = judge259_1 + drug_name + judge259_2 + drug_name_2 + judge259_3
        exp259_2 = judge259_1 + drug_name_2 + judge259_2 + drug_name + judge259_3

        exp260_1 = judge260_1 + drug_name + judge260_2 + drug_name_2 + judge260_3
        exp260_2 = judge260_1 + drug_name_2 + judge260_2 + drug_name + judge260_3

        exp261_1 = judge261_1 + drug_name + judge261_2 + drug_name_2 + judge261_3
        exp261_2 = judge261_1 + drug_name_2 + judge261_2 + drug_name + judge261_3

        exp262_1 = judge262_1 + drug_name + judge262_2 + drug_name_2 + judge262_3
        exp262_2 = judge262_1 + drug_name_2 + judge262_2 + drug_name + judge262_3

        exp263_1 = judge263_1 + drug_name + judge263_2 + drug_name_2 + judge263_3
        exp263_2 = judge263_1 + drug_name_2 + judge263_2 + drug_name + judge263_3

        exp264_1 = judge264_1 + drug_name + judge264_2 + drug_name_2 + judge264_3
        exp264_2 = judge264_1 + drug_name_2 + judge264_2 + drug_name + judge264_3

        exp265_1 = drug_name + judge265_1 + drug_name_2 + judge265_2
        exp265_2 = drug_name_2 + judge265_1 + drug_name + judge265_2

        exp266_1 = judge266_1 + drug_name + judge266_2 + drug_name_2 + judge266_3
        exp266_2 = judge266_1 + drug_name_2 + judge266_2 + drug_name + judge266_3

        exp267_1 = judge267_1 + drug_name + judge267_2 + drug_name_2 + judge267_3
        exp267_2 = judge267_1 + drug_name_2 + judge267_2 + drug_name + judge267_3

        exp268_1 = judge268_1 + drug_name + judge268_2 + drug_name_2 + judge268_3
        exp268_2 = judge268_1 + drug_name_2 + judge268_2 + drug_name + judge268_3

        exp269_1 = judge269_1 + drug_name + judge269_2 + drug_name_2 + judge269_3
        exp269_2 = judge269_1 + drug_name_2 + judge269_2 + drug_name + judge269_3

        exp270_1 = judge270_1 + drug_name + judge270_2 + drug_name_2 + judge270_3
        exp270_2 = judge270_1 + drug_name_2 + judge270_2 + drug_name + judge270_3

        exp271_1 = judge271_1 + drug_name + judge271_2 + drug_name_2 + judge271_3
        exp271_2 = judge271_1 + drug_name_2 + judge271_2 + drug_name + judge271_3

        exp272_1 = judge272_1 + drug_name + judge272_2 + drug_name_2 + judge272_3
        exp272_2 = judge272_1 + drug_name_2 + judge272_2 + drug_name + judge272_3

        exp273_1 = judge273_1 + drug_name + judge273_2 + drug_name_2 + judge273_3
        exp273_2 = judge273_1 + drug_name_2 + judge273_2 + drug_name + judge273_3

        exp274_1 = drug_name + judge274_1 + drug_name_2 + judge274_2
        exp274_2 = drug_name_2 + judge274_1 + drug_name + judge274_2

        exp = [exp1_1, exp1_2, exp2_1, exp2_2, exp3_1, exp3_2, exp4_1, exp4_2, exp5_1, exp5_2,
               exp6_1, exp6_2, exp7_1, exp7_2, exp8_1, exp8_2, exp9_1, exp9_2, exp10_1, exp10_2,
               exp11_1, exp11_2, exp12_1, exp12_2, exp13_1, exp13_2, exp14_1, exp14_2, exp15_1, exp15_2,
               exp16_1, exp16_2, exp17_1, exp17_2, exp18_1, exp18_2, exp19_1, exp19_2, exp20_1, exp20_2,
               exp21_1, exp21_2, exp22_1, exp22_2, exp23_1, exp23_2, exp24_1, exp24_2, exp25_1, exp25_2,
               exp26_1, exp26_2, exp27_1, exp27_2, exp28_1, exp28_2, exp29_1, exp29_2, exp30_1, exp30_2,
               exp31_1, exp31_2, exp32_1, exp32_2, exp33_1, exp33_2, exp34_1, exp34_2, exp35_1, exp35_2,
               exp36_1, exp36_2, exp37_1, exp37_2, exp38_1, exp38_2, exp39_1, exp39_2, exp40_1, exp40_2,
               exp41_1, exp41_2, exp42_1, exp42_2, exp43_1, exp43_2, exp44_1, exp44_2, exp45_1, exp45_2,
               exp46_1, exp46_2, exp47_1, exp47_2, exp48_1, exp48_2, exp49_1, exp49_2, exp50_1, exp50_2,
               exp51_1, exp51_2, exp52_1, exp52_2, exp53_1, exp53_2, exp54_1, exp54_2, exp55_1, exp55_2,
               exp56_1, exp56_2, exp57_1, exp57_2, exp58_1, exp58_2, exp59_1, exp59_2, exp60_1, exp60_2,
               exp61_1, exp61_2, exp62_1, exp62_2, exp63_1, exp63_2, exp64_1, exp64_2, exp65_1, exp65_2,
               exp66_1, exp66_2, exp67_1, exp67_2, exp68_1, exp68_2, exp69_1, exp69_2, exp70_1, exp70_2,
               exp71_1, exp71_2, exp72_1, exp72_2, exp73_1, exp73_2, exp74_1, exp74_2, exp75_1, exp75_2,
               exp76_1, exp76_2, exp77_1, exp77_2, exp78_1, exp78_2, exp79_1, exp79_2, exp80_1, exp80_2,
               exp81_1, exp81_2, exp82_1, exp82_2, exp83_1, exp83_2, exp84_1, exp84_2, exp85_1, exp85_2,
               exp86_1, exp86_2, exp87_1, exp87_2, exp88_1, exp88_2, exp89_1, exp89_2, exp90_1, exp90_2,
               exp91_1, exp91_2, exp92_1, exp92_2, exp93_1, exp93_2, exp94_1, exp94_2, exp95_1, exp95_2,
               exp96_1, exp96_2, exp97_1, exp97_2, exp98_1, exp98_2, exp99_1, exp99_2, exp100_1, exp100_2,
               exp101_1, exp101_2, exp102_1, exp102_2,exp103_1,exp103_2,exp104_1,exp104_2,exp105_1,exp105_2,
               exp106_1,exp106_2,exp108_1,exp108_2,exp110_1,exp110_2,exp111_1,exp111_2,exp112_1,exp112_2,
               exp113_1,exp113_2,exp114_1,exp114_2,exp115_1,exp115_2,
                exp116_1,exp116_2,exp117_1,exp117_2,exp118_1,exp118_2,exp119_1,exp119_2,exp120_1,exp120_2,
                exp121_1,exp121_2,exp122_1,exp122_2,exp123_1,exp123_2,exp124_1,exp124_2,exp125_1,exp125_2,
                exp126_1,exp126_2,exp127_1,exp127_2,exp128_1,exp128_2,exp129_1,exp129_2,exp130_1,exp130_2,
                exp131_1,exp131_2,exp132_1,exp132_2,exp133_1,exp133_2,exp134_1,exp134_2,exp135_1,exp135_2,
                exp136_1,exp136_2,exp137_1,exp137_2,exp138_1,exp138_2,exp139_1,exp139_2,exp140_1,exp140_2,
                exp141_1,exp141_2,exp142_1,exp142_2,exp143_1,exp143_2,exp144_1,exp144_2,exp145_1,exp145_2,
                exp146_1,exp146_2,exp147_1,exp147_2,exp148_1,exp148_2,exp149_1,exp149_2,exp150_1,exp150_2,
                exp151_1,exp151_2,exp152_1,exp152_2,exp153_1,exp153_2,exp154_1,exp154_2,exp155_1,exp155_2,
                exp156_1,exp156_2,exp157_1,exp157_2,exp158_1,exp158_2,exp159_1,exp159_2,exp160_1,exp160_2,
                exp161_1,exp161_2,exp162_1,exp162_2,exp163_1,exp163_2,exp164_1,exp164_2,exp165_1,exp165_2,
                exp166_1,exp166_2,exp167_1,exp167_2,exp168_1,exp168_2,exp169_1,exp169_2,exp170_1,exp170_2,
                exp171_1,exp171_2,exp172_1,exp172_2,exp173_1,exp173_2,exp174_1,exp174_2,exp175_1,exp175_2,
                exp176_1,exp176_2,exp177_1,exp177_2,exp178_1,exp178_2,exp179_1,exp179_2,exp180_1,exp180_2,
                exp181_1,exp181_2,exp182_1,exp182_2,exp183_1,exp183_2,exp184_1,exp184_2,exp185_1,exp185_2,
                exp186_1,exp186_2,exp187_1,exp187_2,exp188_1,exp188_2,exp189_1,exp189_2,exp190_1,exp190_2,
                exp191_1,exp191_2,exp192_1,exp192_2,exp193_1,exp193_2,exp194_1,exp194_2,exp195_1,exp195_2,
                exp196_1,exp196_2,exp197_1,exp197_2,exp198_1,exp198_2,exp199_1,exp199_2,exp200_1,exp200_2,
                exp201_1,exp201_2,exp202_1,exp202_2,exp203_1,exp203_2,exp204_1,exp204_2,exp205_1,exp205_2,
                exp206_1,exp206_2,exp207_1,exp207_2,exp208_1,exp208_2,exp209_1,exp209_2,exp210_1,exp210_2,
                exp211_1,exp211_2,exp212_1,exp212_2,exp213_1,exp213_2,exp214_1,exp214_2,exp215_1,exp215_2,
                exp216_1,exp216_2,exp217_1,exp217_2,exp218_1,exp218_2,exp219_1,exp219_2,exp220_1,exp220_2,
                exp221_1,exp221_2,exp222_1,exp222_2,exp223_1,exp223_2,exp224_1,exp224_2,exp225_1,exp225_2,
                exp226_1,exp226_2,exp227_1,exp227_2,exp228_1,exp228_2,exp229_1,exp229_2,exp230_1,exp230_2,
                exp231_1,exp231_2,exp232_1,exp232_2,exp233_1,exp233_2,exp234_1,exp234_2,exp235_1,exp235_2,
                exp236_1,exp236_2,exp237_1,exp237_2,exp238_1,exp238_2,exp239_1,exp239_2,exp240_1,exp240_2,
                exp241_1,exp241_2,exp242_1,exp242_2,exp243_1,exp243_2,exp244_1,exp244_2,exp245_1,exp245_2,
                exp246_1,exp246_2,exp247_1,exp247_2,exp248_1,exp248_2,exp249_1,exp249_2,exp250_1,exp250_2,
                exp251_1,exp251_2,exp252_1,exp252_2,exp253_1,exp253_2,exp254_1,exp254_2,exp255_1,exp255_2,
                exp256_1,exp256_2,exp257_1,exp257_2,exp258_1,exp258_2,exp259_1,exp259_2,exp260_1,exp260_2,
                exp261_1,exp261_2,exp262_1,exp262_2,exp263_1,exp263_2,exp264_1,exp264_2,exp265_1,exp265_2,
                exp266_1,exp266_2,exp267_1,exp267_2,exp268_1,exp268_2,exp269_1,exp269_2,exp270_1,exp270_2,
                exp271_1,exp271_2,exp272_1,exp272_2,exp273_1,exp273_2,exp274_1,exp274_2]
        result_str += '\n'
        # if drug_interaction[2].text not in exp:
        #     print(drug_interaction[2].text)
        #     print(drug_name)
        #     print(drug_name_2+"\n")
        # result_str +=drug_interaction[2].text
        #zch

        # 药物相互作用的说明
        # result_str += drug_interaction[2].text

        # increase 为1, decrease 为-1
        # if (drug_interaction[2].text.find('increase') != -1):
        #     result_str += '1'
        # elif (drug_interaction[2].text.find('decrease') != -1 or drug_interaction[2].text.find('reduce') != -1):
        #     result_str += '-1'
        # else:
        #     result_str += drug_interaction[2].text

        result_str += '\n'
    return result_str


def parsePolypeptide(drugElement, drug_pri_id, ns, lableName=""):
    result_str = ''
    lables = drugElement.find(ns + lableName)
    for lable in lables.iter(ns + lableName[0:-1]):
        result_str += drug_pri_id + ' '

        polypeptide = lable.find(ns + 'polypeptide')
        if (polypeptide is not None):
            result_str += polypeptide.get('id') + ' '
        else:
            result_str += ' ' * 6 + ' '

        for action in lable.find(ns + 'actions').iter(ns + 'action'):
            result_str += action.text + '/ '

        result_str += '\n'
    return result_str


if __name__ == '__main__':
    # lableNames = ['targets', 'enzymes', 'carriers', 'transporters']
    # for lableName in lableNames:
    #     parseXml(parsePolypeptide,
    #             inFile="full database.xml",
    #             outFile='drug_polypeptide_' + lableName + '.txt',
    #             lableName=lableName)
    parseXml(parseInteraction, inFile='./full database.xml', outFile='D:/muti_DDI.txt')
    print('done')
