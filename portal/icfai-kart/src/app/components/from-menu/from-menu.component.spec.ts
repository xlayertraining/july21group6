import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FromMenuComponent } from './from-menu.component';

describe('FromMenuComponent', () => {
  let component: FromMenuComponent;
  let fixture: ComponentFixture<FromMenuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FromMenuComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FromMenuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
