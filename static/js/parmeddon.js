
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
script.type = 'text/javascript';

function delete_e(span)
{

    let headers = span.closest(".card").querySelectorAll(".card-header h2")

    let finnestringbe = ''
    let multiple = ''
    
    for (var n = 0; n < headers.length; n++)
    {
        if (headers.length == 0 || headers.length == 1)
        {
            finnestringbe += headers[n].innerHTML
            break
        }

        else {
            let h2 = headers[n]
            finnestringbe += `${h2.innerHTML + '|'}`
            multiple =  finnestringbe.slice(0,-1)
        }
       
    }

    console.log(finnestringbe);
    let target = span.closest('article')
    target.remove()

    if (multiple == '')
    {
        $.post( "/delete", {
            // ': String(e.closest('h2'))
            'javascript_data': `${finnestringbe}`

        });
    }
    else {
        $.post( "/delete", {
            // ': String(e.closest('h2'))
            'javascript_data': `${multiple}`

        });
    }
}

