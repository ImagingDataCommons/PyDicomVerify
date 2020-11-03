import re

def get_closest_body_part_examined(bpe: str):
    bpe = bpe.upper()
    bpe = re.sub(r'[^3-4A-Z]','', bpe)
    bpe = bpe[0] + re.sub(r'[^A-Z]', '', bpe[1:])
    output = ''
    bpes = list(BodyPartExamined2SCT)
    if bpe not in bpes:
        for bpe_el in bpes:
            if re.search(bpe, bpe_el) is not None:
                if len(bpe_el) < len(output) or output == '':
                    output = bpe_el
    if output == '':
        for bpe_el in bpes:
            if re.search(bpe_el, bpe) is not None:
                if len(bpe_el) > len(output):
                    output = bpe_el
    if output == '':
        output = None
    return output


BodyPartExamined2SCT = {
    '3RDVENTRICLE': (49841001, 'Third ventricle', 'SCT',),
    '4THVENTRICLE': (35918002, 'Fourth ventricle', 'SCT',),
    'ABDOMEN': (818981001, 'Abdomen', 'SCT',),
    'ABDOMENPELVIS': (818982008, 'Abdomen and Pelvis', 'SCT',),
    'ABDOMINALAORTA': (7832008, 'Abdominal aorta', 'SCT',),
    'ACA': (60176003, 'Anterior cerebral artery', 'SCT',),
    'ACJOINT': (85856004, 'Acromioclavicular joint', 'SCT',),
    'ADRENAL': (23451007, 'Adrenal gland', 'SCT',),
    'AMNIOTICFLUID': (77012006, 'Amniotic fluid', 'SCT',),
    'ANKLE': (70258002, 'Ankle joint', 'SCT',),
    'ANTCARDIACV': (194996006, 'Anterior cardiac vein', 'SCT',),
    'ANTCOMMA': (8012006, 'Anterior communicating artery', 'SCT',),
    'ANTECUBITALV': (128553008, 'Antecubital vein', 'SCT',),
    'ANTSPINALA': (17388009, 'Anterior spinal artery', 'SCT',),
    'ANTTIBIALA': (68053000, 'Anterior tibial artery', 'SCT',),
    'ANUSRECTUMSIGMD': (110612005, 'Anus, rectum and sigmoid colon', 'SCT',),
    'AORTA': (15825003, 'Aorta', 'SCT',),
    'AORTICARCH': (57034009, 'Aortic arch', 'SCT',),
    'APPENDIX': (66754008, 'Appendix', 'SCT',),
    'ARM': (40983000, 'Upper arm', 'SCT',),
    'ARTERY': (51114001, 'Artery', 'SCT',),
    'ASCAORTA': (54247002, 'Ascending aorta', 'SCT',),
    'ASCENDINGCOLON': (9040008, 'Ascending colon', 'SCT',),
    'AXILLA': (91470000, 'Axilla', 'SCT',),
    'AXILLARYA': (67937003, 'Axillary Artery', 'SCT',),
    'AXILLARYV': (68705008, 'Axillary vein', 'SCT',),
    'AZYGOSVEIN': (72107004, 'Azygos vein', 'SCT',),
    'BACK': (77568009, 'Back', 'SCT',),
    'BASILARA': (59011009, 'Basilar artery', 'SCT',),
    'BILEDUCT': (28273000, 'Bile duct', 'SCT',),
    'BLADDER': (89837001, 'Bladder', 'SCT',),
    'BLADDERURETHRA': (110837003, 'Bladder and urethra', 'SCT',),
    'BRACHIALA': (17137000, 'Brachial artery', 'SCT',),
    'BRACHIALV': (20115005, 'Brachial vein', 'SCT',),
    'BRAIN': (12738006, 'Brain', 'SCT',),
    'BREAST': (76752008, 'Breast', 'SCT',),
    'BRONCHUS': (955009, 'Bronchus', 'SCT',),
    'BULB': (21479005, 'Carotid bulb', 'SCT',),
    'BUTTOCK': (46862004, 'Buttock', 'SCT',),
    'CALCANEUS': (80144004, 'Calcaneus', 'SCT',),
    'CALF': (53840002, 'Calf of leg', 'SCT',),
    'CAROTID': (69105007, 'Carotid Artery', 'SCT',),
    'CCA': (32062004, 'Common carotid artery', 'SCT',),
    'CELIACA': (57850000, 'Celiac artery', 'SCT',),
    'CEPHALICV': (20699002, 'Cephalic vein', 'SCT',),
    'CEREBELLUM': (113305005, 'Cerebellum', 'SCT',),
    'CEREBHEMISPHERE': (372073000, 'Cerebral hemisphere', 'SCT',),
    'CEREBRALA': (88556005, 'Cerebral artery', 'SCT',),
    'CERVIX': (71252005, 'Cervix', 'SCT',),
    'CFA': (181347005, 'Common femoral artery', 'SCT',),
    'CFV': (397363009, 'Common femoral vein', 'SCT',),
    'CHEEK': (60819002, 'Cheek', 'SCT',),
    'CHEST': (43799004, 'Chest', 'SCT',),
    'CHESTABDOMEN': (416550000, 'Chest and Abdomen', 'SCT',),
    'CHESTABDPELVIS': (416775004, 'Chest, Abdomen and Pelvis', 'SCT',),
    'CHOROIDPLEXUS': (80621003, 'Choroid plexus', 'SCT',),
    'CIRCLEOFWILLIS': (11279006, 'Circle of Willis', 'SCT',),
    'CLAVICLE': (51299004, 'Clavicle', 'SCT',),
    'COCCYX': (64688005, 'Coccyx', 'SCT',),
    'COLON': (71854001, 'Colon', 'SCT',),
    'COMILIACA': (73634005, 'Common iliac artery', 'SCT',),
    'COMILIACV': (46027005, 'Common iliac vein', 'SCT',),
    'COMMONBILEDUCT': (79741001, 'Common bile duct', 'SCT',),
    'CORNEA': (28726007, 'Cornea', 'SCT',),
    'CORONARYARTERY': (41801008, 'Coronary artery', 'SCT',),
    'CORONARYSINUS': (90219004, 'Coronary sinus', 'SCT',),
    'CSPINE': (122494005, 'Cervical spine', 'SCT',),
    'CTSPINE': (297171002, 'Cervico-thoracic spine', 'SCT',),
    'CULDESAC': (53843000, 'Rectouterine pouch', 'SCT',),
    'DESCAORTA': (32672002, 'Descending aorta', 'SCT',),
    'DESCENDINGCOLON': (32622004, 'Descending colon', 'SCT',),
    'DUODENUM': (38848004, 'Duodenum', 'SCT',),
    'EAC': (84301002, 'External auditory canal', 'SCT',),
    'EAR': (117590005, 'Ear', 'SCT',),
    'ECA': (22286001, 'External carotid artery', 'SCT',),
    'ELBOW': (16953009, 'Elbow joint', 'SCT',),
    'ENDOARTERIAL': (51114001, 'Endo-arterial', 'SCT',),
    'ENDOCARDIAC': (80891009, 'Endo-cardiac', 'SCT',),
    'ENDOESOPHAGEAL': (32849002, 'Endo-esophageal', 'SCT',),
    'ENDOMETRIUM': (2739003, 'Endometrium', 'SCT',),
    'ENDONASAL': (53342003, 'Endo-nasal', 'SCT',),
    'ENDONASOPHARYNYX': (18962004, 'Endo-nasopharyngeal', 'SCT',),
    'ENDORECTAL': (34402009, 'Endo-rectal', 'SCT',),
    'ENDORENAL': (64033007, 'Endo-renal', 'SCT',),
    'ENDOURETERIC': (87953007, 'Endo-ureteric', 'SCT',),
    'ENDOURETHRAL': (13648007, 'Endo-urethral', 'SCT',),
    'ENDOVAGINAL': (76784001, 'Endo-vaginal', 'SCT',),
    'ENDOVASCULAR': (59820001, 'Endo-vascular', 'SCT',),
    'ENDOVENOUS': (29092000, 'Endo-venous', 'SCT',),
    'ENDOVESICAL': (48367006, 'Endo-vesical', 'SCT',),
    'EPIDIDYMIS': (87644002, 'Epididymis', 'SCT',),
    'EPIGASTRIC': (27947004, 'Epigastric region', 'SCT',),
    'ESOPHAGUS': (32849002, 'Esophagus', 'SCT',),
    'EXTILIACA': (113269004, 'External iliac artery', 'SCT',),
    'EXTILIACV': (63507001, 'External iliac vein', 'SCT',),
    'EXTJUGV': (71585003, 'External jugular vein', 'SCT',),
    'EXTREMITY': (66019005, 'Extremity', 'SCT',),
    'EYE': (81745001, 'Eye', 'SCT',),
    'EYELID': (80243003, 'Eyelid', 'SCT',),
    'FACE': (89545001, 'Face', 'SCT',),
    'FACIALA': (23074001, 'Facial artery', 'SCT',),
    'FEMORALA': (7657000, 'Femoral artery', 'SCT',),
    'FEMORALV': (83419000, 'Femoral vein', 'SCT',),
    'FEMUR': (71341001, 'Femur', 'SCT',),
    'FIBULA': (87342007, 'Fibula', 'SCT',),
    'FINGER': (7569003, 'Finger', 'SCT',),
    'FLANK': (58602004, 'Flank', 'SCT',),
    'FONTANEL': (79361005, 'Fontanel of skull', 'SCT',),
    'FOOT': (56459004, 'Foot', 'SCT',),
    'FOREARM': (14975008, 'Forearm', 'SCT',),
    'GALLBLADDER': (28231008, 'Gallbladder', 'SCT',),
    'GASTRICV': (110568007, 'Gastric vein', 'SCT',),
    'GENICULARA': (128559007, 'Genicular artery', 'SCT',),
    'GESTSAC': (300571009, 'Gestational sac', 'SCT',),
    'GLUTEAL': (46862004, 'Gluteal region', 'SCT',),
    'GSV': (60734001, 'Great saphenous vein', 'SCT',),
    'HAND': (85562004, 'Hand', 'SCT',),
    'HEAD': (69536005, 'Head', 'SCT',),
    'HEADNECK': (774007, 'Head and Neck', 'SCT',),
    'HEART': (80891009, 'Heart', 'SCT',),
    'HEPATICA': (76015000, 'Hepatic artery', 'SCT',),
    'HEPATICV': (8993003, 'Hepatic vein', 'SCT',),
    'HIP': (24136001, 'Hip joint', 'SCT',),
    'HUMERUS': (85050009, 'Humerus', 'SCT',),
    'HYPOGASTRIC': (11708003, 'Hypogastric region', 'SCT',),
    'HYPOPHARYNX': (81502006, 'Hypopharynx', 'SCT',),
    'IAC': (361078006, 'Internal Auditory Canal', 'SCT',),
    'ICA': (86117002, 'Internal carotid artery', 'SCT',),
    'ILEUM': (34516001, 'Ileum', 'SCT',),
    'ILIACA': (10293006, 'Iliac artery', 'SCT',),
    'ILIACV': (244411005, 'Iliac vein', 'SCT',),
    'ILIUM': (22356005, 'Ilium', 'SCT',),
    'INFMESA': (33795007, 'Inferior mesenteric artery', 'SCT',),
    'INFVENACAVA': (64131007, 'Inferior vena cava', 'SCT',),
    'INGUINAL': (26893007, 'Inguinal region', 'SCT',),
    'INNOMINATEA': (12691009, 'Innominate artery', 'SCT',),
    'INNOMINATEV': (8887007, 'Innominate vein', 'SCT',),
    'INTILIACA': (90024005, 'Internal iliac artery', 'SCT',),
    'INTJUGULARV': (12123001, 'Internal jugular vein', 'SCT',),
    'INTMAMMARYA': (69327007, 'Internal mammary artery', 'SCT',),
    'INTRACRANIAL': (1101003, 'Intracranial', 'SCT',),
    'JAW': (661005, 'Jaw region', 'SCT',),
    'JAW': (91609006, 'Mandible', 'SCT',),
    'JEJUNUM': (21306003, 'Jejunum', 'SCT',),
    'JOINT': (39352004, 'Joint', 'SCT',),
    'KIDNEY': (64033007, 'Kidney', 'SCT',),
    'KNEE': (72696002, 'Knee', 'SCT',),
    'LACRIMALA': (59749000, 'Lacrimal artery', 'SCT',),
    'LARGEINTESTINE': (14742008, 'Large intestine', 'SCT',),
    'LARYNX': (4596009, 'Larynx', 'SCT',),
    'LATRIUM': (82471001, 'Left atrium', 'SCT',),
    'LATVENTRICLE': (66720007, 'Lateral Ventricle', 'SCT',),
    'LEG': (30021000, 'Lower leg', 'SCT',),
    'LFEMORALA': (113270003, 'Left femoral artery', 'SCT',),
    'LHEPATICV': (273202007, 'Left hepatic vein', 'SCT',),
    'LHYPOCHONDRIAC': (133945003, 'Left hypochondriac region', 'SCT',),
    'LINGUALA': (113264009, 'Lingual artery', 'SCT',),
    'LINGUINAL': (85119005, 'Left inguinal region', 'SCT',),
    'LIVER': (10200004, 'Liver', 'SCT',),
    'LLQ': (68505006, 'Left lower quadrant of abdomen', 'SCT',),
    'LLUMBAR': (133943005, 'Left lumbar region', 'SCT',),
    'LPORTALV': (70253006, 'Left portal vein', 'SCT',),
    'LPULMONARYA': (50408007, 'Left pulmonary artery', 'SCT',),
    'LSPINE': (122496007, 'Lumbar spine', 'SCT',),
    'LSSPINE': (297173004, 'Lumbo-sacral spine', 'SCT',),
    'LSUPPULMONARYV': (43863001, 'Superior left pulmonary vein', 'SCT',),
    'LUMBAR': (52612000, 'Lumbar region', 'SCT',),
    'LUMBARA': (34635009, 'Lumbar artery', 'SCT',),
    'LUMEN': (91747007, 'Lumen of blood vessel', 'SCT',),
    'LUNG': (39607008, 'Lung', 'SCT',),
    'LUQ': (86367003, 'Left upper quadrant of abdomen', 'SCT',),
    'LVENTRICLE': (87878005, 'Left ventricle', 'SCT',),
    'MASTOID': (59066005, 'Mastoid bone', 'SCT',),
    'MAXILLA': (70925003, 'Maxilla', 'SCT',),
    'MCA': (17232002, 'Middle cerebral artery', 'SCT',),
    'MEDIASTINUM': (72410000, 'Mediastinum', 'SCT',),
    'MESENTRICA': (86570000, 'Mesenteric artery', 'SCT',),
    'MESENTRICV': (128583004, 'Mesenteric vein', 'SCT',),
    'MIDHEPATICV': (273099000, 'Middle hepatic vein', 'SCT',),
    'MORISONSPOUCH': (243977002, 'Morisons pouch', 'SCT',),
    'MOUTH': (123851003, 'Mouth', 'SCT',),
    'NASOPHARYNX': (360955006, 'Nasopharynx', 'SCT',),
    'NECK': (45048000, 'Neck', 'SCT',),
    'NECKCHEST': (417437006, 'Neck and Chest', 'SCT',),
    'NECKCHESTABDOMEN': (416152001, 'Neck, Chest and Abdomen', 'SCT',),
    'NECKCHESTABDPELV': (416319003, 'Neck, Chest, Abdomen and Pelvis', 'SCT',),
    'NOSE': (45206002, 'Nose', 'SCT',),
    'OCCIPTALV': (32114007, 'Occipital vein', 'SCT',),
    'OCCPITALA': (31145008, 'Occipital artery', 'SCT',),
    'OPHTHALMICA': (53549008, 'Ophthalmic artery', 'SCT',),
    'OPTICCANAL': (55024004, 'Optic canal', 'SCT',),
    'ORBIT': (363654007, 'Orbital structure', 'SCT',),
    'OVARY': (15497006, 'Ovary', 'SCT',),
    'PANCREAS': (15776009, 'Pancreas', 'SCT',),
    'PANCREATICDUCT': (69930009, 'Pancreatic duct', 'SCT',),
    'PARASTERNAL': (91691001, 'Parasternal', 'SCT',),
    'PARATHYROID': (111002, 'Parathyroid', 'SCT',),
    'PAROTID': (45289007, 'Parotid gland', 'SCT',),
    'PATELLA': (64234005, 'Patella', 'SCT',),
    'PCA': (70382005, 'Posterior cerebral artery', 'SCT',),
    'PELVIS': (816092008, 'Pelvis', 'SCT',),
    'PENILEA': (282044005, 'Penile artery', 'SCT',),
    'PENIS': (18911002, 'Penis', 'SCT',),
    'PERINEUM': (38864007, 'Perineum', 'SCT',),
    'PERONEALA': (8821006, 'Peroneal artery', 'SCT',),
    'PHARYNX': (54066008, 'Pharynx', 'SCT',),
    'PHARYNXLARYNX': (312535008, 'Pharynx and larynx', 'SCT',),
    'PLACENTA': (78067005, 'Placenta', 'SCT',),
    'POPLITEALA': (43899006, 'Popliteal artery', 'SCT',),
    'POPLITEALFOSSA': (32361000, 'Popliteal fossa', 'SCT',),
    'POPLITEALV': (56849005, 'Popliteal vein', 'SCT',),
    'PORTALV': (32764006, 'Portal vein', 'SCT',),
    'POSCOMMA': (43119007, 'Posterior communicating artery', 'SCT',),
    'POSTIBIALA': (13363002, 'Posterior tibial artery', 'SCT',),
    'PROFFEMA': (31677005, 'Profunda femoris artery', 'SCT',),
    'PROFFEMV': (23438002, 'Profunda femoris vein', 'SCT',),
    'PROSTATE': (41216001, 'Prostate', 'SCT',),
    'PULMONARYA': (81040000, 'Pulmonary artery', 'SCT',),
    'PULMONARYV': (122972007, 'Pulmonary vein', 'SCT',),
    'RADIALA': (45631007, 'Radial artery', 'SCT',),
    'RADIUS': (62413002, 'Radius', 'SCT',),
    'RADIUSULNA': (110535000, 'Radius and ulna', 'SCT',),
    'RATRIUM': (73829009, 'Right atrium', 'SCT',),
    'RECTUM': (34402009, 'Rectum', 'SCT',),
    'RENALA': (2841007, 'Renal artery', 'SCT',),
    'RENALV': (56400007, 'Renal vein', 'SCT',),
    'RETROPERITONEUM': (82849001, 'Retroperitoneum', 'SCT',),
    'RFEMORALA': (69833005, 'Right femoral artery', 'SCT',),
    'RHEPATICV': (272998002, 'Right hepatic vein', 'SCT',),
    'RHYPOCHONDRIAC': (133946002, 'Right hypochondriac region', 'SCT',),
    'RIB': (113197003, 'Rib', 'SCT',),
    'RINGUINAL': (37117007, 'Right inguinal region', 'SCT',),
    'RLQ': (48544008, 'Right lower quadrant of abdomen', 'SCT',),
    'RLUMBAR': (133944004, 'Right lumbar region', 'SCT',),
    'RPORTALV': (73931004, 'Right portal vein', 'SCT',),
    'RPULMONARYA': (78480002, 'Right pulmonary artery', 'SCT',),
    'RSUPPULMONARYV': (8629005, 'Superior right pulmonary vein', 'SCT',),
    'RUQ': (50519007, 'Right upper quadrant of abdomen', 'SCT',),
    'RVENTRICLE': (53085002, 'Right ventricle', 'SCT',),
    'SAPHENOUSV': (362072009, 'Saphenous vein', 'SCT',),
    'SCALP': (41695006, 'Scalp', 'SCT',),
    'SCAPULA': (79601000, 'Scapula', 'SCT',),
    'SCJOINT': (7844006, 'Sternoclavicular joint', 'SCT',),
    'SCLERA': (18619003, 'Sclera', 'SCT',),
    'SCROTUM': (20233005, 'Scrotum', 'SCT',),
    'SELLA': (42575006, 'Sella turcica', 'SCT',),
    'SEMVESICLE': (64739004, 'Seminal vesicle', 'SCT',),
    'SESAMOID': (58742003, 'Sesamoid bones of foot', 'SCT',),
    'SFA': (181349008, 'Superficial femoral artery', 'SCT',),
    'SFJ': (128587003, 'Saphenofemoral junction', 'SCT',),
    'SFV': (397364003, 'Superficial femoral vein', 'SCT',),
    'SHOULDER': (16982005, 'Shoulder', 'SCT',),
    'SIGMOID': (60184004, 'Sigmoid colon', 'SCT',),
    'SIJOINT': (39723000, 'Sacroiliac joint', 'SCT',),
    'SKULL': (89546000, 'Skull', 'SCT',),
    'SMA': (42258001, 'Superior mesenteric artery', 'SCT',),
    'SMALLINTESTINE': (30315005, 'Small intestine', 'SCT',),
    'SPINALCORD': (2748008, 'Spinal cord', 'SCT',),
    'SPINE': (421060004, 'Spine', 'SCT',),
    'SPLEEN': (78961009, 'Spleen', 'SCT',),
    'SPLENICA': (22083002, 'Splenic artery', 'SCT',),
    'SPLENICV': (35819009, 'Splenic vein', 'SCT',),
    'SSPINE': (54735007, 'Sacrum', 'SCT',),
    'STERNUM': (56873002, 'Sternum', 'SCT',),
    'STOMACH': (69695003, 'Stomach', 'SCT',),
    'SUBCLAVIANA': (36765005, 'Subclavian artery', 'SCT',),
    'SUBCLAVIANV': (9454009, 'Subclavian vein', 'SCT',),
    'SUBCOSTAL': (19695001, 'Subcostal', 'SCT',),
    'SUBMANDIBULAR': (54019009, 'Submandibular gland', 'SCT',),
    'SUPRACLAVICULAR': (77621008, 'Supraclavicular region of neck', 'SCT',),
    'SUPRAPUBIC': (11708003, 'Suprapubic region', 'SCT',),
    'SUPTHYROIDA': (72021004, 'Superior thyroid artery', 'SCT',),
    'SVC': (48345005, 'Superior vena cava', 'SCT',),
    'TESTIS': (40689003, 'Testis', 'SCT',),
    'THALAMUS': (42695009, 'Thalamus', 'SCT',),
    'THIGH': (68367000, 'Thigh', 'SCT',),
    'THORACICAORTA': (113262008, 'Thoracic aorta', 'SCT',),
    'THORAX': (43799004, 'Thorax', 'SCT',),
    'THUMB': (76505004, 'Thumb', 'SCT',),
    'THYMUS': (9875009, 'Thymus', 'SCT',),
    'THYROID': (69748006, 'Thyroid', 'SCT',),
    'TIBIA': (12611008, 'Tibia', 'SCT',),
    'TIBIAFIBULA': (110536004, 'Tibia and fibula', 'SCT',),
    'TLSPINE': (297172009, 'Thoraco-lumbar spine', 'SCT',),
    'TMJ': (53620006, 'Temporomandibular joint', 'SCT',),
    'TOE': (29707007, 'Toe', 'SCT',),
    'TONGUE': (21974007, 'Tongue', 'SCT',),
    'TRACHEA': (44567001, 'Trachea', 'SCT',),
    'TRACHEABRONCHUS': (110726009, 'Trachea and bronchus', 'SCT',),
    'TRANSVERSECOLON': (485005, 'Transverse colon', 'SCT',),
    'TSPINE': (122495006, 'Thoracic spine', 'SCT',),
    'ULNA': (23416004, 'Ulna', 'SCT',),
    'ULNARA': (44984001, 'Ulnar artery', 'SCT',),
    'UMBILICAL': (90290004, 'Umbilical region', 'SCT',),
    'UMBILICALA': (50536004, 'Umbilical artery', 'SCT',),
    'UMBILICALV': (284639000, 'Umbilical vein', 'SCT',),
    'UPRURINARYTRACT': (431491007, 'Upper urinary tract', 'SCT',),
    'URETER': (87953007, 'Ureter', 'SCT',),
    'URETHRA': (13648007, 'Urethra', 'SCT',),
    'UTERUS': (35039007, 'Uterus', 'SCT',),
    'VAGINA': (76784001, 'Vagina', 'SCT',),
    'VEIN': (29092000, 'Vein', 'SCT',),
    'VERTEBRALA': (85234005, 'Vertebral artery', 'SCT',),
    'VULVA': (45292006, 'Vulva', 'SCT',),
    'WHOLEBODY': (38266002, 'Entire body', 'SCT',),
    'WRIST': (74670003, 'Wrist joint', 'SCT',),
    'ZYGOMA': (13881006, 'Zygoma', 'SCT',),
}
SCT2BodyPartExamined = {
    111002: 'PARATHYROID',
    485005: 'TRANSVERSECOLON',
    661005: 'JAW',
    774007: 'HEADNECK',
    955009: 'BRONCHUS',
    1101003: 'INTRACRANIAL',
    2739003: 'ENDOMETRIUM',
    2748008: 'SPINALCORD',
    2841007: 'RENALA',
    4596009: 'LARYNX',
    7569003: 'FINGER',
    7657000: 'FEMORALA',
    7832008: 'ABDOMINALAORTA',
    7844006: 'SCJOINT',
    8012006: 'ANTCOMMA',
    8629005: 'RSUPPULMONARYV',
    8821006: 'PERONEALA',
    8887007: 'INNOMINATEV',
    8993003: 'HEPATICV',
    9040008: 'ASCENDINGCOLON',
    9454009: 'SUBCLAVIANV',
    9875009: 'THYMUS',
    10200004: 'LIVER',
    10293006: 'ILIACA',
    11279006: 'CIRCLEOFWILLIS',
    11708003: 'HYPOGASTRIC',
    11708003: 'SUPRAPUBIC',
    12123001: 'INTJUGULARV',
    12611008: 'TIBIA',
    12691009: 'INNOMINATEA',
    12738006: 'BRAIN',
    13363002: 'POSTIBIALA',
    13648007: 'ENDOURETHRAL',
    13648007: 'URETHRA',
    13881006: 'ZYGOMA',
    14742008: 'LARGEINTESTINE',
    14975008: 'FOREARM',
    15497006: 'OVARY',
    15776009: 'PANCREAS',
    15825003: 'AORTA',
    16953009: 'ELBOW',
    16982005: 'SHOULDER',
    17137000: 'BRACHIALA',
    17232002: 'MCA',
    17388009: 'ANTSPINALA',
    18619003: 'SCLERA',
    18911002: 'PENIS',
    18962004: 'ENDONASOPHARYNYX',
    19695001: 'SUBCOSTAL',
    20115005: 'BRACHIALV',
    20233005: 'SCROTUM',
    20699002: 'CEPHALICV',
    21306003: 'JEJUNUM',
    21479005: 'BULB',
    21974007: 'TONGUE',
    22083002: 'SPLENICA',
    22286001: 'ECA',
    22356005: 'ILIUM',
    23074001: 'FACIALA',
    23416004: 'ULNA',
    23438002: 'PROFFEMV',
    23451007: 'ADRENAL',
    24136001: 'HIP',
    26893007: 'INGUINAL',
    27947004: 'EPIGASTRIC',
    28231008: 'GALLBLADDER',
    28273000: 'BILEDUCT',
    28726007: 'CORNEA',
    29092000: 'ENDOVENOUS',
    29092000: 'VEIN',
    29707007: 'TOE',
    30021000: 'LEG',
    30315005: 'SMALLINTESTINE',
    31145008: 'OCCPITALA',
    31677005: 'PROFFEMA',
    32062004: 'CCA',
    32114007: 'OCCIPTALV',
    32361000: 'POPLITEALFOSSA',
    32622004: 'DESCENDINGCOLON',
    32672002: 'DESCAORTA',
    32764006: 'PORTALV',
    32849002: 'ENDOESOPHAGEAL',
    32849002: 'ESOPHAGUS',
    33795007: 'INFMESA',
    34402009: 'ENDORECTAL',
    34402009: 'RECTUM',
    34516001: 'ILEUM',
    34635009: 'LUMBARA',
    35039007: 'UTERUS',
    35819009: 'SPLENICV',
    35918002: '4THVENTRICLE',
    36765005: 'SUBCLAVIANA',
    37117007: 'RINGUINAL',
    38266002: 'WHOLEBODY',
    38848004: 'DUODENUM',
    38864007: 'PERINEUM',
    39352004: 'JOINT',
    39607008: 'LUNG',
    39723000: 'SIJOINT',
    40689003: 'TESTIS',
    40983000: 'ARM',
    41216001: 'PROSTATE',
    41695006: 'SCALP',
    41801008: 'CORONARYARTERY',
    42258001: 'SMA',
    42575006: 'SELLA',
    42695009: 'THALAMUS',
    43119007: 'POSCOMMA',
    43799004: 'CHEST',
    43799004: 'THORAX',
    43863001: 'LSUPPULMONARYV',
    43899006: 'POPLITEALA',
    44567001: 'TRACHEA',
    44984001: 'ULNARA',
    45048000: 'NECK',
    45206002: 'NOSE',
    45289007: 'PAROTID',
    45292006: 'VULVA',
    45631007: 'RADIALA',
    46027005: 'COMILIACV',
    46862004: 'BUTTOCK',
    46862004: 'GLUTEAL',
    48345005: 'SVC',
    48367006: 'ENDOVESICAL',
    48544008: 'RLQ',
    49841001: '3RDVENTRICLE',
    50408007: 'LPULMONARYA',
    50519007: 'RUQ',
    50536004: 'UMBILICALA',
    51114001: 'ARTERY',
    51114001: 'ENDOARTERIAL',
    51299004: 'CLAVICLE',
    52612000: 'LUMBAR',
    53085002: 'RVENTRICLE',
    53342003: 'ENDONASAL',
    53549008: 'OPHTHALMICA',
    53620006: 'TMJ',
    53840002: 'CALF',
    53843000: 'CULDESAC',
    54019009: 'SUBMANDIBULAR',
    54066008: 'PHARYNX',
    54247002: 'ASCAORTA',
    54735007: 'SSPINE',
    55024004: 'OPTICCANAL',
    56400007: 'RENALV',
    56459004: 'FOOT',
    56849005: 'POPLITEALV',
    56873002: 'STERNUM',
    57034009: 'AORTICARCH',
    57850000: 'CELIACA',
    58602004: 'FLANK',
    58742003: 'SESAMOID',
    59011009: 'BASILARA',
    59066005: 'MASTOID',
    59749000: 'LACRIMALA',
    59820001: 'ENDOVASCULAR',
    60176003: 'ACA',
    60184004: 'SIGMOID',
    60734001: 'GSV',
    60819002: 'CHEEK',
    62413002: 'RADIUS',
    63507001: 'EXTILIACV',
    64033007: 'ENDORENAL',
    64033007: 'KIDNEY',
    64131007: 'INFVENACAVA',
    64234005: 'PATELLA',
    64688005: 'COCCYX',
    64739004: 'SEMVESICLE',
    66019005: 'EXTREMITY',
    66720007: 'LATVENTRICLE',
    66754008: 'APPENDIX',
    67937003: 'AXILLARYA',
    68053000: 'ANTTIBIALA',
    68367000: 'THIGH',
    68505006: 'LLQ',
    68705008: 'AXILLARYV',
    69105007: 'CAROTID',
    69327007: 'INTMAMMARYA',
    69536005: 'HEAD',
    69695003: 'STOMACH',
    69748006: 'THYROID',
    69833005: 'RFEMORALA',
    69930009: 'PANCREATICDUCT',
    70253006: 'LPORTALV',
    70258002: 'ANKLE',
    70382005: 'PCA',
    70925003: 'MAXILLA',
    71252005: 'CERVIX',
    71341001: 'FEMUR',
    71585003: 'EXTJUGV',
    71854001: 'COLON',
    72021004: 'SUPTHYROIDA',
    72107004: 'AZYGOSVEIN',
    72410000: 'MEDIASTINUM',
    72696002: 'KNEE',
    73634005: 'COMILIACA',
    73829009: 'RATRIUM',
    73931004: 'RPORTALV',
    74670003: 'WRIST',
    76015000: 'HEPATICA',
    76505004: 'THUMB',
    76752008: 'BREAST',
    76784001: 'ENDOVAGINAL',
    76784001: 'VAGINA',
    77012006: 'AMNIOTICFLUID',
    77568009: 'BACK',
    77621008: 'SUPRACLAVICULAR',
    78067005: 'PLACENTA',
    78480002: 'RPULMONARYA',
    78961009: 'SPLEEN',
    79361005: 'FONTANEL',
    79601000: 'SCAPULA',
    79741001: 'COMMONBILEDUCT',
    80144004: 'CALCANEUS',
    80243003: 'EYELID',
    80621003: 'CHOROIDPLEXUS',
    80891009: 'ENDOCARDIAC',
    80891009: 'HEART',
    81040000: 'PULMONARYA',
    81502006: 'HYPOPHARYNX',
    81745001: 'EYE',
    82471001: 'LATRIUM',
    82849001: 'RETROPERITONEUM',
    83419000: 'FEMORALV',
    84301002: 'EAC',
    85050009: 'HUMERUS',
    85119005: 'LINGUINAL',
    85234005: 'VERTEBRALA',
    85562004: 'HAND',
    85856004: 'ACJOINT',
    86117002: 'ICA',
    86367003: 'LUQ',
    86570000: 'MESENTRICA',
    87342007: 'FIBULA',
    87644002: 'EPIDIDYMIS',
    87878005: 'LVENTRICLE',
    87953007: 'ENDOURETERIC',
    87953007: 'URETER',
    88556005: 'CEREBRALA',
    89545001: 'FACE',
    89546000: 'SKULL',
    89837001: 'BLADDER',
    90024005: 'INTILIACA',
    90219004: 'CORONARYSINUS',
    90290004: 'UMBILICAL',
    91470000: 'AXILLA',
    91609006: 'JAW',
    91691001: 'PARASTERNAL',
    91747007: 'LUMEN',
    110535000: 'RADIUSULNA',
    110536004: 'TIBIAFIBULA',
    110568007: 'GASTRICV',
    110612005: 'ANUSRECTUMSIGMD',
    110726009: 'TRACHEABRONCHUS',
    110837003: 'BLADDERURETHRA',
    113197003: 'RIB',
    113262008: 'THORACICAORTA',
    113264009: 'LINGUALA',
    113269004: 'EXTILIACA',
    113270003: 'LFEMORALA',
    113305005: 'CEREBELLUM',
    117590005: 'EAR',
    122494005: 'CSPINE',
    122495006: 'TSPINE',
    122496007: 'LSPINE',
    122972007: 'PULMONARYV',
    123851003: 'MOUTH',
    128553008: 'ANTECUBITALV',
    128559007: 'GENICULARA',
    128583004: 'MESENTRICV',
    128587003: 'SFJ',
    133943005: 'LLUMBAR',
    133944004: 'RLUMBAR',
    133945003: 'LHYPOCHONDRIAC',
    133946002: 'RHYPOCHONDRIAC',
    181347005: 'CFA',
    181349008: 'SFA',
    194996006: 'ANTCARDIACV',
    243977002: 'MORISONSPOUCH',
    244411005: 'ILIACV',
    272998002: 'RHEPATICV',
    273099000: 'MIDHEPATICV',
    273202007: 'LHEPATICV',
    282044005: 'PENILEA',
    284639000: 'UMBILICALV',
    297171002: 'CTSPINE',
    297172009: 'TLSPINE',
    297173004: 'LSSPINE',
    300571009: 'GESTSAC',
    312535008: 'PHARYNXLARYNX',
    360955006: 'NASOPHARYNX',
    361078006: 'IAC',
    362072009: 'SAPHENOUSV',
    363654007: 'ORBIT',
    372073000: 'CEREBHEMISPHERE',
    397363009: 'CFV',
    397364003: 'SFV',
    416152001: 'NECKCHESTABDOMEN',
    416319003: 'NECKCHESTABDPELV',
    416550000: 'CHESTABDOMEN',
    416775004: 'CHESTABDPELVIS',
    417437006: 'NECKCHEST',
    421060004: 'SPINE',
    431491007: 'UPRURINARYTRACT',
    816092008: 'PELVIS',
    818981001: 'ABDOMEN',
    818982008: 'ABDOMENPELVIS',
}
SRT2BodyPartExamined ={
    'F-03FC9': 'RADIALA',
    'G-035A': 'RIB',
    'G-035B': 'SCROTUM',
    'R-FAB52': 'FEMUR',
    'R-FAB53': 'EXTJUGV',
    'R-FAB54': 'COLON',
    'R-FAB55': 'BULB',
    'R-FAB56': 'TONGUE',
    'T-04000': 'LARGEINTESTINE',
    'T-11100': 'LFEMORALA',
    'T-11102': 'COMILIACA',
    'T-11133': 'INTMAMMARYA',
    'T-11166': 'FETALPOLE',
    'T-11170': 'HEAD',
    'T-11180': 'STERNUM',
    'T-11210': 'GENICULARA',
    'T-11300': 'LVENTRICLE',
    'T-11501': 'BILEDUCT',
    'T-11502': 'CFV',
    'T-11503': 'EXTREMITY',
    'T-11AD0': 'ANTECUBITALV',
    'T-11BF0': 'FACIALA',
    'T-12280': 'JAW',
    'T-12310': 'ILIUM',
    'T-12340': 'TMJ',
    'T-12403': 'LINGUINAL',
    'T-12410': 'UMBILICALA',
    'T-12420': 'HUMERUS',
    'T-12430': 'SFV',
    'T-12701': 'LSSPINE',
    'T-12710': 'CORONARYARTERY',
    'T-12730': 'VAGINA',
    'T-12740': 'TLSPINE',
    'T-12750': 'THORAX',
    'T-12770': 'AORTA',
    'T-12980': 'ANUSRECTUMSIGMD',
    'T-15001': 'CELIACA',
    'T-15200': 'TRACHEA',
    'T-15290': 'PHARYNXLARYNX',
    'T-15420': 'ENDOMETRIUM',
    'T-15430': 'CCA',
    'T-15460': 'FETALLEG',
    'T-15610': 'PARASTERNAL',
    'T-15680': 'EXTILIACA',
    'T-15710': 'RUQ',
    'T-15750': 'LARYNX',
    'T-20101': 'SCAPULA',
    'T-21000': 'SUPTHYROIDA',
    'T-21300': 'PORTALV',
    'T-2300C': 'MAXILLA',
    'T-23050': 'ENDOESOPHAGEAL',
    'T-24100': 'LACRIMALA',
    'T-25000': 'SAPHENOUSV',
    'T-26000': 'FOREARM',
    'T-28000': 'LLQ',
    'T-32000': 'POPLITEALFOSSA',
    'T-32000': 'RLQ',
    'T-32200': 'VERTEBRALA',
    'T-32300': 'ENDOVASCULAR',
    'T-32500': 'CORONARYSINUS',
    'T-32600': 'CAROTID',
    'T-40000': 'LUMBARA',
    'T-40230': 'THIGH',
    'T-41000': 'SUBCLAVIANV',
    'T-41000': 'OCCIPTALV',
    'T-42000': 'PERONEALA',
    'T-42070': 'MIDHEPATICV',
    'T-42100': 'THYMUS',
    'T-42300': 'INNOMINATEV',
    'T-42400': 'VEIN',
    'T-42500': 'BRONCHUS',
    'T-43000': 'EPIGASTRIC',
    'T-44000': 'RETROPERITONEUM',
    'T-44200': 'SKULL',
    'T-44400': 'SEMVESICLE',
    'T-45010': 'SHOULDER',
    'T-45100': 'BRACHIALA',
    'T-45170': 'OVARY',
    'T-45200': 'PROFFEMA',
    'T-45210': 'SFA',
    'T-45230': 'EXTILIACV',
    'T-45240': 'ARM',
    'T-45250': 'MEDIASTINUM',
    'T-45300': 'LUMBAR',
    'T-45320': 'HEART',
    'T-45400': 'KNEE',
    'T-45410': 'BASILARA',
    'T-45510': 'ENDONASOPHARYNYX',
    'T-45520': 'ECA',
    'T-45530': 'FEMORALA',
    'T-45540': 'INTRACRANIAL',
    'T-45600': 'STOMACH',
    'T-45700': 'FETALARM',
    'T-45730': 'SCJOINT',
    'T-45800': 'TIBIA',
    'T-45900': 'AMNIOTICFLUID',
    'T-46010': 'PHARYNX',
    'T-46100': 'SFJ',
    'T-46200': 'RENALV',
    'T-46400': 'MCA',
    'T-46420': '3RDVENTRICLE',
    'T-46460': 'PULMONARYV',
    'T-46500': 'RFEMORALA',
    'T-46510': 'CEREBELLUM',
    'T-46520': 'CALF',
    'T-46600': 'ACJOINT',
    'T-46700': 'ENDONASAL',
    'T-46710': 'PROFFEMV',
    'T-46740': 'SSPINE',
    'T-46807': 'SUPRACLAVICULAR',
    'T-46910': 'WHOLEBODY',
    'T-46960': 'ANTTIBIALA',
    'T-47100': 'CIRCLEOFWILLIS',
    'T-47160': 'ENDOURETHRAL',
    'T-47200': 'NECKCHESTABDOMEN',
    'T-47300': 'EAC',
    'T-47400': 'PROSTATE',
    'T-47402': 'BRACHIALV',
    'T-47403': 'TRACHEABRONCHUS',
    'T-47410': 'MESENTRICA',
    'T-47420': 'GSV',
    'T-47440': 'HYPOPHARYNX',
    'T-47490': 'VULVA',
    'T-47500': 'CALCANEUS',
    'T-47600': 'PULMONARYA',
    'T-47630': 'SPLEEN',
    'T-47700': 'ANTCOMMA',
    'T-48000': 'UTERUS',
    'T-48000': 'ABDOMENPELVIS',
    'T-48160': 'PERINEUM',
    'T-48170': 'OPTICCANAL',
    'T-48214': 'AZYGOSVEIN',
    'T-48330': 'LLUMBAR',
    'T-48340': 'SUPRAPUBIC',
    'T-48403': 'FINGER',
    'T-48410': 'GALLBLADDER',
    'T-48510': 'BLADDER',
    'T-48530': 'APPENDIX',
    'T-48581': 'FEMORALV',
    'T-48610': 'ANTCARDIACV',
    'T-48620': 'ASCAORTA',
    'T-48710': 'CULDESAC',
    'T-48720': 'LPULMONARYA',
    'T-48725': 'FIBULA',
    'T-48726': 'LPORTALV',
    'T-48727': 'CHEEK',
    'T-48740': 'ICA',
    'T-48810': 'ENDOCARDIAC',
    'T-48813': 'FACE',
    'T-48814': 'COCCYX',
    'T-48820': 'PAROTID',
    'T-48832': 'CHESTABDPELVIS',
    'T-4884A': 'PANCREATICDUCT',
    'T-48890': 'MOUTH',
    'T-48920': 'ADRENAL',
    'T-48930': 'DUODENUM',
    'T-49110': 'HYPOGASTRIC',
    'T-49215': 'ABDOMINALAORTA',
    'T-49240': 'ANTSPINALA',
    'T-49350': 'URETHRA',
    'T-4940B': 'UMBILICAL',
    'T-4940E': 'OPHTHALMICA',
    'T-49410': 'SCALP',
    'T-49530': 'BUTTOCK',
    'T-49650': 'CHOROIDPLEXUS',
    'T-49660': 'EYE',
    'T-53000': 'IAC',
    'T-55000': 'FONTANEL',
    'T-55300': 'ENDOARTERIAL',
    'T-56000': 'DESCENDINGCOLON',
    'T-56000': 'RINGUINAL',
    'T-57000': 'MESENTRICV',
    'T-58000': 'EAR',
    'T-58200': 'LEG',
    'T-58400': 'AORTICARCH',
    'T-58600': 'RVENTRICLE',
    'T-59000': 'MASTOID',
    'T-59200': 'HEPATICV',
    'T-59300': 'ULNA',
    'T-59420': 'LIVER',
    'T-59440': 'CEREBHEMISPHERE',
    'T-59460': 'TOE',
    'T-59470': 'LINGUALA',
    'T-59490': 'RSUPPULMONARYV',
    'T-59600': 'ESOPHAGUS',
    'T-59600': 'HAND',
    'T-60610': 'INNOMINATEA',
    'T-61100': 'ENDOVAGINAL',
    'T-61300': 'LHYPOCHONDRIAC',
    'T-62000': 'KIDNEY',
    'T-63000': 'NOSE',
    'T-64500': 'HIP',
    'T-65000': 'WRIST',
    'T-65010': 'HEPATICA',
    'T-7000B': 'NECKCHEST',
    'T-71000': 'INFMESA',
    'T-71000': 'FLANK',
    'T-73000': 'ENDORECTAL',
    'T-73000': 'SPINE',
    'T-74000': 'BRAIN',
    'T-74250': 'SPLENICV',
    'T-75000': 'RECTUM',
    'T-75000': 'UPRURINARYTRACT',
    'T-81000': 'FETALDIGIT',
    'T-82000': 'ILEUM',
    'T-82000': 'ABDOMEN',
    'T-83000': 'PELVIS',
    'T-83200': 'SUBCOSTAL',
    'T-83400': 'DESCAORTA',
    'T-87000': 'RPORTALV',
    'T-91000': 'PLACENTA',
    'T-92000': 'LATRIUM',
    'T-93000': 'GASTRICV',
    'T-94000': 'MORISONSPOUCH',
    'T-95000': '4THVENTRICLE',
    'T-98000': 'RADIUSULNA',
    'T-A0100': 'ZYGOMA',
    'T-A010F': 'PENIS',
    'T-A1650': 'ACA',
    'T-A1740': 'PARATHYROID',
    'T-A1820': 'TRANSVERSECOLON',
    'T-A1900': 'SPLENICA',
    'T-A4000': 'ILIACV',
    'T-A6000': 'SCLERA',
    'T-A7010': 'CSPINE',
    'T-AA000': 'LUNG',
    'T-AA110': 'LUMEN',
    'T-AA200': 'INGUINAL',
    'T-AA810': 'SIJOINT',
    'T-AB001': 'OCCPITALA',
    'T-AB200': 'SMALLINTESTINE',
    'T-AB959': 'CLAVICLE',
    'T-B3000': 'SPINALCORD',
    'T-B6000': 'CTSPINE',
    'T-B7000': 'BREAST',
    'T-C3000': 'LSPINE',
    'T-C8000': 'UMBILICALV',
    'T-D0010': 'FETALHEART',
    'T-D00F7': 'CORNEA',
    'T-D00F8': 'GESTSAC',
    'T-D00F9': 'LATVENTRICLE',
    'T-D0300': 'JOINT',
    'T-D04FF': 'TSPINE',
    'T-D0662': 'PCA',
    'T-D1000': 'ENDOVESICAL',
    'T-D1100': 'SVC',
    'T-D1160': 'AXILLA',
    'T-D1200': 'TESTIS',
    'T-D1206': 'CEPHALICV',
    'T-D1213': 'POPLITEALV',
    'T-D1400': 'FOOT',
    'T-D1460': 'TIBIAFIBULA',
    'T-D14AE': 'RATRIUM',
    'T-D1600': 'CERVIX',
    'T-D1620': 'RHYPOCHONDRIAC',
    'T-D2100': 'INTJUGULARV',
    'T-D2220': 'THORACICAORTA',
    'T-D2300': 'AXILLARYA',
    'T-D2310': 'POPLITEALA',
    'T-D2340': 'PATELLA',
    'T-D2342': 'CEREBRALA',
    'T-D2600': 'PANCREAS',
    'T-D2600': 'COMILIACV',
    'T-D2700': 'RPULMONARYA',
    'T-D3136': 'THUMB',
    'T-D3300': 'THYROID',
    'T-D4110': 'INTILIACA',
    'T-D4120': 'URETER',
    'T-D4130': 'AXILLARYV',
    'T-D4140': 'INFVENACAVA',
    'T-D4200': 'SUBCLAVIANA',
    'T-D4210': 'RLUMBAR',
    'T-D4211': 'RADIUS',
    'T-D4212': 'EPIDIDYMIS',
    'T-D4230': 'NECKCHESTABDPELV',
    'T-D4240': 'ARTERY',
    'T-D4240': 'CFA',
    'T-D4434': 'ANKLE',
    'T-D4900': 'LUQ',
    'T-D6407': 'ENDOVENOUS',
    'T-D7000': 'SUBMANDIBULAR',
    'T-D7010': 'ENDOURETERIC',
    'T-D7020': 'ENDORENAL',
    'T-D8104': 'ILIACA',
    'T-D8200': 'ASCENDINGCOLON',
    'T-D8500': 'NECK',
    'T-D8700': 'GLUTEAL',
    'T-D8800': 'LSUPPULMONARYV',
    'T-D8810': 'PENILEA',
    'T-D9100': 'RHEPATICV',
    'T-D9200': 'SESAMOID',
    'T-D930A': 'BLADDERURETHRA',
    'T-D9310': 'EYELID',
    'T-D9400': 'SIGMOID',
    'T-D9440': 'ELBOW',
    'T-D9700': 'ULNARA',
    'T-D9800': 'NASOPHARYNX',
    'T-DD006': 'ORBIT',
    'T-DD123': 'POSTIBIALA',
    'T-F1100': 'COMMONBILEDUCT',
    'T-F1320': 'RENALA',
    'T-F1810': 'CHESTABDOMEN',
}
class    DisplayableAnatomicConcept:
    def __init__(self, conceptUniqueIdentifier: str,
                 conceptIdentifier: str,
                 pairedStructure: bool,
                 codingSchemeDesignator: str,
                 legacyCodingSchemeDesignator: str,
                 codingSchemeVersion: str,
                 codeValue: str, codeMeaning: str,
                 codeStringEquivalent: str,
                 synonynms: list = [],
                 shortcutMenuEntry: list = [],
                 fullyQualifiedMenuEntry: list = []
                 ):
        self.ConceptUniqueIdentifier = conceptUniqueIdentifier
        self.ConceptIdentifier = conceptIdentifier
        self.PairedStructure = pairedStructure
        self.CodingSchemeDesignator = codingSchemeDesignator
        self.LegacyCodingSchemeDesignator = legacyCodingSchemeDesignator
        self.CodingSchemeVersion = codingSchemeVersion
        self.CodeValue = codeValue
        self.CodeMeaning = codeMeaning
        self.CodeStringEquivalent = codeStringEquivalent
        self.Synonynms = [] if synonynms is None else synonynms
        self.ShortcutMenuEntry = shortcutMenuEntry
        self.FullyQualifiedMenuEntry = fullyQualifiedMenuEntry

    def __str__(self):
        line = '{} = {}'
        out = ''
        out += line.format(
            "ConceptUniqueIdentifier", self.ConceptUniqueIdentifier) + "\n"
        out += line.format(
            "ConceptIdentifier", self.ConceptIdentifier) + "\n"
        out += line.format(
            "PairedStructure", self.PairedStructure) + "\n"
        out += line.format(
            "CodingSchemeDesignator", self.CodingSchemeDesignator) + "\n"
        out += line.format(
            "LegacyCodingSchemeDesignator", self.LegacyCodingSchemeDesignator) + "\n"
        out += line.format(
            "CodingSchemeVersion", self.CodingSchemeVersion) + "\n"
        out += line.format(
            "CodeValue", self.CodeValue) + "\n"
        out += line.format(
            "CodeMeaning", self.CodeMeaning) + "\n"
        out += line.format(
            "CodeStringEquivalent", self.CodeStringEquivalent) + "\n"
        out += line.format(
            "Synonynms", self.Synonynms) + "\n"
        out += line.format(
            "ShortcutMenuEntry", self.ShortcutMenuEntry) + "\n"
        out += line.format(
            "FullyQualifiedMenuEntry", self.FullyQualifiedMenuEntry) + "\n"
        return out

badLateralityOrViewOrAnatomyPhraseTriggers = [
    "History","Hx of"
    ]
badAnatomyWords = [
    "research", # contains "ear""and", # expedient way to remove conjunction
    "head first", # sometimes occurs in protocols"feet first",
    "entra di piedi","axials", # don't want LS to be confused as lumbar spine
    "sagittals","coronals",
    "locator", # else TOR matches chest"tracker"
    ]
anatomicConceptEntries = [
    # combined entries ...
    DisplayableAnatomicConcept(
        "C1508499","416949008", False,#unpaired
        "SRT", "SNM3", None, "R-FAB57", "Abdomen and Pelvis", "ABDOMENPELVIS",
        [
            "Abdomen Pelvis", # without conjunctions"Abdo Pelvis", # various abbreviations
            "Abd Pelvis","Abd Pelv",
            "Abd Pel","AbdoPelv",
            "brzuch miednica"#PL
        ],
        ["Abdomen and Pelvis"], ["Abdomen and Pelvis"]),
    DisplayableAnatomicConcept(
        "C1442171","416550000", False,#unpaired
        "SRT", "SNM3", None, "R-FAB55", "Chest and Abdomen", "CHESTABDOMEN",
        [
            "Chest Abdomen", # without conjunctions"Chest Abdo", # various abbreviations
            "Chest Abd","Thorax Abdomen",
            "Thorax Abdo","Thorax Abd",
            "Chest Liver", # not ideal match, but sometimes seem in protocols"Thorax Liver",
            "torace addome","Klatka brzuch"#PL
        ],
        ["Chest and Abdomen"], ["Chest and Abdomen"]),
    DisplayableAnatomicConcept(
        "C1562547","416775004", False,#unpaired
        "SRT", "SNM3", None, "R-FAB56", "Chest, Abdomen and Pelvis", "CHESTABDPELVIS",
        [
            "Chest Abdomen Pelvis", # without conjunctions"Chest Abdo Pelvis", # various abbreviations
            "Chest Abdo Pelv","Chest Abdo Pel",
            "Chest Abd Pelvis","Chest Abd Pelv",
            "Chest Abd Pel","Chest AbdoPelv",
            "Chest Abdomen Pelv","Chest Abdomen Pel",
            "Thorax Abdomen Pelvis","Thorax Abdo Pelvis",
            "Thorax Abdo Pelv","Thorax Abdo Pel",
            "Thorax Abd Pelvis","Thorax Abd Pelv",
            "Thorax Abd Pel","Thorax AbdoPelv",
            "Thorax Abdomen Pelv","Thorax Abdomen Pel",
            "Thoraco Abdomino Pelvien","Torax Abdomen Pelvis",
            "Th Abd Pel","C A P",
            "CAP","T A P",
            "TAP","Klatka brzuch miednica",#PL
            ""],
        ["Chest, Abdomen and Pelvis"], ["Chest, Abdomen and Pelvis"]),
    DisplayableAnatomicConcept(
        "C0460004","774007", False,#unpaired
        "SRT", "SNM3", None, "T-D1000", "Head and Neck", "HEADNECK",
        ["Head Neck"], # without conjunctions
        ["Head and Neck"], ["Head and Neck"]),
    DisplayableAnatomicConcept(
        "C1562459","417437006", False,#unpaired
        "SRT", "SNM3", None, "R-FAB52", "Neck and Chest", "NECKCHEST",
        [
            "Neck Chest", # without conjunctions"Neck Thorax",
            "Collo Tor"
        ],
        ["Neck and Chest"], ["Neck and Chest"]),
    DisplayableAnatomicConcept(
        "C1562378","416152001", False,#unpaired
        "SRT", "SNM3", None, "R-FAB53", "Neck, Chest and Abdomen", "NECKCHESTABDOMEN",
        [
            "Neck Chest Abdomen", # without conjunctions"Neck Chest Abdo", # various abbreviations
            "Neck Chest Abd","Neck Thorax Abdomen",
            "Neck Thorax Abdo","Neck Thorax Abd",
            "Collo Tor Addo"],
        ["Neck, Chest and Abdomen"], ["Neck, Chest and Abdomen"]),
    DisplayableAnatomicConcept(
        "C1562776","416319003", False,#unpaired
        "SRT", "SNM3", None, "R-FAB54", "Neck, Chest, Abdomen and Pelvis", "NECKCHESTABDPELV",
        [
            "Neck Chest Abdomen Pelvis", # without conjunctions"Neck Chest Abdo Pelvis", # various abbreviations
            "Neck Chest Abd Pelvis","Neck Chest Abdo Pelv",
            "Neck Chest Abdo Pel","Neck Chest Abd Pelv",
            "Neck Chest Abd Pel","Neck Thorax Abdomen Pelvis",
            "Neck Thorax Abdo Pelvis","Neck Thorax Abd Pelvis",
            "Neck Thorax Abdo Pelv","Neck Thorax Abdo Pel",
            "Neck Thorax Abd Pelv","Neck Thorax Abd Pel"
        ],
        ["Neck, Chest, Abdomen and Pelvis"],
        ["Neck, Chest, Abdomen and Pelvis"]),
    DisplayableAnatomicConcept(
        "C1508520","LP33902-5", False,#unpaired
        "LN", None, None, "LP33902-5", "Aortic Arch and Carotid Artery", None,
        [
            "Aortic Arch Carotid Artery", # without conjunctions"Aortic Arch and Carotid Arteries",
            "Aortic Arch Carotid Arteries"
        ],
        ["Aortic Arch and Carotid Artery"], ["Aortic Arch and Carotid Artery"]),
    # single part entries ...
    DisplayableAnatomicConcept(
        "C0000726","113345001", False,#unpaired
        "SRT", "SNM3", None, "T-D4000", "Abdomen", "ABDOMEN",
        [
            "Abdominal","BØICHO",#CZ
            "bruco",#CZ"Buik",#NL
            "Vatsa",#FI"Ventre",#FR
            "Addome",#IT"Abdome",#PT
            "はら",#JP"心窩部",#JP
            "胴",#JP"腹",#JP
            "腹部",#JP"ЖИВОТ",#RU
            "Buk",#NL"Pilvo",#LT
            "Addo","brzuch"#PL
        ],
        ["Abdomen"], ["Abdomen"]),
    DisplayableAnatomicConcept(
        "C0001625","23451007", True ,#paired
        "SRT", "SNM3", None, "T-B3000", "Adrenal gland", "ADRENAL",["Adrenal"],
        ["Adrenal gland"], ["Adrenal gland"]),
    DisplayableAnatomicConcept(
        "C0042425","67109009", False,#unpaired
        "SRT", "SNM3", None, "T-64700", "Ampulla of Vater", None, None,
        ["Ampulla of Vater"], ["Ampulla of Vater"]
        ),
    DisplayableAnatomicConcept("C0003087","70258002", True ,#paired
        "SRT", "SNM3", None, "T-15750", "Ankle joint", "ANKLE",
        [
            "Ankle","Tobillo",#ES
            "Knöchel",#DE"Enkel",#NL
            "Cheville",#FR"Tornozelo",#PT
            "αστράγαλος",#GR"足首",#JP
            "발목",#KR"лодыжка"#RU
        ],
        ["Ankle joint"], ["Ankle joint"]),
    DisplayableAnatomicConcept(
        "C0003483","15825003", False,#unpaired
        "SRT", "SNM3", None, "T-42000", "Aorta", "AORTA", None,
        ["Aorta"], ["Aorta"]),
    DisplayableAnatomicConcept("C0545736","LP33868-8", False,#unpaired
        "LN", None, None, "LP33868-8", "Aorta and femoral artery", None, None,
        ["Aorta and femoral artery"], ["Aorta and femoral artery"]
        ),
    DisplayableAnatomicConcept("C0003489","57034009", False,#unpaired
        "SRT", "SNM3", None, "T-42300", "Aortic Arch", None, None,
        ["Aortic Arch"], ["Aortic Arch"]),
    DisplayableAnatomicConcept("C1508529","LP33903-3", False,#unpaired
        "LN", None, None, "LP33903-3",
        "Aortic arch and subclavian artery", None, None,
        ["Aortic arch and subclavian artery"],
        ["Aortic arch and subclavian artery"]),
    DisplayableAnatomicConcept("C0446516","40983000", True ,#paired
        "SRT", "SNM3", None, "T-D8200", "Arm", "ARM",
        None, ["Arm"], ["Arm"]
        ),# D1-50666 "Arteriovenous fistula" is in the SNOMED US extension
    DisplayableAnatomicConcept(
        "C0003855","439470001", False,#unpaired
        "SRT", "SNM3", None, "D1-50666", "Arteriovenous fistula",
        None, None, ["Arteriovenous fistula"], ["Arteriovenous fistula"]
        ),
    DisplayableAnatomicConcept("C0004454","34797008", True ,#paired
        "SRT", "SNM3", None, "T-D8100", "Axilla", "AXILLA", None,
        ["Axilla"], ["Axilla"]),
    DisplayableAnatomicConcept("C1995000","77568009", False,#unpaired
        "SRT", "SNM3", None, "T-D2100", "Back", "BACK", None,
        ["Back"], ["Back"]),
    DisplayableAnatomicConcept("C0005400","28273000", False,#unpaired
        "SRT", "SNM3", None, "T-60610", "Bile duct", None, None,
        ["Bile duct"], ["Bile duct"]),
    DisplayableAnatomicConcept("C0005682","89837001", False,#unpaired
        "SRT", "SNM3", None, "T-74000", "Bladder", "BLADDER", None,
        ["Bladder"], ["Bladder"]),
    DisplayableAnatomicConcept("C0006087","17137000", True ,#paired
        "SRT", "SNM3", None, "T-47160", "Brachial artery", None, None,
        ["Brachial artery"], ["Brachial artery"]),
    DisplayableAnatomicConcept("C0006104","12738006", False,#unpaired
        "SRT", "SNM3", None, "T-A0100", "Brain", "BRAIN", None,
        ["Brain"], ["Brain"]),
    DisplayableAnatomicConcept("C0006141","76752008", True ,#paired
        "SRT", "SNM3", None, "T-04000", "Breast", "BREAST", None,
        ["Breast"], ["Breast"]),
    DisplayableAnatomicConcept("C0006255","955009", True ,#paired
        "SRT", "SNM3", None, "T-26000", "Bronchus", "BRONCHUS", None,
        ["Bronchus"], ["Bronchus"]),
    DisplayableAnatomicConcept("C0006497","46862004", True ,#paired
        "SRT", "SNM3", None, "T-D2600", "Buttock", "BUTTOCK", None,
        ["Buttock"], ["Buttock"]),
    DisplayableAnatomicConcept("C0006655","80144004", True ,#paired
        "SRT", "SNM3", None, "T-12770", "Calcaneus", "CALCANEUS", None,
        ["Calcaneus"], ["Calcaneus"]),
    DisplayableAnatomicConcept("C0230445","53840002", True ,#paired
        "SRT", "SNM3", None, "T-D9440", "Calf of leg", "CALF",["Calf"],
        ["Calf of leg"], ["Calf of leg"]),
    DisplayableAnatomicConcept(
        "C0007272","69105007", True ,#paired
        "SRT", "SNM3", None, "T-45010", "Carotid Artery", "CAROTID",["Carotid"],
        ["Carotid Artery"], ["Carotid Artery"]),
    DisplayableAnatomicConcept(
        "C1268981","180924008", False,#unpaired
        "SRT", "SNM3", None, "T-A600A", "Cerebellum", "CEREBELLUM", None,
        ["Cerebellum"], ["Cerebellum"]),
    DisplayableAnatomicConcept("C0728985","122494005", False,#unpaired
        "SRT", "SNM3", None, "T-11501", "Cervical spine", "CSPINE",
        [
            "CS","CWK",#NL
            "CWZ",#NL"HWS",#DE
            "H Rygg",#SE"Cspine",
            "C spine","Spine Cervical",
            "Cervical","Cervic",#abbrev
            "Kaelalülid",#EE"KRÈNÍ OBRATLE",#CZ
            "Halswervels",#NL"Vertebrae cervicalis",#NL
            "Wervel hals",#NL"Kaulanikamat",#FI
            "Rachis cervical",#FR"Vertèbre cervicale",#FR
            "Vertèbres cervicales",#FR"COLONNE CERVICALE",#FR
            "CERVICALE",#FR"Halswirbel",#DE
            "Vertebrae cervicales",#DE"Vertebre cervicali",#IT
            "頚椎",#JP"頸椎",#JP
            "Vértebras Cervicais",#PT"ШЕЙНЫЕ ПОЗВОНКИ",#RU
            "columna cervical",#ES"columna cerv",#ES abbrev
            "columna espinal cervical",#ES"columna vertebral cervical",#ES
            "vértebras cervicales",#ES"Cervikalkotor",#SE
            "Halskotor",#SE"Halsrygg",#SE
            "Cervicale wervelzuil",#BE"C chrbtica"#SK
        ],
        ["Cervical spine"], ["Cervical spine"]),
    DisplayableAnatomicConcept(
        "C0729373","297171002", False,#unpaired
        "SRT", "SRT", None, "T-D00F7", "Cervico-thoracic spine", "CTSPINE",
        [
            "CTSPINE","Cervico-thoracic",
        "Cervicothoracic"],
        ["Cervico-thoracic spine"], ["Cervico-thoracic spine"]),
    DisplayableAnatomicConcept(
        "C0007874","71252005", False,#unpaired
        "SRT", "SNM3", None, "T-83200", "Cervix", "CERVIX", None, ["Cervix"], ["Cervix"]),
    DisplayableAnatomicConcept("C0007966","60819002", True ,#paired
        "SRT", "SNM3", None, "T-D1206", "Cheek", "CHEEK", None, ["Cheek"], ["Cheek"]),
    DisplayableAnatomicConcept("C0817096","51185008", False,#unpaired
        "SRT", "SNM3", None, "T-D3000", "Chest", "CHEST",
        [
            "Thorax","Rindkere",#EE
            "HRUDNÍK",#CZ"hrudník",#CZ
            "Borst",#NL"Rintakehä",#FI
            "Poitrine",#FR"Potter",#FR ?? - seen in examples
            "Torse",#FR"Brustkorb",#DE
            "Torace",#IT"Peito",#PT
            "ГРУДНАЯ КЛЕТКА",#RU"ГРУДЬ",#RU
            "pecho",#ES"torácico",#ES
            "Bröstkorg",#SE"Torax",#SE,PT,ES
            "hrudnнk",#SK"hrudn",#SK abbrev
            "mellkas",#HU"Krūtinės ląsta",#LT
            "Tor","Klatka"#PL
        ],
        ["Chest"], ["Chest"]),
    DisplayableAnatomicConcept(
        "C1284333","362047009", False,#unpaired
        "SRT", "SNM3", None, "T-45526", "Circle of Willis", "CIRCLEOFWILLIS",
        None, ["Circle of Willis"], ["Circle of Willis"]),
    DisplayableAnatomicConcept("C0008913","51299004", True ,#paired
        "SRT", "SNM3", None, "T-12310", "Clavicle", "CLAVICLE", None,
        ["Clavicle"], ["Clavicle"]),
    DisplayableAnatomicConcept("C0009194","64688005", False,#unpaired
        "SRT", "SNM3", None, "T-11BF0", "Coccyx", "COCCYX", None,
        ["Coccyx"], ["Coccyx"]),
    DisplayableAnatomicConcept("C0009368","71854001", False,#unpaired
        "SRT", "SNM3", None, "T-59300", "Colon", "COLON", None,
        ["Colon"], ["Colon"]),
    DisplayableAnatomicConcept("C1268346","110797007", False,#unpaired
        "SRT", "SNM3", None, "T-DD080", "Colon and rectum", None, None,
        ["Colon and rectum"], ["Colon and rectum"]),
    DisplayableAnatomicConcept("C0010031","28726007", True ,#paired
        "SRT", "SNM3", None, "T-AA200", "Cornea", "CORNEA", None,
        ["Cornea"], ["Cornea"]),
    DisplayableAnatomicConcept("C0205042","41801008", False,#unpaired
        "SRT", "SNM3", None, "T-43000", "Coronary artery", "CORONARYARTERY",
        ["Coronary"], ["Coronary artery"], ["Coronary artery"]),
    DisplayableAnatomicConcept(
        "C0011980","5798000", False,#unpaired
        "SRT", "SNM3", None, "T-D3400", "Diaphragm", None, None,
        ["Diaphragm"], ["Diaphragm"]),
    DisplayableAnatomicConcept("C0013303","38848004", False,#unpaired
        "SRT", "SNM3", None, "T-58200", "Duodenum", "DUODENUM", None,
        ["Duodenum"], ["Duodenum"]),
    DisplayableAnatomicConcept("C0521421","1910005", True ,#paired
        "SRT", "SNM3", None, "T-AB000", "Ear", "EAR", None, ["Ear"], ["Ear"]),
    DisplayableAnatomicConcept("C1305417","76248009", True ,#paired
        "SRT", "SNM3", None, "T-D8300", "Elbow", "ELBOW",
        [
            "Ellbogen",#DE"Coude",#FR
        "Küünar",#EE"Armbåge",#SE
        "Codo",#ES"Cotovelo"#PT
        ],
        ["Elbow"], ["Elbow"]),
    DisplayableAnatomicConcept(
        "C0229960","38266002", False,#unpaired
        "SRT", "SNM3", None, "T-D0010", "Entire body", "WHOLEBODY",
        [
            "Entire body","Whole body",
        "Mid body" # not quite right, but nothing better 
        ],
        ["Entire body"], ["Entire body"]),
    DisplayableAnatomicConcept(
        "C0014876","32849002", False,#unpaired
        "SRT", "SNM3", None, "T-56000", "Esophagus", "ESOPHAGUS", None,
        ["Esophagus"], ["Esophagus"]),
    DisplayableAnatomicConcept("C0015385","66019005", True ,#paired
        "SRT", "SNM3", None, "T-D0300", "Extremity", "EXTREMITY",
        [
            "Extremety",#Agfa CR spelling mistake"Extremidad"#ES
        ],
        ["Extremity"], ["Extremity"]),
    DisplayableAnatomicConcept(
        "C0015392","81745001", True ,#paired
        "SRT", "SNM3", None, "T-AA000", "Eye", "EYE", None, ["Eye"], ["Eye"]),
    DisplayableAnatomicConcept("C0015426","80243003", True ,#paired
        "SRT", "SNM3", None, "T-AA810", "Eyelid", "EYELID", None, ["Eyelid"],
        ["Eyelid"]
        ),# not face ... gets confused with frontal view (FR,NL) ...    
    DisplayableAnatomicConcept(
        "C0015450","89545001", True ,#paired
        "SRT", "SNM3", None, "T-D1200", "Face", "FACE", None,
        ["Face"], ["Face"]),
    DisplayableAnatomicConcept("C0015801","7657000", True ,#paired
        "SRT", "SNM3", None, "T-47400", "Femoral artery", None, None,
        ["Femoral artery"], ["Femoral artery"]),
    DisplayableAnatomicConcept("C0015811","71341001", True ,#paired
        "SRT", "SNM3", None, "T-12710", "Femur", "FEMUR", None,
        ["Femur"], ["Femur"]),
    DisplayableAnatomicConcept("C0524584","55460000", True ,#paired
        "SRT", "SNM3", None, "T-F5201", "Fetus", None, None,
        ["Fetus"], ["Fetus"]),
    DisplayableAnatomicConcept("C0016129","7569003", True ,#paired
        "SRT", "SNM3", None, "T-D8800", "Finger", "FINGER", None,
        ["Finger"], ["Finger"]),
    DisplayableAnatomicConcept("C0016504","56459004", True ,#paired
        "SRT", "SNM3", None, "T-D9700", "Foot", "FOOT",
        [
            "Pied",#FR"Pie",#ES
            "Voet",#NL"Fuß",#DE
            "πόδι",#GR"Piede",#IT
            #"pé"*#*PT*#*,*#* Cannot use this one ... matches PET and calls all PET scans as foot ! 
            "нога"#RU
        ],
        ["Foot"], ["Foot"]),
    DisplayableAnatomicConcept(
        "C0223680","55797009", True ,#paired
        "SRT", "SNM3", None, "T-12402", "Forearm bone", "FOREARM",
        [
            "Forearm","U ARM",#DE
            "Unterarm",#DE"Avambraccio",#IT
            "PØEDLOKTÍ",#CZ"Onderarm",#NL
            "Kyynärvarsi",#FI"Avant-bras",#FR
            "まえうで",#JP"前腕",#JP
            "Antebraço",#PT"ПРЕДПЛЕЧЬЕ",#RU
            "antebrazo",#ES"Underarm",#SE
            "predlaktie"#SK
        ],
        ["Forearm"], ["Forearm"]),
    DisplayableAnatomicConcept(
        "C0016976","28231008", False,#unpaired
        "SRT", "SNM3", None, "T-63000", "Gallbladder", "GALLBLADDER", None,
        ["Gallbladder"], ["Gallbladder"]),
    DisplayableAnatomicConcept("C0018563","85562004", True ,#paired
        "SRT", "SNM3", None, "T-D8700", "Hand", "HAND", None,
        ["Hand"], ["Hand"]),
    DisplayableAnatomicConcept("C0018670","69536005", False,#unpaired
        "SRT", "SNM3", None, "T-D1100", "Head", "HEAD",
        [
            "Kopf",#DE"Schaedel",#DE
            "Schædel",#DE"Sch?del",#DE encoded incorrectly
            "Tete"#FR
        ],
        ["Head"], ["Head"]),
    DisplayableAnatomicConcept(
        "C0460004","774007", False,#unpaired
        "SRT", "SNM3", None, "T-D1000", "Head and Neck",
        "HEADNECK", ["Head Neck"],
        ["Head and Neck"], ["Head and Neck"]),
    DisplayableAnatomicConcept(
        "C0018787","80891009", False,#unpaired
        "SRT", "SNM3", None, "T-32000", "Heart", "HEART", None,
        ["Heart"], ["Heart"]),
    DisplayableAnatomicConcept("C0019552","24136001", True ,#paired
        "SRT", "SNM3", None, "T-15710", "Hip joint", "HIP",
        [
            "Hip","Heup",#NL
            "Hanche",#FR"Hüfte",#DE
            "Puus",#EE"HÖFT",#SE
            "Cadera",#ES"ισχίο",#GR
            "anca",#IT"ヒップ",#JP
            "엉덩이",#KR"вальма"#RU
        ],
        ["Hip"], ["Hip"]),
    DisplayableAnatomicConcept(
        "C0020164","85050009", True ,#paired
        "SRT", "SNM3", None, "T-12410", "Humerus", "HUMERUS",
        [
            "UP_EXM",#Fuji CR BPE"O ARM",#DE,SE
            "Oberarm",#DE"Õlavars",#EE
            "Bovenarm",#NL"húmero"#ES
        ],
        ["Humerus"], ["Humerus"]),
    DisplayableAnatomicConcept(
        "C0020885","34516001", False,#unpaired
        "SRT", "SNM3", None, "T-58600", "Ileum", "ILEUM", None, ["Ileum"],
        ["Ileum"]),
    DisplayableAnatomicConcept("C0576469","299716001", True ,#paired
        "SRT", "SNM3", None, "T-41068", "Iliac and femoral artery", None, None,
        ["Iliac and femoral artery"], ["Iliac and femoral artery"]),
    DisplayableAnatomicConcept("C0020889","22356005", True ,#paired
        "SRT", "SNM3", None, "T-12340", "Ilium", "ILIUM", None, ["Ilium"], ["Ilium"]),
    DisplayableAnatomicConcept("C0018246","26893007", True ,#paired
        "SRT", "SNM3", None, "T-D7000", "Inguinal region", None, None,
        ["Inguinal region"], ["Inguinal region"]),
    DisplayableAnatomicConcept("C1283773","361078006", True ,#paired
        "SRT", "SNM3", None, "T-AB959", "Internal Auditory Canal", "IAC",
        ["IAC"],
        ["Internal Auditory Canal"], ["Internal Auditory Canal"]),
    DisplayableAnatomicConcept(
        "C0226364","90024005", True ,#paired
        "SRT", "SNM3", None, "T-46740", "Internal iliac artery", None, None,
        ["Internal iliac artery"], ["Internal iliac artery"]),
    DisplayableAnatomicConcept("C0022359","661005", True ,#paired
        "SRT", "SNM3", None, "T-D1213", "Jaw region", "JAW", None,
        ["Jaw region"], ["Jaw region"]),
    DisplayableAnatomicConcept("C0022378","21306003", False,#unpaired
        "SRT", "SNM3", None, "T-58400", "Jejunum", "JEJUNUM", None,
        ["Jejunum"], ["Jejunum"]),
    DisplayableAnatomicConcept("C0022646","64033007", True ,#paired
        "SRT", "SNM3", None, "T-71000", "Kidney", "KIDNEY", None,
        ["Kidney"], ["Kidney"]),
    DisplayableAnatomicConcept("C1456798","72696002", True ,#paired
        "SRT", "SNM3", None, "T-D9200", "Knee", "KNEE",
        [
            "Knie",#DE,NL"Genou",#FR
            "Põlv",#EE"Pölv",#EE ?wrong accent
            "Knä",#SE"Rodilla"#ES
        ],
        ["Knee"], ["Knee"]),
    DisplayableAnatomicConcept(
        "C0023078","4596009", False,#unpaired
        "SRT", "SNM3", None, "T-24100", "Larynx", "LARYNX",
        [
            "Laringe",#ES,IT"Kehlkopf",#DE
            "Strottenhoofd"#NL#FR is same as english
        ],
        ["Larynx"], ["Larynx"]),
    DisplayableAnatomicConcept(
        "C1140621","30021000", True ,#paired
        "SRT", "SNM3", None, "T-D9400", "Leg", "LEG",
        [
            "LOW_EXM",#Fuji CR BPE"LOWEXM",#Siemens CR BPE
            "TIB FIB ANKLE","Jambe"#FR
        ],
        ["Leg"], ["Leg"]),
    DisplayableAnatomicConcept(
        "C0023884","10200004", False,#unpaired
        "SRT", "SNM3", None, "T-62000", "Liver", "LIVER",
        [
            "foie",#FR"Kepenys"#LT
        ],
        ["Liver"], ["Liver"]),
    DisplayableAnatomicConcept(
        "C0024091","122496007", False,#unpaired
        "SRT", "SNM3", None, "T-11503", "Lumbar spine", "LSPINE",
        [
            "LS","LWK",#NL
        "LWZ",#NL"LWS",#DE
        "L Rygg",#SE"Lspine",
        "L spine","Spine Lumbar",
        "Lumbar","Rachis lombaire",#FR
        "COLONNE LOMBAIRE",#FR"Rach.Lomb",#FR abbrev
        "lombaire",#FR"Nimmelülid",#EE
        "Columna lumbar",#ES"LÄNDRYGG",#SE
        "L chrbtica",#SK"COL LOMBARE"
        ],
        ["Lumbar spine"], ["Lumbar spine"]),
    DisplayableAnatomicConcept(
        "C0223603","297173004", False,#unpaired
        "SRT", "SRT", None, "T-D00F9", "Lumbo-sacral spine", "LSSPINE",
        [
            "LSSPINE","Lumbosacral spine",
        "Lumbo-sacrale wervelzuil",#BE"columna vertebral lumbosacra",#ES
        "vértebras lumbosacras",#ES"Colonna Lombosacrale"
        ],
        ["Lumbo-sacral spine"], ["Lumbo-sacral spine"]),
    DisplayableAnatomicConcept(
        "C0024109","39607008", True ,#paired
        "SRT", "SNM3", None, "T-28000", "Lung", "LUNG",
        [
            "pluco",#PL"pluca"#PL
        ],
        ["Lung"], ["Lung"]),
    DisplayableAnatomicConcept(
        "C0024687","91609006", True ,#paired
        "SRT", "SNM3", None, "T-11180", "Mandible", "JAW", None,
        ["Mandible"], ["Mandible"]),
    DisplayableAnatomicConcept("C0024947","70925003", True ,#paired
        "SRT", "SNM3", None, "T-11170", "Maxilla", "MAXILLA", None,
        ["Maxilla"], ["Maxilla"]),
    DisplayableAnatomicConcept("C0178738","LP30124-9", True ,#paired
        "LN", None, None, "LP30124-9", "Maxilla and Mandible", None, None,
        ["Maxilla and Mandible"], ["Maxilla and Mandible"]),
    DisplayableAnatomicConcept("C0025066","72410000", False,#unpaired
        "SRT", "SNM3", None, "T-D3300", "Mediastinum", "MEDIASTINUM", None,
        ["Mediastinum"], ["Mediastinum"]),
    DisplayableAnatomicConcept("C1267547","21082005", False,#unpaired
        "SRT", "SNM3", None, "T-51000", "Mouth", "MOUTH", None, ["Mouth"],
        ["Mouth"]),
    DisplayableAnatomicConcept("C0027530","45048000", False,#unpaired
        "SRT", "SNM3", None, "T-D1600", "Neck", "NECK",
        [
            "Kael",#EE"Collo",#IT
            "Cuello",#ES"Hals",#DE
            "Nek",#NL"Nacke"#SE
        ],
        ["Neck"], ["Neck"]),
    DisplayableAnatomicConcept(
        "C0028429","45206002", False,#unpaired
        "SRT", "SNM3", None, "T-21000", "Nose", "NOSE", None,
        ["Nose"], ["Nose"]),
    DisplayableAnatomicConcept("C0015392","371398005", True ,#paired
        "SRT", "SNM3", None, "T-D0801", "Orbital region", "ORBIT",
        ["Orbit"], ["Orbital region"], ["Orbital region"]),
    DisplayableAnatomicConcept(
        "C0029939","15497006", True ,#paired
        "SRT", "SNM3", None, "T-87000", "Ovary", "OVARY", None,
        ["Ovary"], ["Ovary"]),
    DisplayableAnatomicConcept("C0030274","15776009", False,#unpaired
        "SRT", "SNM3", None, "T-65000", "Pancreas", "PANCREAS", None,
        ["Pancreas"], ["Pancreas"]),
    DisplayableAnatomicConcept("C0030288","69930009", False,#unpaired
        "SRT", "SNM3", None, "T-65010", "Pancreatic duct", None, None,
        ["Pancreatic duct"], ["Pancreatic duct"]),
    DisplayableAnatomicConcept("C1267614","110621006", False,#unpaired
        "SRT", "SNM3", None, "T-65600",
        "Pancreatic duct and bile duct systems", None,
        [
            "Pancreatic duct and bile duct systems","Pancreatic duct and bile ducts",
            "Pancreatic duct and bile duct","Pancreatic and bile ducts"
        ],
        ["Pancreatic duct and bile duct systems"],
    ["Pancreatic duct and bile duct systems"]),
    DisplayableAnatomicConcept(
        "C0030580","45289007", True ,#paired
        "SRT", "SNM3", None, "T-61100", "Parotid gland", "PAROTID",["Parotid"],
        ["Parotid gland"], ["Parotid gland"]),
    DisplayableAnatomicConcept(
        "C0030647","64234005", True ,#paired
        "SRT", "SNM3", None, "T-12730", "Patella", "PATELLA", None, ["Patella"], ["Patella"]),
    DisplayableAnatomicConcept("C0030797","12921003", False,#unpaired
        "SRT", "SNM3", None, "T-D6000", "Pelvis", "PELVIS",
        [
            "PV",#abbreviations"Pelv",
            "Pel","Bekken",#NL
            "Becken",#DE"Bassin",#FR
            "Vaagen",#EE"BÄCKEN",#SE
            "λεκάνη",#GR"Bacino",#IT
            "骨盤",#JP"골반",#KR
            "miednica"#PL
        ],
        ["Pelvis"], ["Pelvis"]),
    DisplayableAnatomicConcept(
        "C0030851","18911002", False,#unpaired
        "SRT", "SNM3", None, "T-91000", "Penis", "PENIS", None, ["Penis"],
        ["Penis"]),
    DisplayableAnatomicConcept("C0225972","25489000", False,#unpaired
        "SRT", "SNM3", None, "T-39050", "Pericardial cavity", None, None,
        ["Pericardial cavity"], ["Pericardial cavity"]),
    DisplayableAnatomicConcept("C1278903","181211006", False,#unpaired
        "SRT", "SNM3", None, "T-55002", "Pharynx", "PHARYNX", None,
        ["Pharynx"], ["Pharynx"]),
    DisplayableAnatomicConcept("C0033572","41216001", False,#unpaired
        "SRT", "SNM3", None, "T-92000", "Prostate", "PROSTATE", None,
        ["Prostate"], ["Prostate"]),
    DisplayableAnatomicConcept("C0034896","34402009", False,#unpaired
        "SRT", "SNM3", None, "T-59600", "Rectum", "RECTUM", None,
        ["Rectum"], ["Rectum"]),
    DisplayableAnatomicConcept("C0035561","113197003", True ,#paired
        "SRT", "SNM3", None, "T-11300", "Rib", "RIB",
        [
            "Gril costal",#FR"Gril cost"#FR abbrev
        ],
        ["Rib"], ["Rib"]),
    DisplayableAnatomicConcept(
        "C0036037","54735007", False,#unpaired
        "SRT", "SNM3", None, "T-11AD0", "Sacrum", "SSPINE",["SSPINE"],
        ["Sacrum"], ["Sacrum"]),
    DisplayableAnatomicConcept(
        "C0036270","41695006", False,#unpaired
        "SRT", "SNM3", None, "T-D1160", "Scalp", "SCALP", None,
        ["Scalp"], ["Scalp"]),
    DisplayableAnatomicConcept("C0036277","79601000", True ,#paired
        "SRT", "SNM3", None, "T-12280", "Scapula", "SCAPULA", None,
        ["Scapula"], ["Scapula"]),
    DisplayableAnatomicConcept("C0036410","18619003", True ,#paired
        "SRT", "SNM3", None, "T-AA110", "Sclera", "SCLERA", None,
        ["Sclera"], ["Sclera"]),
    DisplayableAnatomicConcept("C0036471","20233005", True ,#paired
        "SRT", "SNM3", None, "T-98000", "Scrotum", "SCROTUM", None,
        ["Scrotum"], ["Scrotum"]),
    DisplayableAnatomicConcept("C0037004","16982005", True ,#paired
        "SRT", "SNM3", None, "T-D2220", "Shoulder", "SHOULDER",
        [
            "Schouder",#NL"Schulter",#DE
            "Epaule",#FR"épaule",#FR
            "õlg",#EE"Ölg",#EE ?wrong accent
            "Hombro",#ES"Ombro",#PT
            "Rameno",#SK"Rippe"#DE
        ],
        ["Shoulder"], ["Shoulder"]),
    DisplayableAnatomicConcept(
        "C0021852","30315005", False,#unpaired
        "SRT", "SNM3", None, "T-58000", "Small intestine", None, None,
        ["Small intestine"], ["Small intestine"]),
    DisplayableAnatomicConcept(
        "C0037303","89546000", False,#unpaired
        "SRT", "SNM3", None, "T-11100", "Skull", "SKULL",
        [
            "Kolju",#EE"LEBKA",#CZ
            "Schedel",#NL"Kallo",#FI
            "Crâne",#FR"Cranium",#DE
            "Schädel",#DE"Cranio",#IT
            "Calota Craniana",#PT"Crânio",#PT
            "ЧЕРЕП",#RU"Calota Craneal",#ES
            "Cráneo",#ES"Kalvarium",#SE
            "Kranium",#SE"Skalle",#SE
            "Lebka"#SK
        ],
        ["Skull"], ["Skull"]),
    DisplayableAnatomicConcept(
        "C0037949","280717001", False,#unpaired
        "SRT", "SNM3", None, "T-D0146", "Spine", "SPINE",
        [
            "Rachis",#FR"Rygg",#SE
            "chrbtica"#SK
        ],
        ["Spine"], ["Spine"]),
    DisplayableAnatomicConcept(
        "C0028872","51807001", False,#unpaired
        "SRT", "SNM3", None, "T-64710", "Sphincter of Oddi", None, None,
        ["Sphincter of Oddi"], ["Sphincter of Oddi"]),
    DisplayableAnatomicConcept("C0278443","56101001", False,#unpaired
        "SRT", "SNM3", None, "T-65016", "Sphincter pancreaticus", None, None,
        ["Sphincter pancreaticus"], ["Sphincter pancreaticus"]),
    DisplayableAnatomicConcept("C0037993","78961009", False,#unpaired
        "SRT", "SNM3", None, "T-C3000", "Spleen", "SPLEEN", None,
        ["Spleen"], ["Spleen"]),
    DisplayableAnatomicConcept("C0038293","56873002", False,#unpaired
        "SRT", "SNM3", None, "T-11210", "Sternum", "STERNUM", None,
        ["Sternum"], ["Sternum"]),
    DisplayableAnatomicConcept("C0038351","69695003", False,#unpaired
        "SRT", "SNM3", None, "T-57000", "Stomach", "STOMACH", None,
        ["Stomach"], ["Stomach"]),
    DisplayableAnatomicConcept("C0038530","36765005", False,#unpaired
        "SRT", "SNM3", None, "T-46100", "Subclavian artery", None, None,
        ["Subclavian artery"], ["Subclavian artery"]),
    DisplayableAnatomicConcept("C0038556","54019009", True ,#paired
        "SRT", "SNM3", None, "T-61300", "Submandibular gland",
        "SUBMANDIBULAR",["Submandibular"],
        ["Submandibular gland"], ["Submandibular gland"]),
    DisplayableAnatomicConcept(
        "C0039493","53620006", True ,#paired
        "SRT", "SNM3", None, "T-15290", "Temporomandibular joint", "TMJ",
        [
            "Temporomandibular","TMJ"
        ],
        ["Temporomandibular joint"], ["Temporomandibular joint"]),
    DisplayableAnatomicConcept(
        "C0039597","40689003", True ,#paired
        "SRT", "SNM3", None, "T-94000", "Testis", "TESTIS", None,
        ["Testis"], ["Testis"]),
    DisplayableAnatomicConcept("C0039866","68367000", True ,#paired
        "SRT", "SNM3", None, "T-D9100", "Thigh", "THIGH",
        [
            "Oberschenkel",#DE"Bovenbeen",#NL
            "Reis"#EE
        ],
        ["Thigh"], ["Thigh"]),
    DisplayableAnatomicConcept(
        "C0581269","122495006", False,#unpaired
        "SRT", "SNM3", None, "T-11502", "Thoracic spine", "TSPINE",
        [
            "TSPINE","TS",
            "THWK",#NL"DWZ",#NL
            "BWS",#DE"B Rygg",#SE
            "T spine","Spine Thoracic",
            "Thoracic","Dorsal",
            "Dorsal spine","Spine Dorsal",
            "Rachis dorsal",#FR"COLONNE THORACIQUE",#FR
            "THORACIQUE",#FR"Rinnaosa",#EE??
            "Rinnalülid",#EE"Columna dorsal",#ES
            "Columna vertebral dorsal",#ES"Thoracale wervelzuil",#BE
            "BRÖSTRYGG",#SE"Th chrbtica"#SK
        ],
        ["Thoracic spine"], ["Thoracic spine"]),
    DisplayableAnatomicConcept(
        "C0729374","297172009", False,#unpaired
        "SRT", "SRT", None, "T-D00F8", "Thoraco-lumbar spine", "TLSPINE",
        [
            "TLSPINE","Thoraco-lumbar",
            "Thoracolumbar","Col.Dors.Lomb",#FR abbrev
            "THORACOLUMBALE"],
        ["Thoraco-lumbar spine"], ["Thoraco-lumbar spine"]),
    DisplayableAnatomicConcept(
        "C0040067","76505004", True ,#paired
        "SRT", "SNM3", None, "T-D8810", "Thumb", "THUMB", None,
        ["Thumb"], ["Thumb"]),
    DisplayableAnatomicConcept("C1306748","118507000", False,#unpaired
        "SRT", "SNM3", None, "T-C8001", "Thymus", "THYMUS", None,
        ["Thymus"], ["Thymus"]),
    DisplayableAnatomicConcept("C0040132","69748006", False,#unpaired
        "SRT", "SNM3", None, "T-B6000", "Thyroid", "THYROID", None,
        ["Thyroid"], ["Thyroid"]),
    DisplayableAnatomicConcept("C0040357","29707007", True ,#paired
        "SRT", "SNM3", None, "T-D9800", "Toe", "TOE", None,
        ["Toe"], ["Toe"]),
    DisplayableAnatomicConcept("C0040408","21974007", False,#unpaired
        "SRT", "SNM3", None, "T-53000", "Tongue", "TONGUE", None,
        ["Tongue"], ["Tongue"]),
    DisplayableAnatomicConcept("C0040578","44567001", False,#unpaired
        "SRT", "SNM3", None, "T-25000", "Trachea", "TRACHEA", None,
        ["Trachea"], ["Trachea"]),
    DisplayableAnatomicConcept("C0227690","65364008", True ,#paired
        "SRT", "SNM3", None, "T-73800", "Ureter", "URETER", None,
        ["Ureter"], ["Ureter"]),
    DisplayableAnatomicConcept("C0041967","13648007", False,#unpaired
        "SRT", "SNM3", None, "T-75000", "Urethra", "URETHRA", None,
        ["Urethra"], ["Urethra"]),
    DisplayableAnatomicConcept("C0042149","35039007", False,#unpaired
        "SRT", "SNM3", None, "T-83000", "Uterus", "UTERUS", None,
        ["Uterus"], ["Uterus"]),
    DisplayableAnatomicConcept("C0042232","76784001", False,#unpaired
        "SRT", "SNM3", None, "T-82000", "Vagina", "VAGINA", None,
        ["Vagina"], ["Vagina"]),
    DisplayableAnatomicConcept("C0729900","312548007", False,#unpaired
        "SRT", "SNM3", None, "T-46006", "Ventral branch of abdominal aorta",
        None, None,
        ["Ventral branch of abdominal aorta"],
        ["Ventral branch of abdominal aorta"]),
    DisplayableAnatomicConcept("C0042993","45292006", False,#unpaired
        "SRT", "SNM3", None, "T-81000", "Vulva", "VULVA", None,
        ["Vulva"], ["Vulva"]),
    DisplayableAnatomicConcept("C1262468","74670003", True ,#paired
        "SRT", "SNM3", None, "T-15460", "Wrist joint", "WRIST",
        [
            "Wrist","muñeca",#ES
            "MUÒECA",#ES ? misspelled"pols",#NL
            "poignet",#FR"Handgelenk",#DE
            "καρπός",#GR"polso",#IT,PT
            "手首",#JP"손목",#KR
            "запястье руки",#RU"ranne",#EE
            "käe"#EE
            ], 
        ["Wrist joint"], ["Wrist joint"]),
    DisplayableAnatomicConcept(
        "C0162485","51204001", True ,#paired
        "SRT", "SNM3", None, "T-11167", "Zygomatic arch",
        "ZYGOMA", # need to change concept when CP 1258 is approved :(
        ["Zygoma"],["Zygomatic arch"], ["Zygomatic arch"]),
]
def removeAccentsFromLowerCaseString(txt: str) -> str:	
    txt = re.sub("[àáãäåāąăâ]","a", txt)
    txt = re.sub("[æ]","ae", txt)
    txt = re.sub("[çćĉċ]","c", txt)
    txt = re.sub("[ďđ]","d", txt)
    txt = re.sub("[èéêëēęěĕė]","e", txt)
    txt = re.sub("[ƒ]","f", txt)
    txt = re.sub("[ĝğġģ]","g", txt)
    txt = re.sub("[ĥħ]","h", txt)
    txt = re.sub("[ìíîïīĩĭįı]","i", txt)
    txt = re.sub("[ĳ]","ij", txt)
    txt = re.sub("[ĵ]","j", txt)
    txt = re.sub("[ĸ]","k", txt)
    txt = re.sub("[łľĺļŀ]","l", txt)
    txt = re.sub("[ñńňņŉŋ]","n", txt)
    txt = re.sub("[òóôõöøōőŏ]","o", txt)
    txt = re.sub("[œ]","oe", txt)
    txt = re.sub("[ŕřŗ]","r", txt)
    txt = re.sub("[śšşŝș]","txt", txt)
    txt = re.sub("[ťţŧț]","t", txt)
    txt = re.sub("[ùúûüūůűŭũų]","u", txt)
    txt = re.sub("[ŵ]","w", txt)
    txt = re.sub("[ýÿŷ]","y", txt)
    txt = re.sub("[žżź]","z", txt)
    txt = re.sub("[ß]","ss", txt)
    return txt


def isBadLateralityOrViewOrAnatomyPhraseTriggers(keyText: str) -> bool:
    badLateralityOrViewOrAnatomyPhraseTriggers = [
        "History",
        "Hx of",
    ]
    keyText = keyText.lower()
    for bad_w in badLateralityOrViewOrAnatomyPhraseTriggers:
        if re.search(bad_w.lower(), keyText) is not None:
            return True
    return False


def removeAnyBadWords(string: str) -> str:
    for badWord in badAnatomyWords:
        string = re.sub(badWord.lower()," ", string)
        string = re.sub(r'\s{2}'," ", string)
        cleanedText = re.sub(r'\s*(.*)',r'\g<1>', string)
        cleanedText = re.sub(r'(.*)\s*',r'\g<1>', cleanedText)
    return string


def findLongestIndividualEntryContainedWithin(
        keyText: str) -> DisplayableAnatomicConcept:
    entry = None
    cleanedText = keyText.lower()
    cleanedText = removeAccentsFromLowerCaseString(cleanedText)
    cleanedText = re.sub(r'[^a-zA-Z0-9]',' ', cleanedText)		
    cleanedText = re.sub(r'\n{2,}', ' ', cleanedText)
    cleanedText = re.sub(r'\s{2,}', ' ', cleanedText)
    cleanedText = re.sub(r'^\s+(.*)',r'\g<1>', cleanedText)
    cleanedText = re.sub(r'(.*)\s+$',r'\g<1>', cleanedText)
    cleanedText = removeAnyBadWords(cleanedText)
    if len(cleanedText) > 0:
        lengthFound=0;
        for concept in anatomicConceptEntries:
            codeMeaning = concept.CodeMeaning.lower()
            s_res = re.search(codeMeaning, cleanedText)
            if s_res is not None:
                tryLength = len(codeMeaning)
                if tryLength > lengthFound:
                    entry = concept
                    lengthFound = tryLength
            synonyms = concept.Synonynms
            for synonym in synonyms:
                synonym = synonym.lower()
                synonym = removeAccentsFromLowerCaseString(synonym);
                s_res = re.search(synonym, cleanedText)
                if s_res is not None:
                    tryLength = len(synonym)
                    if tryLength > lengthFound:
                        entry = concept
                        lengthFound = tryLength
    return entry