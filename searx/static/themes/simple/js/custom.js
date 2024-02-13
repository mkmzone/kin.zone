let searchForm = document.getElementById("search");
let searchFormInput = document.getElementById("q");
let clearSearch = document.getElementById('clear_search');

/*
searchForm.addEventListener("click", function(e){   
    if(e.target.matches(".autocomplete ul")){
        document.forms["search"].submit();
    }
});
*/

searchFormInput.addEventListener("focusout", function(e){   
    if(!searchFormInput.value && searchFormInput.getAttribute("value")){
        searchFormInput.value = searchFormInput.getAttribute("value");
        clearSearch.classList.remove("empty");    
    }
});

function showNavDropdownMenu() {
    document.getElementById("nav_dropdown_menu").classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.closest('#nav_dropdown')) {
        let navDropdownMenu = document.getElementById("nav_dropdown_menu");
        if(navDropdownMenu.classList.contains('show')){
            navDropdownMenu.classList.remove('show');
        }
    }
} 

//documen

//let onAutoCompleteClick = function(e){if(e.target.tagName ==="li"){document.forms["search"].submit();}};
