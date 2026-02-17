(function () {
    function ready(fn) {
        if (document.readyState !== "loading") {
            fn();
        } else {
            document.addEventListener("DOMContentLoaded", fn);
        }
    }

    ready(function () {
        const $ = django.jQuery; // 🔴 ISSO É O PONTO-CHAVE

        const instrumentoSelect = $("#id_instrumento");

        if (!instrumentoSelect.length) {
            console.warn("Campo instrumento não encontrado");
            return;
        }

        instrumentoSelect.on("select2:select", function (e) {
            const instrumentoId = e.params.data.id;

            if (!instrumentoId) return;

            fetch(`/calibracao/api/instrumento/${instrumentoId}/`)
                .then(response => response.json())
                .then(data => {
                    $("#id_descricao").val(data.descricao || "");
                    $("#id_marca").val(data.marca || "");
                    $("#id_modelo").val(data.modelo || "");
                    $("#id_tipo").val(data.tipo || "");
                    $("#id_numero_serie").val(data.numero_serie || "");
                })
                .catch(err => {
                    console.error("Erro ao carregar snapshot:", err);
                });
        });
    });
})();

