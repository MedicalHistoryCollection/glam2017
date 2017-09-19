/**
 * Created by ljaouen on 15.09.17.
 */
//let $ = require('jquery');
//require("./bower_components/jqcloud2/dist/jqcloud.min");

var cwords = [
	{text: "Anatomie", weight: 10, link: 'https://github.com/MedicalHistoryCollection/glam2017'},
	{text: "Anatomie", link: 'https://github.com/MedicalHistoryCollection/glam2017/10', weight: 10 },
	{text: "Histologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/10a', weight: 100},
	{text: "Pharmacie", link: 'https://github.com/MedicalHistoryCollection/glam2017/16a', weight: 160},
	{text: "Odontostomatologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/27', weight: 27},
	{text: "Cardiologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/30a', weight: 3001},
	{text: "Gastéroentérologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/30c', weight: 3003},
	{text: "Neurologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/30g', weight: 3007},
	{text: "Pédiatrie, néonatalogie", link: 'https://github.com/MedicalHistoryCollection/glam2017/30l', weight: 3009},
	{text: "Ophtalmologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/30s', weight: 3015},
	{text: "Vénéro-dermatologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/30u', weight: 3016},
	{text: "Diagnostic", link: 'https://github.com/MedicalHistoryCollection/glam2017/40', weight: 1000},
	{text: "Chirurgie générale", link: 'https://github.com/MedicalHistoryCollection/glam2017/45a', weight: 450},
	{text: "Chirurgie cardio-vasculaire", link: 'https://github.com/MedicalHistoryCollection/glam2017/45b', weight: 451},
	{text: "Obstétrique, gynécologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/45h', weight: 456},
	{text: "Orthopédie, traumatologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/45j', weight: 457},
	{text: "Oto-rhino-laryngologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/45k', weight: 458},
	{text: "Urologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/45l', weight: 459},
	{text: "Anesthésiologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/46', weight: 46},
	{text: "Radiologie", link: 'https://github.com/MedicalHistoryCollection/glam2017/47', weight: 47},
	{text: "Médecine sociale et préventive", link: 'https://github.com/MedicalHistoryCollection/glam2017/72', weight: 72}
];

jQuery('cloudwords').jQCloud(cwords);
