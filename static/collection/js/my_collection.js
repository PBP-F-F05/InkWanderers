async function getHistoryBook() {
    return fetch("/account/get-history-book-json").then((res) => res.json())
}
async function refreshProducts() {
    const bookRecords = await getHistoryBook();
    let htmlString = ``;

    bookRecords.forEach((record) => {
        const book = record.book;
        console.log("Line 10: -->"+record.date_added);
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
                    <p  class="book-review-count">${book.review_count} | </p>
                    <i class="fa fa-calendar" aria-hidden="true"></i>
                    <p  class="books-count">${record.date_added}</p>
                </div>
            </div>
        </a>
        
        `
    })
    
    document.getElementById("list-books").innerHTML = htmlString
}

refreshProducts()
