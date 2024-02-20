let searchForm = document.getElementById("search");
let searchFormInput = document.getElementById("q");
let clearSearch = document.getElementById('clear_search');
let sendSearch = document.getElementById('send_search');
let searchView = document.getElementById('search_view');
let searchBox = document.getElementById('search_box_area');

if(searchFormInput){
    searchFormInput.addEventListener("focusout", function(e){   
        if(!searchFormInput.value && searchFormInput.getAttribute("value")){
            searchFormInput.value = searchFormInput.getAttribute("value");
            clearSearch.classList.remove("empty");    
        }
    });
}

if(clearSearch){   
    clearSearch.addEventListener("mousedown", function(e){
        e.preventDefault();
        searchFormInput.value = "";
        clearSearch.classList.remove("empty");
    });   
}

if(sendSearch){
    sendSearch.addEventListener("mousedown", function(e){
        e.preventDefault();
        searchForm.submit();
    });
}

document.getElementById("nav_dropdown").onclick = function (event) {
    document.getElementById("nav_dropdown_menu").classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.closest('#nav_dropdown')) {
        let navDropdownMenu = document.getElementById("nav_dropdown_menu");
        if(navDropdownMenu.classList.contains('show')){
            navDropdownMenu.classList.remove('show');
        }
    }
    //event.preventDefault();
    //alert(event.target.tagName);
    //console.log(`${event.type}, ${event.target}, ${event.target.classList}, ${event.originalTarget}, `);
    //alert(event.currentTarget.tagName);
} 


function setLogs(element) {
    element.addEventListener("focus", () => {
        console.log("focus", element.tagName);
    });
    element.addEventListener("blur", () => {
        console.log("blur", element.tagName);
    });
    element.addEventListener("mousedown", () => {
        console.log("mousedown", element.tagName);
    });
    element.addEventListener("mouseup", () => {
        console.log("mouseup", element.tagName);
    });
    element.addEventListener("click", () => {
        console.log("click", element.tagName);
    });

    for (const child of element.children)
        setLogs(child);
}

//setLogs(document.body);