import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NetworkService } from 'src/app/service/network.service';

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.scss']
})
export class AddProductComponent implements OnInit {

  productName: String = '';
  productPrice: String = '';
  productDesc: String = '';
  productDetails: String = '';
  whatsappNumber: String = '';

  constructor(private networkService: NetworkService, private router: Router) { }

  ngOnInit(): void {
  }

  onSubmit() {

    const restBody = {
      productName: this.productName,
      price: this.productPrice,
      description: this.productDesc,
      details: this.productDetails,
      whatsappNumber: this.whatsappNumber
    };

    console.log('main_body', restBody);

    this.networkService.postProduct(restBody).subscribe( success => {
      console.log(success);
      if (success.status == true) {
        // sign in success
        // localStorage.setItem(environment.authKey, success.result[0].Authorization);
        this.router.navigate(['home']);
      } else {
        alert(success.message);
      }
      
    }, error => {

    });
  }

}
