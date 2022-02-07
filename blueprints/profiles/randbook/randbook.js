var books = [
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

function newBook() {
    var randomNumber = Math.floor(Math.random() * (books.length));
    document.getElementById('bookDisplay').innerHTML = books[randomNumber];
}