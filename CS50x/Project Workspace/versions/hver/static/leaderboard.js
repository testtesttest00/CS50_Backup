async function leaderboard(event){
    let button = event.target;
    let input = button.parentElement.querySelector("input");
    if (button.id == "enter"){
        if (document.getElementById("game").querySelector("thead").querySelector("td").innerHTML == "Solved!" && input.value != ""){
            let response = await fetch("/leaderboard", {
                method: "POST",
                headers: {"Content-type":"application/json"},
                body: JSON.stringify({player: input.value, moves: document.getElementById("turn").innerHTML})
            })
            let ranks = await response.json();
            let rows = " ";
            for (let row of ranks){
                rows += `<tr><td>${row[0]}</td><td>${row[1]}</td></tr>`;
            }

            input.value = "";
            button.disabled = true;
            document.getElementById("leaderboard").querySelector("tbody").innerHTML = rows;
        }
    }
    else if (button.id == "refresh"){
//                let response = await fetch("/leaderboard", {
//                    method: "POST",
//                    headers: {"Content-type":"application/json"},
//                    body: JSON.stringify({moves:"0"})
//                })
//                let ranks = await response.text();
        fetch("/leaderboard", {
            method: "POST",
            headers: {"Content-type":"application/json"},
            body: JSON.stringify({moves:"0"})
        }).then(response => response.json())
        .then(ranks => {
            let table = document.getElementById("leaderboard").querySelector("tbody");
            let rows = " ";
            ranks.forEach(row => {
                rows += `<tr><td>${row[0]}</td><td>${row[1]}</td></tr>`;
            });

            table.innerHTML = rows;
        });
    }
}
