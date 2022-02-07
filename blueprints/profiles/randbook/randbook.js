let btn = document.getElementById('btn');
let output = document.getElementById('output');
let quotes = [
    "Madame Bovary by Gustave Flaubert",
    "Ulysses by James Joyce",
    "In Search of Lost Time by Marcel Proust",
    "Don Quixote by Miguel de Cervantes",
    "One Hundred Years of Solitude by Gabriel Garcia Marques",
    "The Great Gatsby by F. Scott Fitzgerald",
    "Moby Dick by Herman Melville",
    "War and Peace by Leo Tolstoy",
    "Hamlet by William Shakespeare",
    "The Odyssey by Homer",
];

btn.addEventListener('click', function(){
    var randomQuote = quotes[Math.floor(Math.random() * quotes.length)]
    output.innerHTML = randomQuote;
})