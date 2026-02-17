document.addEventListener("DOMContentLoaded", function () {

    const flyout = document.createElement("div");
    flyout.className = "sidebar-flyout";
    document.body.appendChild(flyout);

    function showFlyout(title, links) {
        flyout.innerHTML = `<h4>${title}</h4>` + links.map(
            l => `<a href="${l.url}">${l.label}</a>`
        ).join("");
        flyout.classList.add("active");
    }

    function hideFlyout() {
        flyout.classList.remove("active");
    }

    const groups = {
        "Financeiro": {
            title: "Financeiro",
            links: [
                { label: "Contas a Pagar", url: "/admin/financeiro/contapagar/" },
                { label: "Contas a Receber", url: "/admin/financeiro/contareceber/" },
                { label: "Impostos", url: "/admin/financeiro/imposto/" }
            ]
        },
        "Clientes": {
            title: "Clientes",
            links: [
                { label: "Empresas", url: "/admin/clientes/cliente/" },
                { label: "Contatos", url: "/admin/clientes/contatocliente/" }
            ]
        },
        "Gestão Metrológica": {
            title: "Gestão Metrológica",
            links: [
                { label: "Instrumentos", url: "/admin/calibracao/instrumento/" },
                { label: "Calibrações", url: "/admin/calibracao/calibracao/" },
                { label: "Padrões", url: "/admin/calibracao/padrao/" }
            ]
        }
    };

    document.querySelectorAll(".nav-sidebar .nav-item").forEach(item => {
        const text = item.innerText.trim();
        if (!groups[text]) return;

        item.addEventListener("mouseenter", () => {
            showFlyout(groups[text].title, groups[text].links);
        });

        item.addEventListener("mouseleave", () => {
            setTimeout(() => {
                if (!flyout.matches(":hover")) hideFlyout();
            }, 150);
        });
    });

    flyout.addEventListener("mouseleave", hideFlyout);
});

