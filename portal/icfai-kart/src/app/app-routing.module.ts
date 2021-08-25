import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SignInPageComponent } from './components/sign-in-page/sign-in-page.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'sign_in',
    pathMatch: 'full'
  },
  {
    path: "sign_in",
    component: SignInPageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
