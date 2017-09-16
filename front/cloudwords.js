/**
 * Created by ljaouen on 15.09.17.
 */
let $ = require('jquery');
require("./bower_components/jqcloud2/dist/jqcloud.min");

var cwords = [
	{text: "Anatomie", weight: 10, link: 'https://github.com/MedicalHistoryCollection/glam2017'},
	{text: "Histologie", weight: 100, link: 'https://github.com/MedicalHistoryCollection/glam2017'},
	{text: "Pharmacie", weight: 160, link: 'https://github.com/MedicalHistoryCollection/glam2017rg'}
];

$('#cloudwords').jQCloud(cwords);
