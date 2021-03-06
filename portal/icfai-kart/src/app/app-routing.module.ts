import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { AddProductComponent } from './components/product/add-product/add-product.component';
import { EditProductComponent } from './components/product/edit-product/edit-product.component';
import { MyProductsComponent } from './components/product/my-products/my-products.component';
import { SignInComponent } from './components/sign-in/sign-in.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { FromMenuComponent } from './components/from-menu/from-menu.component';
import { SingleProductComponent } from './components/product/single-product/single-product.component';
const routes: Routes = [  
  {
    path: "",
    component: SignInComponent
  },
  {
    path: "sign_in",
    component: SignInComponent
  },
  {
    path: "sign_up",
    component: SignUpComponent
  },
  {
    path: "home",
    component: HomeComponent
  },
  {
    path: "my_products",
    component: MyProductsComponent
  },
  {
    path: "add_product",
    component: AddProductComponent
  },
  {
    path: "edit_product",
    component: EditProductComponent
  },
  {
    path: "from_menu",
    component: FromMenuComponent
  },
  {
    path: "single_product",
    component: SingleProductComponent

  }
];

@NgModule({
  imports: [
  CommonModule,
  RouterModule.forRoot(routes,{
  useHash: true
  })
  ],
  exports: [
  ],
})
export class AppRoutingModule { }
