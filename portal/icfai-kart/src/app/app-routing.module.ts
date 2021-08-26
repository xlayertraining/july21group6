import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SignInPageComponent } from './components/sign-in-page/sign-in-page.component';
import { SignUpPageComponent } from './sign-up-page/sign-up-page.component';
const routes: Routes = [
  {
    path: '',
    redirectTo: 'sign_in',
    pathMatch: 'full'
  },
  {
    path: "sign_in",
    component: SignInPageComponent
  },
  {
    path: "sign_up",
    component: SignUpPageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
