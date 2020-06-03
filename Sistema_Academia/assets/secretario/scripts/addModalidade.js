$(function () {
    let modalidade = $('#modalidades');
    let element  = document.getElementsByName('modalidade');
    let classe = document.getElementById('modalidades');
    /*
    Adiciona um select embaixo do anteiror junto com o hr
    childElementCount = modalidade + N*(modalidades + hr)
    A tag 'name' será usada para indentificar o valor do input no views.py
    */
    $("#addInput").on('click',function () {
        $(  '<hr>' +
            '<select class="form-control" name="modalidade'+`${($(classe)[0].childElementCount-1)/2}`+'" id="modalidade" >' +
            '<option value="nselecionado" >Selecione a Modalidade</option>' +
            '<option value="musculacao" >Musculação</option>' +
            '<option value="natacao" >Natação</option>' +
            '<option value="variado" >Variado</option>' +
            '</select>').appendTo(modalidade);
        return false;
    });
    $("#remove").on('click',function () {
        let hr = $(element[element.length-1])[0].previousElementSibling;
        $(hr)[0].remove()
        $(element[element.length-1])[0].remove();
        return false;
    });
});