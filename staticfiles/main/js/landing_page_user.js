async function getProducts() {
    return fetch("/get_books_json").then((res) => res.json())
} 

async function refreshProducts() {
    const productCardsContainer = document.getElementById("product_cards");
    productCardsContainer.innerHTML = "";
    const products = await getProducts();
    const searchInput = document.getElementById("search");
    const searchText = searchInput.value.trim().toLowerCase();
    const searchCategory = document.getElementById("searchCategory").value;
    products.forEach((product) => {
        const productValue = product.fields[searchCategory].toLowerCase();
        

        if (productValue.includes(searchText) || (searchText === "")) {
        const card = document.createElement("div");
        card.classList.add("col-3");

        card.innerHTML = `
            <div class="card mb-3 book-card">
                <img src='${product.fields.thumbnail}' alt="${product.fields.title} cover image" class="book-cover">
                <div class="product-information">   
                    <div class="card-body"> 
                    <p class="book-title">${product.fields.title}</p>
                    <p class="book-authors">${product.fields.authors}</p>
                    <p class="book-text">${truncateDescription(product.fields.description, 100)}</p>
                    </div>
                    <div class="review-container">
                        <div class="d-flex">
                            <i class="fa fa-star" aria-hidden="true"></i>
                            <p  class="book-review-count">${product.fields.review_points/product.fields.review_count} | </p>
                        </div>
                        <a href="/reviews/${product.pk}">See reviews</a>
                    </div>
                </div>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">Year published: ${product.fields.published_year}</li>
                </ul>
                <div class="card-body">
                    <div class="d-flex"> 
                        <a href="/bookmarks/bookmark-book/${product.pk}" type="button" class="btn btn-primary" style="margin:10px" >Add to Bookmark</a>
                        <a href="/collection/add-book/${product.pk}" type="button" class="btn btn-primary" style="margin:10px" >Add to Collection</a>
                    </div>
                </div>
            </div>`;

        productCardsContainer.appendChild(card);
        }
    });
    
    document.getElementById("list-books").innerHTML = htmlString
}

function truncateDescription(description, limit) {
    if (description.length > limit) {
        return description.substring(0, limit) + '...';
    }
    return description;
}


// Attach the refreshProducts function to the input field's input event
const searchInput = document.getElementById("search");
searchInput.addEventListener("input", refreshProducts);

// Attach the refreshProducts function to the select element's change event
const searchCategorySelect = document.getElementById("searchCategory");
searchCategorySelect.addEventListener("change", refreshProducts)


refreshProducts()