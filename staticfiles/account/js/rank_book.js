async function getRankBook() {
    return fetch("/account/get-rank-book-json").then((res) => res.json())
}
async function refreshProducts() {
    const bookRecords = await getRankBook();
    let htmlString = ``;
    const searchInput = document.getElementById("search");
    const searchText = searchInput.value.trim().toLowerCase();
    const searchCategory = document.getElementById("searchCategory").value;

    bookRecords.forEach((record) => {

        const book = record.book;
        const productValue = book[searchCategory].toLowerCase();
        let totalPoint = book.review_points/book.review_count
        if (productValue.includes(searchText) || (searchText === "")) {
            htmlString += 
            `
            <a href="" class="product-box-a">
                <img src='${book.thumbnail}' alt="${book.title} cover image">
    
                <div class="product-information">   
                    <div class="product-information2"> 
                        <p class="book-title">${book.title}</p>
                        <p  class="book-authors">${book.authors}</p>
                    </div>
                    <div class="review-container">
                        <i class="fa fa-star" aria-hidden="true"></i>
                        <p  class="book-review-count">${totalPoint} | </p>
                        <i class="fa fa-book" aria-hidden="true"></i>
                        <p  class="books-count">${record.books_count}</p>

                    </div>
                </div>
            </a>\n
            
            `
        }
    })
    
    document.getElementById("list-books").innerHTML = htmlString
}
const searchInput = document.getElementById("search");
searchInput.addEventListener("input", refreshProducts);

// Attach the refreshProducts function to the select element's change event
const searchCategorySelect = document.getElementById("searchCategory");
searchCategorySelect.addEventListener("change", refreshProducts)
refreshProducts()