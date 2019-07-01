var BASE_URL = localStorageGetItem("baseUrl") || "https://api.judge0.com";
    var SUBMISSION_CHECK_TIMEOUT = 10; // in ms
    var WAIT = localStorageGetItem("wait") == "true";
    var sourceEditor, inputEditor, outputEditor;
    var $insertTemplateBtn, $selectLanguageBtn, $vimCheckBox;
    var $statusLine, $emptyIndicator;
    var timeStart, timeEnd;
    $runBtn = $("#runBtn");
    $saveBtn = $("#saveBtn");

    $(document).ready(function() {
        editor.setValue("#Hello completer le code\n \ndef somme_n(n):\n    #code ici\n    return #valeur a retourner");
    });

    function handleError(jqXHR, textStatus, errorThrown) {
        console.log(JSON.stringify(jqXHR, null, 4));
        $statusLine.html(`${jqXHR.statusText} (${jqXHR.status})`);
    }
    function handleRunError(jqXHR, textStatus, errorThrown) {
        handleError(jqXHR, textStatus, errorThrown);
        $runBtn.button("reset");

    }
    function fetchSubmission(submission_token) {
        $.ajax({
            url: BASE_URL + "/submissions/" + submission_token + "?base64_encoded=true",
            type: "GET",
            async: true,
            success: function(data, textStatus, jqXHR) {
                if (data.status.id <= 2) { // In Queue or Processing
                    setTimeout(fetchSubmission.bind(null, submission_token), SUBMISSION_CHECK_TIMEOUT);
                    return;
                }
                handleResult(data);
            },
            error: handleRunError
        });
    }
    function localStorageSetItem(key, value) {
        try {
            localStorage.setItem(key, value);
        } catch (ignorable) {
        }
    }
    function localStorageGetItem(key) {
        try {
            return localStorage.getItem(key);
        } catch (ignorable) {
            return null;
        }
    }

    function handleResult(data) {
        console.log(data)
        timeEnd = performance.now();
        console.log("It took " + (timeEnd - timeStart) + " ms to get submission result.");

        var status = data.status;
        var stdout = decodeURIComponent(escape(atob(data.stdout || "")));
        var stderr = decodeURIComponent(escape(atob(data.stderr || "")));
        var compile_output = decodeURIComponent(escape(atob(data.compile_output || "")));
        var message = decodeURIComponent(escape(atob(data.message || "")));
        var time = (data.time === null ? "-" : data.time + "s");
        var memory = (data.memory === null ? "-" : data.memory + "KB");

        if (status.id == 6) {
            stdout = compile_output;
        } else if (status.id == 13) {
            stdout = message;
        } else if (status.id != 3 && stderr != "") { // If status is not "Accepted", merge stdout and stderr
            stdout += (stdout == "" ? "" : "\n") + stderr;
        }

        if (status.id == 4){
            console.log('code incorrecte')
        }

        
        well(stdout);
    }
    function run() {
        if (editor.getValue().trim() == "") {
            alert("Editeur vide!");
            return;
        } else {

            var str = editor.getValue();

             var code = str.indexOf("return");
            console.log(code)
            //str = str.find("print").remove();
            str = str + '\nprint(somme_n(10))'
            console.log(str);
        }

        

        var sourceValue = btoa(unescape(encodeURIComponent(str)));
        var inputValue = btoa(unescape(encodeURIComponent(inputEditor)));
        //var stdin = btoa(unescape(encodeURIComponent(code)));
        var languageId =  34;
        var expected_output = btoa(unescape(encodeURIComponent(55)))
        var data = {
            source_code: sourceValue,
            language_id: languageId,
            //stdin: stdin,
            expected_output: expected_output
        };

        timeStart = performance.now();
        $.ajax({
            url: BASE_URL + `/submissions?base64_encoded=true&wait=${WAIT}`,
            type: "POST",
            async: true,
            contentType: "application/json",
            data: JSON.stringify(data),
            success: function(data, textStatus, jqXHR) {
                console.log(`Your submission token is: ${data.token}`);
                if (WAIT == true) {

                    handleResult(data);
                    

                } else {
                    setTimeout(fetchSubmission.bind(null, data.token), SUBMISSION_CHECK_TIMEOUT);
                }
            },
            error: handleRunError
        });
    }

    function well(a){
        if (a == 55){
            $("#vue").html('<span class="info"> Success</span>');
        }else{
            $("#vue").html('<span class="error"> Error\n '+a+' </span>');
        }

            
    }

    function btnrun(){
        $("#vue").html('Run');
    }

    function btnrun(){
        $("#vue").html('Run');
    }