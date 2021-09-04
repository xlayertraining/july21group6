import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NetworkService } from 'src/app/service/network.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  productList: any = [];

  constructor(private router: Router, private networkService: NetworkService) {
    this.networkService.updateHeaders();
  }

  ngOnInit(): void {
    this.getProducts();
  }

  onSignOut(): void {
    localStorage.clear();
    this.router.navigate(['sign_in']);
  }

  onAddProduct(): void {
    this.router.navigate(['add_product']);
  }

  getProducts(): void {
    
    this.networkService.getProduct().subscribe( success => {
      console.log(success);
      if (success.status == true) {
        this.productList = success.result;
      } else {
        // alert(success.message);
      }
      
    }, error => {

    });
  }

}
