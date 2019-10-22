$('#id_snils').mask('999-999-999 99');


//try {
//if (localStorage.getItem('me_reload') == 0) {
//	//location.reload();
//	//history.go(0);
//	//System.Windows.SendKeys.SendWait('^{F5}');
//	location.reload(false);
//	localStorage.setItem('me_reload', 1);
//}
//} catch {}

var m_e = document.getElementById('me_exit')
m_e.addEventListener('mouseover',me_reload)

function me_reload(){
	localStorage.setItem('me_reload', 0);
}


//window.onload = function() {
//	window.location.reload(false)
//}

var p = document.getElementById('id_kod_them');

p.setAttribute('data-toggle', 'tooltip');
p.setAttribute('data-placement', 'left');
p.setAttribute('title', 'Не забудьте выбрать тему обращения');

var btn = document.querySelectorAll('.btn');
for (var i = 0; i < btn.length; i++){
	btn[i].setAttribute('style', 'margin:2px;');	
}

// =========================================
// id_snils
// Проверка снилса

var in_t = document.getElementById('id_snils');
in_t.onblur = function(){
	//alert(1)
	var g_v = in_t.value;
	//alert(g_v)
	if (!check_snils(g_v)){
		//alert(g_v + ' ' + check_snils(g_v));
		$('.toast').toast('show');
	}
}

	

// =========================================



if (localStorage.getItem('me_collapseOne') == 1) {
	var myButtonClasses = document.getElementById("collapseOne").classList;
	myButtonClasses.add("show");
	var myButtonClasses_2 = document.getElementById("collapseTwo").classList;
	myButtonClasses_2.remove("show");
} else {
	var myButtonClasses = document.getElementById("collapseTwo").classList;
	myButtonClasses.add("show");
	var myButtonClasses_2 = document.getElementById("collapseOne").classList;
	myButtonClasses_2.remove("show");
}

// установка активной кнопки типа темы и активация темы
let me_cs_thema = document.querySelectorAll(".me_cs_thema");
let i_thema = localStorage.getItem('me_cs_thema')
try {
	me_cs_thema[i_thema].classList.add("active");
	let opt = document.querySelector('#id_kod_them').querySelectorAll('option');
	if (opt.length == 1 && i_thema != 8 ) {
		me_cs_thema[localStorage.getItem('me_cs_thema')].click();
	}
} catch {
	
}

// сохранение последей темы

document.querySelector("#id_thema_1").onclick = function(){
	localStorage.setItem('me_cs_thema', 0);
}

document.querySelector("#id_thema_2").onclick = function(){
	localStorage.setItem('me_cs_thema', 1);
}

document.querySelector("#id_thema_3").onclick = function(){
	localStorage.setItem('me_cs_thema', 2);
}

document.querySelector("#id_thema_4").onclick = function(){
	localStorage.setItem('me_cs_thema', 3);
}

document.querySelector("#id_thema_5").onclick = function(){
	localStorage.setItem('me_cs_thema', 4);
}

document.querySelector("#id_thema_6").onclick = function(){
	localStorage.setItem('me_cs_thema', 5);
}

document.querySelector("#id_thema_7").onclick = function(){
	localStorage.setItem('me_cs_thema', 6);
}

document.querySelector("#id_thema_8").onclick = function(){
	localStorage.setItem('me_cs_thema', 7);
}

document.querySelector("#id_thema_9").onclick = function(){
	localStorage.setItem('me_cs_thema', 8);
}


document.getElementById("me_collapseOne").onclick = function() {
	//alert(1)
	localStorage.setItem('me_collapseOne', 1);
	localStorage.setItem('me_collapseTwo', 0);
}

document.getElementById("me_collapseTwo").onclick = function() {
	//alert(2)
	localStorage.setItem('me_collapseOne', 0);
	localStorage.setItem('me_collapseTwo', 1);
}


$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

function check_snils(value) {
  var pattern = /^(\d{3})\-(\d{3})\-(\d{3})\s(\d{2})$/
  var isTrueLength = value.replace(/\D/gm, '').length == 11

  if (!isTrueLength || !pattern.test(value)) {
    return false
  }

  var valueClean = value.replace(/-/g, "");
  var valueFinal = valueClean.replace(" ", "");

  var checkSum = parseInt(valueFinal.slice(9), 10);

  // представить строку как массив (для старых браузеров)
  valueFinal = "" + valueFinal;
  valueFinal = valueFinal.split('');

  var sum = (
    valueFinal[0] * 9 +
    valueFinal[1] * 8 +
    valueFinal[2] * 7 +
    valueFinal[3] * 6 +
    valueFinal[4] * 5 +
    valueFinal[5] * 4 +
    valueFinal[6] * 3 +
    valueFinal[7] * 2 +
    valueFinal[8] * 1
  );

  if (sum < 100) {
    return sum == checkSum
  }

  if (sum == 100 || sum == 101) {
    return checkSum == 0;
  }

  if (sum > 101) {
    return (sum % 101 == checkSum || (sum % 101 == 100 && checkSum == 0));
  }
}
