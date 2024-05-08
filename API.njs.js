import React, { useState, useEffect } from 'react';

const API_URL = 'http://20.244.56.144/test';

const AllProductsPage = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`${API_URL}/companies/AMZ/categories/Laptop/products?top=10&minPrice=1&maxPrice=10000`);
        if (response.ok) {
          const data = await response.json();
          setProducts(data);
        } else {
          console.error('Failed to fetch data');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1>All Products</h1>
      <ul>
        {products.map(product => (
          <li key={product.productName}>
            {product.productName} - ${product.price}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AllProductsPage;
