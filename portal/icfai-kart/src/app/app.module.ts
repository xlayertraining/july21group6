import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Router, RouterModule } from '@angular/router';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatCommonModule } from '@angular/material/core';
import { MatInputModule } from '@angular/material/input';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatButtonModule } from '@angular/material/button';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { SignInComponent } from './components/sign-in/sign-in.component';
import { HomeComponent } from './components/home/home.component';
import { EditProductComponent } from './components/product/edit-product/edit-product.component';
import { MyProductsComponent } from './components/product/my-products/my-products.component';
import { AddProductComponent } from './components/product/add-product/add-product.component';
import { HashLocationStrategy, LocationStrategy } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { FromMenuComponent } from './components/from-menu/from-menu.component';
import {MatCardModule} from '@angular/material/card';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatMenuModule} from '@angular/material/menu';
import { SingleProductComponent } from './components/product/single-product/single-product.component';
import { HttpClientModule } from '@angular/common/http';



@NgModule({
  declarations: [
    AppComponent,
    SignUpComponent,
    SignInComponent,
    HomeComponent,
    AddProductComponent,
    MyProductsComponent,
    EditProductComponent,
    FromMenuComponent,
    SingleProductComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatFormFieldModule,
    MatCommonModule,
    MatInputModule,
    FlexLayoutModule,
    MatButtonModule,
    RouterModule,
    MatIconModule,    
    MatCardModule,
    MatGridListModule,
    MatMenuModule,
    HttpClientModule,
  ],
  providers: [
    {
        provide: LocationStrategy,
        useClass: HashLocationStrategy
    }
],
  bootstrap: [AppComponent]
})
export class AppModule {

  constructor(private router: Router) {

    // this.router.navigate(['/sign_in']);
    // console.log('redirected');

  }

}
