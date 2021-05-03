% import model

<!DOCTYPE html>
<html>

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

    % elif poskus == model.poraz:
    <h2>Izgubili ste!</h2>
    Pravilno geslo je bilo {{igra.geslo}}
    
    % else: 
    <form action="/igra/{{id_igre}}/" method="post">
        <input type="text" name="crka" autofocus>
        <button type="submit">Ugibaj!</button>
    </form>

    % end

</body>

</html>