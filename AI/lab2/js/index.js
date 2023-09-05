    // css
import 'normalize.css';
import './../css/main.scss';

    // js
import $ from 'jquery';

$(function() {
    const btnNext = document.getElementById('next');
    let curForm = document.querySelector('form.active');

    btnNext.addEventListener('click', () => {
        let curArrayName = 'inputs' + curForm.id.replace('-',' ').capitalize(true).replace(' ','')
        console.log(curForm.id.replace('-',' ').capitalize(true).replace(' ',''))
        console.log(curArrayName)
        let curArray = makeList("curArrayName");

        Array.prototype.forEach.call(document.querySelectorAll('input[name='+curForm.id+']'), function(element){
            curArray.push(element);
        });
        console.log(curArray)

        let result = curArray.filter(input => input.checked == true)[0];

        console.log(result.id)
        switch(result.id) {
            case 'unclear':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-one-unclear');
                curForm.classList.add('active');
                break;
            case 'first-time':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-one-first-time');
                curForm.classList.add('active');
                break;
            case 'storm':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-one-storm');
                curForm.classList.add('active');
                break;
            case 'unclear-yes':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-two-unclear');
                curForm.classList.add('active');
                break;
            case 'unclear-no':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-one-first-time');
                curForm.classList.add('active');
                break;
            case 'first-time-yes':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-two-unclear');
                curForm.classList.add('active');
                break;
            case 'first-time-no':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-two-other');
                curForm.classList.add('active');
                break;
            case 'storm-yes':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-last');
                curForm.classList.add('active');
                break;
            case 'storm-no':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-one-first-time');
                curForm.classList.add('active');
                break;
            case 'two-unclear-yes':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-last');
                curForm.classList.add('active');
                break;
            case 'two-unclear-no':
                curForm.classList.remove('active');
                curForm = document.querySelector('#result');
                curForm.classList.add('active');
                curForm.querySelector('p#result-one').classList.add('active');
                btnNext.style.display="none";
                break;
            case 'other-yes':
                curForm.classList.remove('active');
                curForm = document.querySelector('form#form-two-unclear');
                curForm.classList.add('active');
                break;
            case 'other-no':
                curForm.classList.remove('active');
                curForm = document.querySelector('#result');
                curForm.classList.add('active');
                curForm.querySelector('p#result-one').classList.add('active');
                btnNext.style.display="none";
                break;
            case 'last-yes':
                curForm.classList.remove('active');
                curForm = document.querySelector('#result');
                curForm.classList.add('active');
                curForm.querySelector('p#result-two').classList.add('active');
                btnNext.style.display="none";
                break;
            case 'last-no':
                curForm.classList.remove('active');
                curForm = document.querySelector('#result');
                curForm.classList.add('active');
                curForm.querySelector('p#result-three').classList.add('active');
                btnNext.style.display="none";
                break;
        }
    })

    function makeList(name){
        window[name] = [];
        return window[name];
    }

    String.prototype.capitalize = function(allWords) {
        return (allWords) ? // If all words
            this.split(' ').map(word => word.capitalize()).join(' ') :
            this.charAt(0).toUpperCase() + this.slice(1);
    }
});