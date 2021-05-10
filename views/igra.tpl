% import model

% rebase( 'base.tpl', title = 'igra')

<body>

    <table>
        <tr>
        <td>
            {{igra.pravilni_del_gesla()}}
        </td>
    </tr>

    <tr>
        <td>Nepravilne črke:</td>
        <td>{{igra.nepravilni_ugibi()}}</td>
    </tr>
    <tr>
        <td><img src="/img/{{igra.stevilo_napak()}}.jpg"> </td>
    </tr>
    </table>

    % if poskus == model.zmaga:
    <h1>Zmaga!</h1>
    Uganili ste pravilno geslo.    
    <form action='/nova_igra/' method = 'POST'>
        <button type = 'submit'>Nova igra</button>
    </form>

    % elif poskus == model.poraz:
    <h2>Izgubili ste!</h2>
    Pravilno geslo je bilo {{igra.geslo}}
    <form action='/nova_igra/' method = 'POST'>
        <button type = 'submit'>Nova igra</button>
    </form>

    % else: 
    <form action="/igra/" method="post">
        <input type="text" name="crka" autofocus>
        <button type="submit">Ugibaj!</button>
    </form>

    % end
